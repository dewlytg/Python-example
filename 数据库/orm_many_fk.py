#!/usr/bin/env python
#coding:utf-8

"""
多外键关联，一对多
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,DATE
from sqlalchemy.orm import sessionmaker,relationship

#declared base class,create engine
Base = declarative_base()
engine = create_engine('mysql://root:123456@192.168.2.210/oldboydb')

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer,ForeignKey("address.id"))
    shipping_address_id = Column(Integer,ForeignKey("address.id"))

    billing_address = relationship("Address",foreign_keys=[billing_address_id])
    shipping_address = relationship("Address",foreign_keys=[shipping_address_id])

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer,primary_key=True)
    street = Column(String(32))
    city = Column(String(32))
    state = Column(String(32))

    def __repr__(self):
        return self.street
#Base.metadata.create_all(engine) #创建表结构，如果表存在就不会创建