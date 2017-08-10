#coding:utf-8

###paramiko 模块使用
import paramiko

hostname = ""
username = ""
password = ""
port = 22


class SshClass ():
    """
    This Class is a SSH for paramiko
    """

    def __init__(self, hostname, username, password, port):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def ssh_command(self, execcommand):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.hostname, port=self.port, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(execcommand)
        ret = stdout.readlines()
        ssh.close()
        return ret

    def ssh_fileput(self, remote, local):
        t = paramiko.Transport((self.hostname, self.port))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        remotepath = remote
        localpath = local
        sftp.put(localpath, remotepath)
        t.close()

    def ssh_fileget(self, remote, local):
        t = paramiko.Transport((self.hostname, self.port))
        t.connect (username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        remotepath = remote
        localpath = local
        sftp.get(remotepath, localpath)
        t.close()


if __name__ == "__main__":
    s1 = SshClass(hostname, username, password, port)