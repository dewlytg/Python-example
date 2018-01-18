#!/usr/bin/env python

import os,pickle,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

class BaseClass(object):

    def __init__(self,name):
        self.name = name
        self.pick_file = os.path.join(BASE_DIR,"db/%s.pickle" % self.__class__.__name__)
        self.meta = pickle.load(open(self.pick_file, "rb")) if os.path.exists(self.pick_file) else{}

    def display(self,*args,**kwargs):
        if self.name == "all":
            for k, v in self.meta.items():
                print(k, v)
        else:
            if self.name in self.meta:
                print(self.meta[self.name])

    def initialize(self,*args,**kwargs):
        if self.name not in self.meta:
            self.meta[self.name] = {}
            with open(self.pick_file, "wb") as f:
                pickle.dump(self.meta, f, pickle.HIGHEST_PROTOCOL)
        else:
            print("已经存在")

    def remove(self,*args,**kwargs):
        if self.name in self.meta:
            del self.meta[self.name]
            with open(self.pick_file, "wb") as f:
                pickle.dump(self.meta, f, pickle.HIGHEST_PROTOCOL)
        else:
            print("不存在的记录")

    def save(self,*args,**kwargs):
        with open(self.pick_file, "wb") as f:
            pickle.dump(self.meta, f, pickle.HIGHEST_PROTOCOL)

    def exist(self):
        if self.name in self.meta:
            return True
        else:
            return False