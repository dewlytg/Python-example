#!/usr/bin/env python

"""
mysqldb只支持mysql数据库
sqlalchemy支持多种数据库模型
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker

#declared base class,create engine
Base = declarative_base()
engine = create_engine('mysql://root:123456@192.168.2.210/oldboydb')

class User(Base):
    __tablename__ = "user" # 表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine) #创建表结构，如果表存在就不会创建

Session_class = sessionmaker(bind=engine)
Session = Session_class()
user_obj = User(name="zhangsan",password="123456")
print(user_obj.name,user_obj.id)

Session.add(user_obj)
print(user_obj.name,user_obj.id)

Session.commit()
print(user_obj.name,user_obj.id)
