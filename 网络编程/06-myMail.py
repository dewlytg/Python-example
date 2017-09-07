#!/usr/bin/env python
#coding:utf-8

"""
POP3 对象的常用方法
方法                            描述
user(login)                     发送用户名 login 到服务器，并等候服务器的正在等待用户密码的返回信息
pass_(passwd)                   发送密码 passwd（在使用 user()登录之后使用）。如果登录失败，引发一个异常
stat()                          返回邮件的状态，一个长度为 2 的元组（msg_ct, mbox_siz）：消息的数量和消息的总大小也即字节数
list([msgnum])                  stat()的扩展，从服务器返回长度为 3 的元组的消息列表（rsp, msg_list,rsp_siz）：服务器的返回信息，消息的列表，返回信息的大小。如果给了 msgnum 的话，只返回指定消息的数据。
retr(msgnum)                    从服务器中得到消息 msgnum，并设置其“已读”标志。返回一个长度为3 的元组（rsp, msglines, msgsiz）：服务器的返回信息，消息 msgnum的所有行，消息的字节数
dele(msgnum)                    把消息 msgnum 标记为删除，大多数服务器在调用 quit()后执行删除操作。
quit()                          登出，保存修改（如，执行“已读”和“删除”标记等），解锁邮箱，结束连接，然后退出在登录时,user()方法不仅向服务器发送了用户名，也要等待服务器正在等待用户密码的返回信息。如果                                       pass_()方法认证失败，会引发一个 poplib.error_proto 的异常。如果成功，会得到一个以'+'号开头的返回信息，如“+OK ready”，然后服务器上的该邮箱就被锁定了，直到调用了 quit()方法为止。
"""

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = "smtp.python.is.cool"
POP3SVR = "pop.python.is.cool"

origHdrs = ["from:wesley@python.is.cool",
            "to:wesley@python.is.cool",
            "Subject:test msg"]
origBody = ["xxx","yyy","zzz"]
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])

sendSrv = SMTP(SMTPSVR)
errs = sendSrv.sendmail("wesley@python.is.cool",("wesley@python.is.cool",),origMsg)
sendSrv.quit()
assert len(errs) == 0,errs
sleep(10)


recvSvr = POP3(POP3SVR)
recvSvr.user("wesley")
recvSvr.pass_("you11NeverGuess")
rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])

sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody
