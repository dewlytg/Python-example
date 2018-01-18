#!/usr/bin/env python

import pickle
import os,pickle,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import ParentClass

class Student(ParentClass.BaseClass):

    def add_info(self,**kwargs):
        if self.exist():
            for k,v in kwargs.items():
                self.meta[self.name][k] = v
                self.save()

if __name__ == "__main__":
    obj = Student("s9")
    # obj.remove()
    obj.initialize()
    obj.add_info(age=22,gender="female")
    print(obj.meta)