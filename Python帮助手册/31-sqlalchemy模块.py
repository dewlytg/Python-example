#coding:utf-8

"""
mysqldb只支持mysql数据库
sqlalchemy支持多种数据库模型
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session,relationship,relationships
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy import func
from sqlalchemy import and_,or_
from datetime import datetime
from sqlalchemy.orm.interfaces import MapperExtension

#declared base class,create engine
Base = declarative_base()
engine = create_engine('mysql://pycharm:pycharm@192.168.2.59/student')

#create session
Session = sessionmaker(bind=engine)
session = Session()

#create table
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "User(id={0},name={1})".format(self.id,self.name)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True,autoincrement=True)
    userid = Column(Integer)
    email = Column(String(50))

Base.metadata.create_all(bind=engine)

#write a line for single table
user = User()
user.name = "sqlalchemy"
session.add(user)
session.commit()

#write mulitple line for single table
session.add_all([User(name='abc'),User(name='123')])
session.commit()

#write a line for multiple table
user = User()
user.name = "addall"
address = Address()
address.userid = 1
address.email = "admin@pycharm.com"
session.add_all([user,address])
session.commit()

#modify
user = session.query(User).get(1)
user.name = "abcabc"
session.add(user)
session.commit()

#delete
session.query(User).filter(User.name == "aaaa").delete()
user = session.query(User).get(4)
session.delete(user)
session.commit()

#query
lstUser = session.query(User).all()
print lstUser
lstUser = session.query(User.name).all()
print lstUser

#query for pager
lstUser = session.query(User).limit(2).offset(0).all()
print lstUser
lstUser = session.query(User).all()[0:2]
print lstUser

#query counts
print session.query(User.id).count()
print session.query(func.count('*')).select_from(User).scalar()
print session.query(func.count(User.id)).scalar()

#equal not equal
lstUser = session.query(User).filter(User.name == 'aaaa').all()
print lstUser
lstUser = session.query(User).filter(User.name != 'aaaa').all()
print lstUser

#like
lstUser = session.query(User).filter(User.name.like('%a%')).all()
print lstUser

#in not in
lstUser = session.query(User).filter(User.name.in_(['aaaa','abc'])).all()
print lstUser
lstUser = session.query(User).filter(~User.name.in_(['aaaa','abc'])).all()
print lstUser

#and
lstUser = session.query(User).filter(User.name == 'aaaa',User.id == 5).all()
print lstUser
lstUser = session.query(User).filter(and_(User.name == 'aaaa',User.id == 5)).all()
print lstUser
lstUser = session.query(User).filter(User.name == 'aaaa').filter(User.id == 5).all()
print lstUser

#or
lstUser = session.query(User).filter(or_(User.name == 'aaaa',User.name == 'abc')).all()
print lstUser

#null,not null
lstUser = session.query(User).filter(User.name == None).all()
print lstUser
lstUser = session.query(User).filter(User.name != None).all()
print lstUser

#dataset
lstUser = session.query(User).all()
print lstUser
lstUser = session.query(User).first()
print lstUser
lstUser = session.query(User).filter(User.id == 1).one()
print lstUser
lstUser = session.query(User.id).filter(User.id == 1).scalar()
print lstUser

#ForeignKey
class Stu(Base):
    __tablename__ = 'stu'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    book = relationship("Book",order_by="Book.id",backref="stu")

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer,primary_key=True)
    bookname = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('stu.id'))

Base.metadata.create_all(bind=engine)
jack = Stu(name='jack')
print jack.id
print jack.name
jack.book = [Book(bookname='JavaScript'),Book(bookname='Python')]
print jack.book
session.add(jack)
session.commit()

#Extension
class DataupdateExtension(MapperExtension):
    def before_update(self,mapper,connection,instance):
        if hasattr(instance,"UpdateTime"):
            instance.UpdateTime = datetime.now()

    def before_insert(self,mapper,connection,instance):
        if hasattr(instance,"CreateTime"):
            instance.CreateTime = datetime.now()
        if hasattr(instance,"UpdateTime"):
            instance.UpdateTime = instance.CreateTime

class EmailAddress(Base):
    __tablename__ = "emailaddress"
    __mapper_args__ = {"extension":DataupdateExtension()}
    id =  Column(Integer,primary_key=True)
    email_address = Column('email',String(50),nullable=False)
    UpdateTime = Column(DateTime)
    CreateTime = Column(DateTime)

Base.metadata.create_all(bind=engine)
address = EmailAddress()
address.email_address = "c@a.com"
session.add(address)
session.commit()
