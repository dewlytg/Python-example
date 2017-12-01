#!/usr/bin/env python
#coding:utf-8

"""
基础表：
Host：主机表
ip   hostname  port

HostGroup：主机组表
name

UserProfile：堡垒机用户表
username password

RemoteUser：远程用户表
username password authtype

关系表：
BindHost:
hostid  remoteruerid 分配一个主机的时候必须再分配一个远程用户

user_m2m_bindhost 用户分配bindhost

bindhost_m2m_hostgroup bindhost分配到组

user_m2m_hostgroup 用户直接管理组
"""

from sqlalchemy import create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,DATE,Enum,UniqueConstraint
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy_utils import ChoiceType #选择类型

##只是声明Base，后面在views中创建engine，并且执行Base.metadata.create_all(engine)，创建表
Base = declarative_base()

user_m2m_bindhost = Table("user_m2m_bindhost",Base.metadata,
                        Column("userprofile_id",Integer,ForeignKey("user_profile.id")),
                        Column("bindhost_id",Integer,ForeignKey("bind_host.id"))
                        )

bindhost_m2m_hostgroup = Table("bindhost_m2m_hostgroup",Base.metadata,
                        Column("bindhost_id",Integer,ForeignKey("bind_host.id")),
                        Column("hostgroup_id",Integer,ForeignKey("host_group.id"))
                        )

user_m2m_hostgroup = Table("user_m2m_hostgroup",Base.metadata,
                        Column("userprofile_id",Integer,ForeignKey("user_profile.id")),
                        Column("hostgroup_id",Integer,ForeignKey("host_group.id"))
                        )

class Host(Base):
    __tablename__ = "host"
    id = Column(Integer,primary_key=True)
    ip = Column(String(32),unique=True)
    hostname = Column(String(32),unique=True)
    port = Column(Integer,default=22)

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = "host_group"
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(32),unique=True)
    bind_hosts = relationship("BindHost",secondary=bindhost_m2m_hostgroup,backref="host_groups")

    def __repr__(self):
        return  self.name


class BindHost(Base):
    """
    192.168.1.10    web    bj_group
    192.168.1.20    mysql  sh_group
    """
    __tablename__ = "bind_host"
    __table_args__ = (UniqueConstraint("host_id","remoteuser_id",name="_host_remoteuser_uc"),) # 联合唯一
    id = Column (Integer, autoincrement=True, primary_key=True)
    host_id = Column(Integer,ForeignKey("host.id")) #普通的一对多外键
    remoteuser_id = Column(Integer,ForeignKey("remote_user.id")) #普通的一对多外键
    host = relationship("Host",backref="bind_hosts") #多对多外键，需要再创建第三张表来定义关系，请看上面Table声明的表
    remote_user = relationship("RemoteUser",backref="bind_hosts") #多对多外键，需要再创建第三张表来定义关系，请看上面Table声明的表

    def __repr__(self):
        return "<%s -- %s>"  %(self.host.ip,self.remote_user.username)

class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(Integer,primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(32))
    bind_hosts = relationship("BindHost",secondary=user_m2m_bindhost,backref="user_profiles") #多对多外键，需要再创建第三张表来定义关系，请看上面Table声明的表
    host_groups = relationship("HostGroup", secondary=user_m2m_hostgroup,backref="user_profiles") #多对多外键，需要再创建第三张表来定义关系，请看上面Table声明的表

    def __repr__(self):
        return self.username

class RemoteUser(Base):
    __tablename__ = "remote_user"
    __table_args__ = (UniqueConstraint("username","password","auth_type",name="_user_passwd_uc"),) # 联合唯一
    AuthTypes = [
        ("ssh-passwd","SSH/Password"), # 第一个字段是存在数据库的字段，第二个是外部显示的字段
        ("ssh-key","SSH/KEY"),
    ]
    id = Column(Integer,primary_key=True)
    username = Column(String(32))
    password = Column(String(32))
    auth_type = Column(ChoiceType(AuthTypes))

    def __repr__(self):
        return self.username

class AuditLog(Base):
    __tablename__ = "audit_log"
    id = Column (Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey("user_profile.id"))  # 普通的一对多外键
    bind_host_id = Column(Integer,ForeignKey("bind_host.id"))
    action_type = Column(String(32))
    cmd = Column(String(64))
    date = Column(String(64))

    def __repr__(self):
        return "%s %s %s" %(self.user_id,self.cmd,self.date)