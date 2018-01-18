#!/usr/bin/env python
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import ParentClass
from core import course_main
from core import teacher_main
from core import student_main

class Class(ParentClass.BaseClass):

    def associate_course(self,coursename):
        course_obj = course_main.Course(coursename)
        if self.exist() and course_obj.exist():
            self.meta[self.name]["course"] = coursename
            self.save()

    def assign_teacher(self,teachername):
        teacher_obj = teacher_main.Teacher(teachername)
        if self.exist() and teacher_obj.exist():
            self.meta[self.name]["teacher"] = teachername
            self.save()

    def enroll_student(self,studentname):
        student_obj = student_main.Student(studentname)
        if self.exist() and student_obj.exist():
            if not self.meta[self.name].get("students"):
                self.meta[self.name]["students"] = []
            if not studentname in self.meta[self.name]["students"]:
                self.meta[self.name]["students"].append(studentname)
                self.save()

    def dismiss_studnet(self,studentname):
        student_obj = student_main.Student(studentname)
        if self.exist() and student_obj.exist():
            if self.meta[self.name].get("students") and studentname in self.meta[self.name]["students"]:
                self.meta[self.name]["students"].remove(studentname)
                self.save()

if __name__ == "__main__":
    obj = Class("a")
    obj.remove()
    # obj.associate_course("Shell")
    # obj.assign_teacher("alex")
    # obj.enroll_student("s1")
    # obj.dismiss_studnet("s1")
    print(obj.meta)
