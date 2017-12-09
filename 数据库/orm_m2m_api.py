#!/usr/bin/env python
#coding:utf-8

import orm_m2m
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_m2m.engine)
Session = Session_class()

# b1 = orm_m2m.Book(name="learn python with Alex",pub_date="2014-05-20")
# b2 = orm_m2m.Book(name="learn Zhangbility with Alex",pub_date="2015-05-20")
# b3 = orm_m2m.Book(name="learn hook up girls with Alex",pub_date="2016-05-20")
#
# a1 = orm_m2m.Author(name="Alex")
# a2 = orm_m2m.Author(name="Jack")
# a3 = orm_m2m.Author(name="Rain")
#
# b1.authors = [a1,a3]
# b3.authors = [a1,a2,a3]
#
# Session.add_all([b1,b2,b3,a1,a2,a3])
# Session.commit()

# author_obj = Session.query(orm_m2m.Author).filter(orm_m2m.Author.name == "Alex").first()
# print(author_obj.books[1].pub_date) # 通过作者反向查询书
# book_obj = Session.query(orm_m2m.Book).filter(orm_m2m.Book.id == 2).first()
# book_obj.authors.remove(author_obj) # 书中删除一个作者
# #print(book_obj.authors)
b3 = orm_m2m.Book(name="中国字典",pub_date="2016-05-20")
Session.add(b3)
Session.commit()