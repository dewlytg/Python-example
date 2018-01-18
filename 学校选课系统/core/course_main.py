#!/usr/bin/env python

import pickle
import os,pickle,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import ParentClass

class Course(ParentClass.BaseClass):

    def initialize(self,period,price):
        if self.name not in self.meta:
            self.meta[self.name] = {}
            self.meta[self.name]["period"] = period
            self.meta[self.name]["price"] = price
            with open(self.pick_file, "wb") as f:
                pickle.dump(self.meta, f, pickle.HIGHEST_PROTOCOL)
        else:
            print("已经存在")

if __name__ == "__main__":
    obj = Course("Shell")
    obj.initialize("6 months","10000")
    print(obj.meta)