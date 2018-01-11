#!/usr/bin/env python

from utils.condition import decrotor
from utils.handler import FileHandler
from utils.mysql import parsring_sql

fileobj = FileHandler("D:\PycharmProjects\Python-Study\员工信息表程序\db\staff_table")
staff_columns = fileobj.get_columns
staff_info_list = fileobj.get_info()

def staff_query(string):
    result = parsring_sql(string)
    select_result = decrotor(result,staff_info_list)
    if select_result:
        if isinstance(result["select"],str):
            if result["select"] == "*":
                print(select_result)
            else:
                for i in select_result:
                    print(i)
        else:
            for i in result["select"]:
                for line in select_result:
                    print(line[i])
    else:
        return False

def staff_add(string):
    result = parsring_sql(string)["values"]
    fileobj.save2file(result)

def staff_delete(string):
    result = parsring_sql(string)
    delete_list = decrotor(result, staff_info_list)
    for i in delete_list:staff_info_list.remove(i)
    fileobj.save2file(staff_info_list)

def staff_update(string):
    result = parsring_sql(string)
    update_list = decrotor(result,staff_info_list)
    for i in staff_info_list:
        if i in update_list:
            key,value = tuple(result["set"]["condition"].items())[0]
            i[key] = value
    fileobj.save2file(staff_info_list)

# staff_query("select * from t1 where name=alex or age>30")
# staff_add("insert into t1 values (Mack,40,13561453430,HR,2009-03-11)")
# staff_delete("delete from t1 where name=mack or age=22")
# staff_update("update  t1 set name=IT where name=Rain")



