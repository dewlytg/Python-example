#!/usr/bin/env python
#coding:utf-8

"""
一对一
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,DATE
from sqlalchemy.orm import sessionmaker,relationship

#declared base class,create engine
Base = declarative_base()
engine = create_engine('mysql://root:123456@192.168.2.210/oldboydb')

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name: %s>" %(self.id ,self.name)

class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey("student.id"))
    student = relationship("Student",backref="my_study_record") # 这个关系放在内存里，可以通过student.my_study_record 来获取对应的上课记录

    def __repr__(self):
        return "<%s name: %s status: %s>" %(self.student.name ,self.day ,self.status)

Base.metadata.create_all(engine) #创建表结构，如果表存在就不会创建
Session_class = sessionmaker(bind=engine)
session = Session_class()

# 创建数据
# s1 = Student(name="Alex",register_date="2014-05-20")
# s2 = Student(name="Jack",register_date="2015-05-20")
# s3 = Student(name="Rain",register_date="2014-03-20")
# s4 = Student(name="Eric",register_date="2017-05-10")
#
# study_obj1 = StudyRecord(day=1,status="YES",stu_id=1)
# study_obj2 = StudyRecord(day=2,status="NO",stu_id=1)
# study_obj3 = StudyRecord(day=3,status="YES",stu_id=1)
# study_obj4 = StudyRecord(day=1,status="YES",stu_id=2)
#
# session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])
# session.commit()

# 先查出来student id，根据stu id 来查询对应的上课记录
stu_obj = session.query(Student).filter(Student.name=="alex").first()
print(stu_obj.my_study_record)
session.commit()
