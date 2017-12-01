#!/usr/bin/env python
#coding:utf-8

"""
多对多
"""

from sqlalchemy import create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,DATE
from sqlalchemy.orm import sessionmaker,relationship

#declared base class,create engine
Base = declarative_base()
engine = create_engine('mysql://root:123456@192.168.2.210/oldboydb?charset=utf8')

book_m2m_author = Table("book_m2m_author",Base.metadata,
                        Column("book_id",Integer,ForeignKey("books.id")),
                        Column("author_id",Integer,ForeignKey("authors.id"))
                        )

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship("Author",secondary=book_m2m_author,backref="books")

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine) #创建表结构，如果表存在就不会创建