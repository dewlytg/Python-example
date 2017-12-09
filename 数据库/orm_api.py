#!/usr/bin/env python

import orm_many_fk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_many_fk.engine)
Session = Session_class()

# addr1 = orm_many_fk.Address(street="Tiantongyuan",city="ChangPing",state="BJ")
# addr2 = orm_many_fk.Address(street="Wudaokou",city="HaiDian",state="BJ")
# addr3 = orm_many_fk.Address(street="Yanjiao",city="LangFang",state="HB")
#
# Session.add_all([addr1,addr2,addr3])
#
# c1 = orm_many_fk.Customer(name="Alex",billing_address=addr1,shipping_address=addr2)
# c2 = orm_many_fk.Customer(name="Jack",billing_address=addr3,shipping_address=addr3)
#
# Session.add_all([c1,c2])
obj = Session.query(orm_many_fk.Customer).filter(orm_many_fk.Customer.name=="alex").first()
print(obj.name,obj.billing_address,obj.shipping_address)

Session.commit()