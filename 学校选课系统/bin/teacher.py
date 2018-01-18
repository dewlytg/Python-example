#!/usr/bin/env python

import os,sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import student_main
from core import class_main
from core import course_main

def show_class(teachername):
    class_obj = class_main.Class("all")
    for k,v in class_obj.meta.items():
        if v["teacher"] == teachername:
            print(k,v)

def show_student(studentname):
    student_obj = student_main.Student(studentname)
    student_obj.display()

if __name__ == "__main__":
    show_class("alex")
    show_student("s2")