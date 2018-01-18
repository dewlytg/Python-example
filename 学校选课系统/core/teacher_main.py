#!/usr/bin/env python

import os,pickle,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import ParentClass

class Teacher(ParentClass.BaseClass):
    pass

if __name__ == "__main__":
    obj = Teacher("mack")
    obj.remove()
    # obj.initialize()
    print(obj.meta)