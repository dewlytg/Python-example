#coding:utf-8

#one
import script1

#two
from imp import reload
reload(script1)

#three
exec(open("script1.py").read())