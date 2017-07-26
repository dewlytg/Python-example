#!/usr/bin/env python
# -*-coding:utf8-*-

import MySQLdb
import smtplib
import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
import multiprocessing
from CuttSms import sendTemplateSMS

def mysql_select(sql, pipe):
    try:
        conn = MySQLdb.connect(host='192.168.1.1',user='root',passwd='123',db='test',port=3306,charset='utf8',connect_timeout=10)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        pipe.send('successful')    
    except Exception,e:
        pipe.send("connect error") 

def query_with_timeout(sql):
    pipe_out, pipe_in = multiprocessing.Pipe(False)
    subproc = multiprocessing.Process(target=mysql_select,args=(sql, pipe_in))
    subproc.start()
    subproc.join(timeout=3)    
    if pipe_out.poll():
        ex_c = pipe_out.recv()
        if ex_c != "successful":
            raise Exception(ex_c)   
    else:
        ex_c = "mysql not written"
        raise Exception(ex_c)
    subproc.terminate()    

def se_mail(mail_result):
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    _from_email = 'zabbix@example.com'
    _to_email = 'gang.tang@example.com'
    _subject = "db-monitor"
    msg = MIMEText("""
        <html>
            <head>
            </head>
            <body>
                <table width="800" border="1" cellspacing="0" cellpadding="4">
                    <tr>
                       <th bgcolor="#00FFFF" height="1"  colspan="4" align="center"  style="font-size:15px">中国区zabbix数据库监控</th>
                    </tr>
                         <td  width="100px"  style="font-size:15px"  nowrap>告警区域</td>
                         <td  style="font-size:15px">中国</td>
                    <tr>
                    </tr>
                         <td  width="100px"  style="font-size:15px"  nowrap>主机名称</td>
                         <td  style="font-size:15px">192.168.1.1</td>
                    <tr>
                    </tr>
                         <td  width="100px"  style="font-size:15px"  nowrap>告警项目</td>
                         <td  style="font-size:15px">zhiyue数据库监控</td>
                    <tr>
                    </tr>
                         <td  width="100px"  style="font-size:15px"  nowrap>告警级别</td>
                         <td  bgcolor=red style="font-size:15px">严重</td>
                    <tr>
                    </tr>
                         <td  width="100px"  style="font-size:15px"  nowrap>告警状态</td>
                         <td  bgcolor=red style="font-size:15px">PROBLEM</td>
                    <tr>
                    </tr>
                         <td  width="100px"  style="font-size:15px"  nowrap>详细内容</td>
                         <td  style="font-size:15px">""" + mail_result + """</td>
                    <tr>
                         <td  width="100px"  style="font-size:15px"  nowrap>发生时间</td>
                         <td  style="font-size:15px">""" + now_time + """</td>
                    </tr>
                </table>
            </body>
        </html>""","html","utf-8")
    msg['From'] = _from_email
    msg['To'] = _to_email
    msg['Subject'] = _subject
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.example.com:25')
        smtp.login('zabbix@example.com', '123')
        smtp.sendmail(_from_email, _to_email, msg.as_string())
        smtp.quit()
        print '邮件发送成功'
    except Exception,e:
        print "失败"+str(e)

if __name__ == '__main__':    
    #创建监控数据库连接，与是否可写，的监控表，下面是创建语句
    #sql_user_info = """
    #CREATE TABLE IF NOT EXISTS db_check_table (
    #itemid INT(20),
    #applicationid INT(20),
    #hostid INT(20),
    #name  VARCHAR(255),
    #du_name  VARCHAR(255),
    #item_name   VARCHAR(255)
    #)
    #"""
    insert_sql = """insert into db_check_table(content) values ('Python monitor')"""   
    try:
        query_with_timeout(insert_sql)    
    except Exception,e:
        mail_result = str(e)        
        if mail_result == "mysql not written":
            se_mail(mail_result)
            sendTemplateSMS('1888888888',['数据库','写入错误'])
        else:
            se_mail(mail_result)
            

