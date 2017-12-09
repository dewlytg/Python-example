#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import base64
import getpass
import os
import socket
import sys
import traceback
from paramiko.py3compat import input
from  modules import models
import datetime

import paramiko
try:
    import interactive
except ImportError:
    from . import interactive


def ssh_login(user_obj,bind_host_obj,mysql_engine,log_recording):
    # now, connect and use paramiko Client to negotiate SSH2 across the connection
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        print('*** Connecting...')
        #client.connect(hostname, port, username, password)
        client.connect(bind_host_obj.host.ip,
                       bind_host_obj.host.port,
                       bind_host_obj.remote_user.username,
                       bind_host_obj.remote_user.password,
                       timeout=30)

        # 记录cmd日志，不要操作一条记录一条，这样慢
        cmd_logs = []
        chan = client.invoke_shell()
        print(repr(client.get_transport()))
        print('*** Here we go!\n')
        # 列表中追加一条auditlog_obj
        cmd_logs.append(models.AuditLog(user_id=user_obj.id,
                                          bind_host_id=bind_host_obj.id,
                                          action_type='login',
                                          date=datetime.datetime.now()
                                          ))
        #log_recording(user_obj,bind_host_obj,cmd_caches) # 记录一条login日志
        log_recording(cmd_logs)
        interactive.interactive_shell(chan,user_obj,bind_host_obj,cmd_logs,log_recording)
        chan.close()
        client.close()

    except Exception as e:
        print('*** Caught exception: %s: %s' % (e.__class__, e))
        traceback.print_exc()
        try:
            client.close()
        except:
            pass
        sys.exit(1)