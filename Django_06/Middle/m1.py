#!/usr/bin/env python

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
class Row1(MiddlewareMixin):
    def process_request(self,request):
        print("请求进站一")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("views01")

    def process_response(self,request,response):
        print("请求返回三")
        return response

class Row2(MiddlewareMixin):
    def process_request(self, request):
        print("请求进站二")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("views02")

    def process_response(self, request, response):
        print("请求返回二")
        return response

class Row3(MiddlewareMixin):
    def process_request(self, request):
        print("请求进站三")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("views03")

    def process_response(self, request, response):
        print("请求返回一")
        return response

    def process_exception(self,request,exception):
        if isinstance(exception,ValueError):
            return HttpResponse("值错误")

    def process_template_response(self,request,response):
        # 如果view中的函数放回的对象中具有render方法就会执行
        print("--------------------------")
        return response