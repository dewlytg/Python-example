#!/usr/bin/env python
#coding:utf-8
import os,sys,json,socket,hashlib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from cfg import config

USER_HOME_DIR = config.USER_HOME_DIR
USER_ACCOUNT_DIR = config.USER_ACCOUNT_DIR
server = socket.socket()
server.bind((config.HOST,config.PORT))
server.listen(5)

while True:
    print("new addr:")
    conn,addr = server.accept()
    while True:
        received_user_info_str = conn.recv(1024)
        if len(received_user_info_str) == 0:
            break
        received_user_info_dic = json.loads(received_user_info_str.decode())
        user_status = {"code":"200","status":"success","msg":"验证成功"}
        user_account_file = os.path.join(USER_ACCOUNT_DIR,received_user_info_dic["username"])
        if os.path.isfile(user_account_file):
            user_home_dir = os.path.join(USER_HOME_DIR,received_user_info_dic["username"])
            user_info_dic = json.load(open(user_account_file))
            if user_info_dic["password"] == received_user_info_dic["password"]:
                pass
            else:
                user_status = {"code":"300","status":"failed","msg":"密码错误"}
        else:
            user_status = {"code": "201", "status": "failed", "msg": "用户不存在"}
        conn.send(json.dumps(user_status).encode())
        while True:
            received_cmd = conn.recv(1024).decode()
            conn.send(user_home_dir.encode())
            current_dir = conn.recv(1024).decode()
            if received_cmd.startswith("dir"):
                cmd_res = os.popen("ls -lh %s" % user_home_dir).read()
                if len(cmd_res) == 0:
                    cmd_res = "cmd has not output"
                conn.send(str(len(cmd_res)).encode())
                received_ack = conn.recv(1024)
                conn.send(cmd_res.encode())
            elif received_cmd.startswith("get"):
                received_cmd = conn.recv(1024).decode()
                filename = received_cmd.split()[1]
                client_down_file = os.path.join(user_home_dir,filename)
                file_size = os.stat(client_down_file).st_size
                conn.send(str(file_size).encode())
                conn.recv(1024)
                if os.path.isfile(client_down_file):
                    f = open(client_down_file,"rb")
                    m = hashlib.md5()
                    for line in f:
                        conn.send(line)
                        m.update(line)
                    else:
                        print("client down file md5",m.hexdigest())
                        f.close()
                    conn.send(str(m.hexdigest()).encode())
            elif received_cmd.startswith("pwd"):
                conn.send(user_home_dir.encode())
            elif received_cmd.startswith("cd"):
                change_dir = received_cmd.split()[1]
                current_dir

server.close()



