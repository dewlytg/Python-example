#!/usr/bin/env python

from modules import models
from conf import settings
from modules.utils import print_err,yaml_parser
from modules.db_conn import session,engine
from modules import common_filters
from modules import ssh_login
import sys


def syncdb(argvs):
    print("Syncing DB....")
    engine = models.create_engine(settings.ConnParams,echo=True)
    models.Base.metadata.create_all(engine) #创建所有表结构

def create_hosts(argvs):
    '''
    create hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        hosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new hosts file>",quit=True)
    source = yaml_parser(hosts_file)
    if source:
        print(source)
        for key,val in source.items():
            print(key,val)
            obj = models.Host(hostname=key,ip=val.get('ip'), port=val.get('port') or 22)
            session.add(obj)
        session.commit()

def create_remoteusers(argvs):
    '''
    create remoteusers
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        remoteusers_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_remoteusers -f <the new remoteusers file>",quit=True)
    source = yaml_parser(remoteusers_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.RemoteUser(username=val.get('username'),auth_type=val.get('auth_type'),password=val.get('password'))
            session.add(obj)
        session.commit()

def create_users(argvs):
    '''
    create little_finger access user
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        user_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreateusers -f <the new users file>",quit=True)

    source = yaml_parser(user_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.UserProfile(username=key,password=val.get('password'))
            if val.get('groups'):
                groups = session.query(models.Group).filter(models.Group.name.in_(val.get('groups'))).all()
                if not groups:
                    print_err("none of [%s] exist in group table." % val.get('groups'),quit=True)
                obj.groups = groups
            if val.get('bind_hosts'):
                bind_hosts = common_filters.bind_hosts_filter(val)
                obj.bind_hosts = bind_hosts
            #print(obj)
            session.add(obj)
        session.commit()

def create_groups(argvs):
    '''
    create groups
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        group_file  = argvs[argvs.index("-f") + 1 ]
    else:
        print_err("invalid usage, should be:\ncreategroups -f <the new groups file>",quit=True)
    source = yaml_parser(group_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.HostGroup(name=key)
            if val.get('bind_hosts'):
                bind_hosts = common_filters.bind_hosts_filter(val)
                obj.bind_hosts = bind_hosts

            if val.get('user_profiles'):
                user_profiles = common_filters.user_profiles_filter(val)
                obj.user_profiles = user_profiles
            session.add(obj)
        session.commit()

def create_bindhosts(argvs):
    '''
    create bind hosts
    :param argvs:
    :return:
    '''
    # tip：千万不要写错表名，否则表无内容
    if '-f' in argvs:
        bindhosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new bindhosts file>",quit=True)
    source = yaml_parser(bindhosts_file)
    if source:
        for key,val in source.items():
            ## 获取一条host对象为的是后续获取host.id
            host_obj = session.query(models.Host).filter(models.Host.hostname==val.get('hostname')).first()
            assert host_obj
            for item in val['remote_users']:
                print(item )
                assert item.get('auth_type')
                ## 获取一条remoteuser对象为的是后续获取remoteuser.id
                if item.get('auth_type') == 'ssh-passwd':
                    remoteuser_obj = session.query(models.RemoteUser).filter(
                                                        models.RemoteUser.username==item.get('username'),
                                                        models.RemoteUser.password==item.get('password')
                                                    ).first()
                else:
                    remoteuser_obj = session.query(models.RemoteUser).filter(
                                                        models.RemoteUser.username==item.get('username'),
                                                        models.RemoteUser.auth_type==item.get('auth_type'),
                                                    ).first()
                if not remoteuser_obj:
                    print_err("RemoteUser obj %s does not exist." % item,quit=True )
                ## 根据上面获取的host.id 和 remoteuser.id 添加bindhost记录
                bindhost_obj = models.BindHost(host_id=host_obj.id,remoteuser_id=remoteuser_obj.id)
                session.add(bindhost_obj)
                #for groups this host binds to
                if source[key].get('groups'):
                    group_objs = session.query(models.HostGroup).filter(models.HostGroup.name.in_(source[key].get('groups') )).all()
                    assert group_objs
                    print('groups:', group_objs)
                    ## 添加一条bindhost_m2m_hostgroup记录
                    bindhost_obj.host_groups = group_objs
                #for user_profiles this host binds to
                if source[key].get('user_profiles'):
                    userprofile_objs = session.query(models.UserProfile).filter(models.UserProfile.username.in_(
                        source[key].get('user_profiles')
                    )).all()
                    assert userprofile_objs
                    print("userprofiles:",userprofile_objs)
                    ## 添加一条user_m2m_bindhost记录
                    bindhost_obj.user_profiles = userprofile_objs
                #print(bindhost_obj)
        session.commit()

def auth():
    '''
    do the user login authentication
    :return:
    '''
    count = 0
    while count < 3:
        username = input ("\033[32;1mUsername:\033[0m").strip ()
        if len (username) == 0: continue
        password = input ("\033[32;1mPassword:\033[0m").strip ()
        if len (password) == 0: continue
        user_obj = session.query (models.UserProfile).filter (models.UserProfile.username == username,
                                                              models.UserProfile.password == password).first ()
        if user_obj:
            return user_obj
        else:
            print ("wrong username or password, you have %s more chances." % (3 - count - 1))
            count += 1
    else:
        print_err ("too many attempts.")

def welcome_msg(user):
    WELCOME_MSG = '''\033[32;1m
    ------------- Welcome [%s] login LittleFinger -------------
    \033[0m''' % user.username
    print (WELCOME_MSG)

#def log_recording(user_obj, bind_host_obj, logs):
def log_recording(logs):
    '''
    flush user operations on remote host into DB
    :param logs: list format [logItem1,logItem2,...]
    :return:
    '''
    print ("\033[41;1m--logs:\033[0m", logs)

    session.add_all(logs)
    session.commit()


#user for jumpserver is ready login to host of remote
def start_session(argvs):
    print('going to start sesssion ')
    #return user_obj
    user = auth() #
    if user:
        welcome_msg(user)
        print(user.bind_hosts) # 调用的是module中的backref对应的回调
        print(user.host_groups) # 调用的是module中的backref对应的回调
        exit_flag = False
        while not exit_flag: # 进入循环
            if user.bind_hosts: # 首先判断用户是否包含有直接绑定的主机，user其实就是user_obj
                print('\033[32;1mz.\tungroupped hosts (%s)\033[0m' % len(user.bind_hosts) )
            for index,group in enumerate(user.host_groups): # 循环判断用户的绑定主机组，group就是hostgroup_obj
                print('\033[32;1m%s.\t%s (%s)\033[0m' %(index,group.name, len(group.bind_hosts)))

            # 用户选择想要连接的主机，如果输入的是"0"就跳过下面循环，继续上面循环，如果输入的是"z"就是未分组的机器，如果输入的是非0的整数就代表要选择分组的机器
            choice = input("[%s]:" % user.username).strip()
            if len(choice) == 0:continue
            if choice == 'z':
                print("------ Group: ungroupped hosts ------" )
                for index,bind_host in enumerate(user.bind_hosts):
                    print("  %s.\t%s@%s(%s)"%(index,
                                              bind_host.remote_user.username,
                                              bind_host.host.hostname,
                                              bind_host.host.ip,
                                              ))
                print("----------- END -----------" )
            elif choice.isdigit(): #这里代表选择分组中的机器，因为一个组有很多机器，所以还要再次循环获取具体的一台机器
                choice = int(choice)
                if choice < len(user.host_groups):
                    print("------ Group: %s ------"  % user.host_groups[choice].name)
                    for index,bind_host in enumerate(user.host_groups[choice].bind_hosts):
                        print("  %s.\t%s@%s(%s)"%(index,
                                                  bind_host.remote_user.username,
                                                  bind_host.host.hostname,
                                                  bind_host.host.ip,
                                                  ))
                    print("----------- END -----------" )

                    #host selection，准备登录选定的主机
                    while not exit_flag:
                        user_option = input("[(b)back, (q)quit, select host to login]:").strip()
                        if len(user_option)==0:continue
                        if user_option == 'b':break
                        if user_option == 'q':
                            exit_flag=True
                            sys.exit()
                        if user_option.isdigit():
                            user_option = int(user_option)
                            if user_option < len(user.host_groups[choice].bind_hosts) :
                                print('host:',user.host_groups[choice].bind_hosts[user_option])
                                #print('audit log:',user.host_groups[choice].bind_hosts[user_option].audit_logs)
                                ssh_login.ssh_login(user,
                                                    user.host_groups[choice].bind_hosts[user_option], #choice指定哪个组，user_option指定哪个机器，bindhost_obj
                                                    session,
                                                    log_recording # 记录日志
                                                    )
                else:
                    print("no this option..")


def display_logs(argvs):
    user = auth()
    auditlog_objs = session.query (models.AuditLog).filter(models.AuditLog.user_id == user.id).all()
    for index,obj in enumerate(auditlog_objs):
        bindhost_obj = session.query(models.BindHost).filter(models.BindHost.id == obj.bind_host_id).first()
        print(obj.user_id,bindhost_obj,obj.cmd,obj.date)