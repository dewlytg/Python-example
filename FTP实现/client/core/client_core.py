#!/usr/bin/env python

import os,sys,json,socket,hashlib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from cfg import config

USER_HOME_DIR = config.USER_HOME_DIR
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((config.HOST,config.PORT))
print(config.help_list)

while True:
    username = input("请输入你的用户名？").strip()
    password = input("请输入你的密码？").strip()
    if not username or not password:continue
    user_info_dic = {"username":username,"password":password}
    client.send(json.dumps(user_info_dic).encode())
    received_user_status = client.recv(1024).decode()
    user_status = json.loads(received_user_status)
    if user_status["code"] == "200":
        print(user_status["msg"])
        while True:
            user_input = input("请输入>>>>")
            cmd = user_input.split()[0]
            client.send(user_input.encode())
            current_dir = client.recv(1024).decode()
            client.send(current_dir)
            if cmd not in config.help_list:
                print("你输入的命令不支持")
            else:
                if cmd == "dir":
                    received_total_size = client.recv(1024).decode()
                    client.send(b"ready to recived")
                    res_size = 0
                    res_data = b""
                    while res_size != int(received_total_size):
                        data = client.recv(1024)
                        res_size += len(data)
                        res_data += data
                    else:
                        print("已经接受完成")
                        print(res_data)
                elif cmd == "get":
                    filename = user_input.split()[1]
                    file_size = int(client.recv(1024).decode())
                    client.send(b"ready download file")
                    user_home_dir = os.path.join(USER_HOME_DIR,username)
                    if not os.path.isdir(user_home_dir):os.makedirs(user_home_dir)
                    f = open(os.path.join(user_home_dir,filename),"wb")
                    m = hashlib.md5()
                    res_size = 0
                    while res_size != file_size:
                        if file_size - res_size > 1024:
                            size = 1024
                        else:
                            size = file_size - res_size
                        data = client.recv(size)
                        f.write(data)
                        m.update(data)
                    else:
                        print("文件已经下载完成")
                        f.close()
                    res_size += size
                    file_md5 = client.recv(1025)
                    new_file_md5 = m.hexdigest()
                    print(file_md5,new_file_md5)
                elif cmd == "pwd":
                    user_home_dir = client.recv(1024).decode()
                    print(user_home_dir)
                elif cmd == "cd":
                    sub_dir = user_input.split()[1]
                    client.send(sub_dir.encode())
    else:
        print(user_status["msg"])
        break
client.close()