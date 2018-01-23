#!/usr/bin/env python
#coding:utf-8
import os,sys,json,socket,hashlib,shutil,socketserver
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from cfg import config

USER_HOME_DIR = config.USER_HOME_DIR
USER_ACCOUNT_DIR = config.USER_ACCOUNT_DIR

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("go connection from",self.client_address)
        conn = self.request
        ret = {"code": "", "msg": ""}
        flag = True
        while flag:
            print("123")
            client_user_info = json.loads(conn.recv(1024).decode())
            client_username = client_user_info["username"]
            client_password = client_user_info["password"]
            user_account_file = os.path.join(USER_ACCOUNT_DIR, client_username)
            user_home_dir = os.path.join(USER_HOME_DIR, client_username)
            if not os.path.isdir(user_home_dir): os.makedirs(user_home_dir)
            if os.path.isfile(user_account_file):
                server_user_info = json.load(open(user_account_file))
                if client_password == server_user_info["password"]:
                    ret["code"] = "200"
                    ret["msg"] = "login success"
                    conn.send(json.dumps(ret).encode())
                    current_user_dir = user_home_dir
                    while flag:
                        client_user_input = conn.recv(1024).decode()
                        if not client_user_input:break
                        client_user_command = client_user_input.split()[0]
                        if client_user_command.startswith("dir"):
                            cmd_res = os.popen("ls -lh %s" % current_user_dir).read()
                            if len(cmd_res) == 0:
                                cmd_res = "has not output"
                            conn.send(str(len(cmd_res)).encode())
                            conn.recv(1024)
                            conn.send(cmd_res.encode())
                        elif client_user_command.startswith("get"):
                            client_filename = client_user_input.split()[1]
                            file_path = os.path.join(user_home_dir,client_filename)
                            if os.path.isfile(file_path):
                                ret["code"] = "300"
                                ret["msg"] = "File exist"
                                conn.send(json.dumps(ret).encode())
                                conn.recv(1024)
                                file_size = os.stat(file_path).st_size
                                conn.send(str(file_size).encode())
                                conn.recv(1024)
                                f = open(file_path,"rb")
                                m = hashlib.md5()
                                for line in f:
                                    conn.send(line)
                                    m.update(line)
                                f.close()
                                conn.send(m.hexdigest().encode())
                            else:
                                ret["code"] = "301"
                                ret["msg"] = "File not exist"
                                conn.send(json.dumps(ret).encode())
                                conn.recv(1024)
                        elif client_user_command.startswith("put"):
                            client_filename = client_user_input.split()[1]
                            client_file_path = os.path.join(current_user_dir,client_filename)
                            conn.send(b"ready to received data")
                            client_file_size = int(conn.recv(1024).decode())
                            f = open(client_file_path,"wb")
                            m = hashlib.md5()
                            received_size = 0
                            while received_size != client_file_size:
                                if client_file_size - received_size > 1024:
                                    size = 1024
                                else:
                                    size = client_file_size - received_size
                                data = conn.recv(size)
                                f.write(data)
                                m.update(data)
                                received_size += len(data)
                            else:
                                print("put has done")
                                f.close()
                                new_file_md5 = m.hexdigest()
                            file_md5 = conn.recv(1024).decode()
                            print("server file md5 is:",new_file_md5)
                            print("client file md5 is:",file_md5)
                        elif client_user_command.startswith("cd"):
                            client_des_dir = client_user_input.split()[1]
                            if client_des_dir == "..":
                                if current_user_dir == user_home_dir:
                                    client_des_path = current_user_dir
                                else:
                                    client_des_path = os.path.dirname(current_user_dir)
                            else:
                                client_des_path = os.path.join(current_user_dir,client_des_dir)
                            if os.path.isdir(client_des_path):
                                conn.send(client_des_path.encode())
                                current_user_dir = client_des_path
                        elif client_user_command.startswith("pwd"):
                            conn.send(current_user_dir.encode())
                        elif client_user_command.startswith("mkdir"):
                            client_mk_dir = client_user_input.split()[1]
                            client_mk_path = os.path.join(current_user_dir,client_mk_dir)
                            os.makedirs(client_mk_path)
                            conn.send(str("%s dir has make" % client_mk_dir).encode())
                        elif client_user_command.startswith("rm"):
                            client_rm_dir = client_user_input.split()[1]
                            client_rm_path = os.path.join(current_user_dir,client_rm_dir)
                            if os.path.isdir(client_rm_path):
                                shutil.rmtree(client_rm_path)
                                temp = b"Directory has removed"
                            elif os.path.isfile(client_rm_path):
                                os.remove(client_rm_path)
                                temp = b"File has removed"
                            elif os.path.exists(client_rm_path):
                                temp = b"File or directory is not exist"
                            conn.send(temp)
                        elif client_user_command.startswith("quit"):
                            flag = False
                else:
                    ret["code"] = "207"
                    ret["msg"] = "password wrong"
                    conn.send(json.dumps(ret).encode())
            else:
                print("对不起你输入的账号【%s】不存在" % client_username)
                ret["code"] = "205"
                ret["msg"] = "user is not exist"
                conn.send(json.dumps(ret).encode())

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer((config.HOST,config.PORT),MyServer)
    server.serve_forever()