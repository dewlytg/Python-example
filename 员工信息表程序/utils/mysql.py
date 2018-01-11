#!/usr/bin/env python

import re

_select_pattern = r"\w+(?P<symbol>\W+)\w+"
_insert_pattern = r'\(.+,.+,.+,.+,.+\)'
_condition_pattern = r"(?P<key>\w+)(?P<symbol>\W+)(?P<value>\w+)"
_select_list = ["select", "from", "where", "and", "or", "like", "order by", "group by", "desc"]
_insert_list = ["insert into","values"]
_delete_list = ["delete from","where","and","or"]
_update_list = ["update","set","where","and","or"]
operator_dict = {"select":_select_list,"insert into":_insert_list,"update":_update_list,"delete":_delete_list}

def regular(string,start,result={}):
    for i in operator_dict[start]:
        if i in string:
            ret = string.split(i)[1].strip()
            variable = ret.split(" ")[0]
            if re.match(_condition_pattern, variable):
                key = re.search(_condition_pattern, variable).groupdict()["key"]
                separator = re.search(_condition_pattern, variable).groupdict()["symbol"]
                value = re.search(_condition_pattern, variable).groupdict()["value"]
                result[i] = {"condition": {key: value}, "operator": separator}
            elif i == "values" and re.match(_insert_pattern,variable):
                result[i] = variable.strip("()")
            elif i == "select":
                if re.match(_select_pattern,variable):
                    separator = re.search (_condition_pattern, variable).groupdict()["symbol"]
                    result["select"] = variable.split(separator)
                else:
                    result["select"] = variable
    return result

def parsring_sql(string):
    for k,v in operator_dict.items():
        if string.startswith(k):
            result = regular(string,k)
            return result

if __name__ == "__main__":
    # parsring_sql("update t1 set name=tg where name=alex")
    parsring_sql("select * from t1 where name=tg")
    # parsring_sql("insert into t1 values (zs,40,13561453430,HR,2009-03-11)")