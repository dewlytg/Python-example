#!/usr/bin/env python
#-*-coding:utf-8-*-

import random

print(random.random())
print(random.randint(1,3))
print(random.randrange(10))
print(random.choice("abcdef"))
print(random.sample("hello",2))
print(random.uniform(1,10))
l = [1,2,3,4,5,6]
print(random.shuffle(l))
print(l)