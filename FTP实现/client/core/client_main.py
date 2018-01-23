#!/usr/bin/env python
#coding:utf-8
import os,sys,json,socket,hashlib,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from cfg import config
from Progress import ProgressBar

USER_HOME_DIR = config.USER_HOME_DIR
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((config.HOST,config.PORT))
print(config.help_list)

while True:
    print("欢迎登录FTP系统".center(50,"-"))
    username = input("请输入用户名>>>")
    password = input("请输入密码>>>")
    if not username or not password:continue
    user_info = json.dumps({"username":username,"password":password})
    client.send(user_info.encode())
    server_ret = json.loads(client.recv(1024).decode())
    if server_ret["code"] == "200":
        print(server_ret["msg"])
        while True:
            user_input = input(">>>").strip()
            if not user_input:continue
            user_command = user_input.split()[0]
            client.send(user_input.encode())
            if user_command in config.help_list:
                if user_command.startswith("dir"):
                    server_response_size = int(client.recv(1024).decode())
                    client.send(b"ready recv data")
                    received_size = 0
                    received_data = b""
                    while received_size != server_response_size:
                        data = client.recv(1024)
                        received_data += data
                        received_size += len(data)
                    print(received_data.decode())
                elif user_command.startswith("get"):
                    server_ret = json.loads(client.recv(1024).decode())
                    if server_ret["code"] == "300":
                        client.send(server_ret["msg"].upper().encode())
                        filename = user_input.split()[1]
                        server_file_size = int(client.recv(1024).decode())
                        received_size = 0
                        f = open(os.path.join(USER_HOME_DIR,username,filename),"wb")
                        m = hashlib.md5()
                        client.send(b"ready recv data")
                        bar = ProgressBar(total=100)
                        while received_size != server_file_size:
                            if server_file_size - received_size > 1024:
                                size = 1024
                            else:
                                size = server_file_size - received_size
                            data = client.recv(size)
                            f.write(data)
                            m.update(data)
                            received_size += len(data)
                            percent = int(received_size*100/server_file_size)
                            bar.log("The file is download percent is:%s" %received_size,percent)
                            time.sleep(0.1)
                        else:
                            print("file has received done")
                            new_file_md5 = m.hexdigest()
                            f.close()
                        server_file_md5 = client.recv(1024)
                        print("server file md5:",server_file_md5)
                        print("client file md5:",new_file_md5)
                    elif server_ret["code"] == "301":
                        client.send(server_ret["msg"].upper().encode())
                        print(server_ret["msg"])
                elif user_command.startswith("put"):
                    local_current_dir = os.getcwd()
                    filename = user_input.split()[1]
                    local_file_path = os.path.join(local_current_dir,filename)
                    if os.path.isfile(local_file_path):
                        client.recv(1024)
                        file_size = os.stat(local_file_path).st_size
                        client.send(str(file_size).encode())
                        f = open(local_file_path,"rb")
                        m = hashlib.md5()
                        for line in f:
                            m.update(line)
                            client.send(line)
                        f.close()
                        client.send(str(m.hexdigest()).encode())
                elif user_command.startswith("cd"):
                    server_des_path = client.recv(1024).decode()
                    print(server_des_path)
                elif user_command.startswith("pwd"):
                    received_data = client.recv(1024).decode()
                    print(received_data)
                elif user_command.startswith("mkdir"):
                    received_data = client.recv(1024).decode()
                    print(received_data)
                elif user_command.startswith("rm"):
                    received_data = client.recv(1024).decode()
                    print(received_data)
                elif user_command.startswith("quit"):
                    client.send(b"quit")
                    sys.exit()
            else:
                print("你的操作不支持")
    else:
        print(server_ret["msg"])
client.close()