#!/usr/bin/env python

from  school_main import School
from class_main import Class
from course_main import Course
from teacher_main import Teacher
from student_main import Student

def main():
    while True:
        print("""========================
            1) 创建学校
            2) 查看学校
            3) 创建班级
            4) 查看班级
            5) 创建课程
            6) 查看课程
            7) 分配课程
            8) 招聘老师
            9) 创建老师
            10) 查看老师
            11）老师分班
            12) 创建学员
            13) 查看学员
            14) 开除学员
        """)
        select_option = input("请输入你的选项,[q]退出程序".center(30,">"))
        if select_option == "1":
            school_name = input("请输入学校名称？")
            school_obj = School(school_name)
            school_obj.initialize()
        elif select_option == "2":
            school_name = input("请输入学校名称？")
            school_obj = School(school_name)
            school_obj.display()
        elif select_option == "3":
            school_name = input("请输入学校名称？")
            class_name = input("请输入班级名称？")
            school_obj = School(school_name)
            school_obj.school_add_class(class_name)
        elif select_option == "4":
            class_name = input("请输入班级名称？")
            class_obj = Class(class_name)
            class_obj.display()
        elif select_option == "5":
            course_name = input("请输入课程名称？")
            course_period = input("请输入课程周期？")
            course_price = input("请输入课程价格？")
            course_obj = Course(course_name)
            course_obj.initialize(course_period,course_price)
        elif select_option == "6":
            course_name = input ("请输入课程名称？")
            course_obj = Course (course_name)
            course_obj.display()
        elif select_option == "7":
            class_name = input("请输入班级名称？")
            course_name = input("请输入课程名称？")
            class_obj = Class(class_name)
            class_obj.associate_course(course_name)
        elif select_option == "8":
            school_name = input("请输入学校名称？")
            teacher_name = input("请输入老师名称？")
            school_obj = School(school_name)
            school_obj.school_empoly_teacher(teacher_name)
        elif select_option == "9":
            teacher_name = input("请输入老师名称？")
            teacher_obj = Teacher(teacher_name)
            teacher_obj.initialize()
        elif select_option == "10":
            teacher_name = input("请输入老师名称？")
            teacher_obj = Teacher (teacher_name)
            teacher_obj.display()
        elif select_option == "11":
            class_name = input("请输入班级名称？")
            teacher_name = input("请输入老师名称？")
            class_obj = Class(class_name)
            class_obj.assign_teacher(teacher_name)
        elif select_option == "12":
            student_name = input("请输入学员的名称？")
            student_age = input("请输入学员的年龄？")
            student_gender = input("请输入学员的性别？")
            student_money = input("请输入学员的存款？")
            student_obj = Student(student_name)
            student_obj.initialize(student_age,student_gender,student_money)
        elif select_option == "13":
            student_name = input("请输入学员的名称？")
            student_obj = Student(student_name)
            student_obj.display()
        elif select_option == "14":
            class_name = input("请输入班级名称？")
            student_name = input("请输入学员的名称？")
            class_obj = Class(class_name)
            class_obj.dismiss_studnet(student_name)
        elif select_option == "q":
            break

if __name__ == "__main__":
    main()