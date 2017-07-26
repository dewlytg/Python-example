#! /usr/bin/env python
# coding=utf-8
"""
1. 这是一段使用APNSWrapper[https://code.google.com/p/apns-python-wrapper/]实现的发送Apple Push的代码，
其中的deviceToken需要替换为自己设备的deviceToken，pem_cert也需要替换为自己应用的P12证书；
2. 具体的获取设备的deviceToken的方法和导出P12证书的方法，
请参考这篇文章[http://www.cnblogs.com/sunnyxx/archive/2012/12/01/2796461.html]
3. 注意python版本必须为Python2.7.10
4. 要用苹果开发者账号登陆，开发这账号99美元一个，不然没有Certificates, Identifiers & Profiles
"""
__author__ = 'dewly_tg'

from APNSWrapper import *
import binascii

# 请替换为自己的设备的deviceToken,每个iphone设备中的app都会产生一个对应的token
deviceToken = binascii.unhexlify("385d62368246f06d287ac6c1deed974adc65b249559f4c3d8413cb42e4944556")

#创建通知对象
notification = APNSNotification()
notification.token(deviceToken)
notification.alert("土豪，我们做朋友吧")
notification.badge(5)
notification.sound()

#创建发送通知的这个wrapper
##push_cert.pem是通过合并得来，请参考上面文章cat public.pem private.pem > push_cert.pem
pem_cert_name = "push_cert.pem"  # 需要使用自己应用的P12证书
wrapper = APNSNotificationWrapper(pem_cert_name, False)
wrapper.append(notification)
wrapper.notify()