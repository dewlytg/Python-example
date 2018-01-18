#!/usr/bin/env python

import os,sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import student_main
from core import class_main
from core import course_main

msg = """
1).注册
2).查看
3).进班
4).缴费
"""

def register(studentname):
    print("欢迎来到学员管理系统，请注册".center(50,"-"))
    password = input("请输入密码？")
    student_obj = student_main.Student(studentname)
    if student_obj.exist():
        print("你注册的用户已经存在")
    else:
        age = input("请输入你的年龄？")
        gender = input("请输入你的性别？")
        money = input("请输入你的存款？")
        student_obj.initialize()
        student_obj.add_info(age=age,gender=gender,money=money,password=password)
    print(student_obj.meta)

def show_info(studentname):
    student_obj = student_main.Student(studentname)
    if student_obj.exist():
        student_obj.display()

def choice_class(studentname):

    class_obj = class_main.Class("all")
    class_obj.display()
    choice_class_name = input("请输入你想进入的班级")
    choice_class_obj = class_main.Class(choice_class_name)
    if choice_class_obj.exist():
        coursename = choice_class_obj.meta[choice_class_name]["course"]
        course_obj = course_main.Course(coursename)
        tuition = course_obj.meta[coursename]["price"]
        choice_class_obj.enroll_student(studentname)
        student_obj = student_main.Student(studentname)
        student_obj.add_info(tuition=tuition)
        print("请及时缴费【%s】" % tuition)
    choice_class_obj.display()
    student_obj.display()

def pay_tution(studentname):
    student_obj = student_main.Student(studentname)
    if student_obj.meta[studentname].get("tuition"):
        money = student_obj.meta[studentname]["money"]
        tuition = student_obj.meta[studentname]["tuition"]
        if int(money) > int(tuition):
            money = int(money) - int(tuition)
            student_obj.meta[studentname]["money"] = money
            del student_obj.meta[studentname]["tuition"]
            student_obj.save()
        else:
            print("你的钱不够！")
    else:
        print("你没有未交的学费")

if __name__ == "__main__":

    while True:
        print(msg)
        select_option = input("请选择，[q]退出".center(30,"*"))
        studentname = input("请输入你的账号？")
        if select_option == "1":
            register(studentname)
        elif select_option == "2":
            show_info(studentname)
        elif select_option == "3":
            choice_class(studentname)
        elif select_option == "4":
            pay_tution(studentname)
        elif select_option == "q":
            break
        else:
            pass