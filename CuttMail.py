#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
This module is sendmail puporse,please

"""

__author__ = "dewly_tg"

from email.header import Header
import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(_to_email,_subject,_message):
    """
    Please input three param (mail_to,subject,message)
    :param _to_email:
    :param _subject:
    :param _message:
    :return:
    """
    _from_email = 'zabbix@cutt.com'
    msg = MIMEMultipart()
    msg['From'] = _from_email
    msg['To'] = _to_email
    msg['Subject'] = Header(_subject, charset='UTF-8')
    txt = MIMEText(_message, _subtype='plain', _charset='UTF-8')
    msg.attach(txt)
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.example.com:25')
        smtp.login('zabbix@example.com', '123')
        smtp.sendmail(_from_email, _to_email, msg.as_string())
    except smtplib.SMTPException,e:
        return e.message
    else:
        return 0
    finally:
        smtp.quit()

