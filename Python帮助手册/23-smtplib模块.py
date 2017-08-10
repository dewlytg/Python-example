#coding:utf-8

import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
import sys

def send_mail(_to_email, _subject, _message):
    _from_email = 'zabbix@cutt.com'
    msg = MIMEMultipart()
    msg['From'] = _from_email
    msg['To'] = _to_email
    msg['Subject'] = Header('zabbix-监控报警', charset='UTF-8')
    txt = MIMEText(_message, _subtype='plain', _charset='UTF-8')
    msg.attach(txt)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.mxhichina.com:25')
    smtp.login ('zabbix@eample', '123456')
    smtp.sendmail(_from_email, _to_email, msg.as_string ())
    smtp.quit()

if __name__ == '__main__':
    send_mail(sys.argv[1],sys.argv[2],sys.argv[3])