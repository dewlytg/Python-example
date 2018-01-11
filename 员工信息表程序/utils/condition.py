#!/usr/bin/env python

class DicSet(object):
    def __init__(self,dictobj):
        self.data = dictobj

    def match(self,dictobj):
        key,value = list(dictobj["condition"].items())[0]
        operator = dictobj["operator"]
        if operator == "=":
            if self.data.get(key) and str(self.data[key]) == value:
                return True
            return False
        elif operator == ">":
            if self.data.get (key) and int(self.data[key]) > int(value):
                return True
            return False
        elif operator == "<":
            if self.data.get (key) and int(self.data[key]) < int(value):
                return True
            return False

    def andOperator(self,lobj,robj):
        left_return = self.match(lobj)
        right_return = self.match(robj)
        if left_return and right_return:
            return True
        return False

    def orOperator(self,lobj,robj):
        left_return = self.match(lobj)
        right_return = self.match(robj)
        if left_return or right_return:
            return True
        return False

def decrotor(dictobj,listobj,result=[]):
    for i in listobj:
        staff_obj = DicSet(i)
        if dictobj.get("and") and staff_obj.andOperator(dictobj["where"], dictobj["and"]):
            result.append(i)
        elif dictobj.get("or") and staff_obj.orOperator(dictobj["where"], dictobj["or"]):
            result.append(i)
        elif staff_obj.match(dictobj["where"]) and not dictobj.get("and") and not dictobj.get("or"):
            result.append(i)
    return result