#!/usr/bin/env python

"""
regular:
1.先算乘除，后加减，有括号先算括号内
"""
from functools import reduce
import re
_multiply_pattern = '([0-9.]+)\*([0-9.]+)'
_division_pattern = '([0-9.]+)/([0-9.]+)'
_plus_pattern = '(-?[0-9.]+)\+([0-9.]+)'
_subtraction_pattern = '(-?[0-9.]+)-([0-9.]+)'
_negative_pattern = r'-([0-9.]+)-([0-9.]+)'
_parenthesis_pattern = '\((.*)\)'
_symbol_pattern = "\d+[\+\-\*\/]\d+"

multiply = lambda x,y:float(x)*float(y)
division = lambda x,y:float(x)/float(y)
plus = lambda x,y:float(x)+float(y)
subtraction = lambda x,y:float(x)-float(y)
operator_list = [{"operator":multiply,"pattern":_multiply_pattern,"symbol":"*"},
                 {"operator":division,"pattern":_division_pattern,"symbol":"/"},
                 {"operator":subtraction,"pattern":_subtraction_pattern,"symbol":"-"},
                 {"operator":plus,"pattern":_plus_pattern,"symbol":"+"}
                 ]

def operator(string):
    while re.search(_symbol_pattern,string):
        for i in operator_list:
            if re.search(i["pattern"],string):
                iterable =re.search(i["pattern"],string).groups()
                result = reduce(i["operator"],iterable)
                string = string.replace(re.search(i["pattern"],string).group(),str(result),1)
                if i["symbol"] in string:continue
    else:
        return string

def complex_operator(string):
    temp = re.search(_parenthesis_pattern,string).groups()[0]
    result = operator(temp)
    string = string.replace(re.search(_parenthesis_pattern,string).group(),str(result),1)
    ret = operator(string)
    return ret

if __name__  == "__main__":
    ret = complex_operator("(-100-10-10*8)+100*2")
    print(ret)