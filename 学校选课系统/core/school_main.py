#!/usr/bin/env python

import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import ParentClass
from core import teacher_main
from core import class_main

class School(ParentClass.BaseClass):
    def school_add_class(self,classname):
        class_obj = class_main.Class(classname)
        class_obj.initialize()
        if self.exist():
            if not self.meta[self.name].get("class"):
                self.meta[self.name]["class"] = []
                self.meta[self.name]["class"] = [classname]
                self.save()
            else:
                if classname in self.meta[self.name]["class"]:
                    pass
                else:
                    self.meta[self.name]["class"].append(classname)
                    self.save()

    def school_remove_class(self,classname):
        class_obj = class_main.Class(classname)
        if self.exist() and class_obj.exist():
            if self.meta[self.name].get("class"):
                if classname in self.meta[self.name]["class"]:
                    self.meta[self.name]["class"].remove(classname)
                    self.save()
                    class_obj.remove()

    def school_empoly_teacher(self,teachername):
        teacher_obj = teacher_main.Teacher(teachername)
        if self.exist() and teacher_obj.exist():
            if not self.meta[self.name].get("teachers"):
                self.meta[self.name]["teachers"] = []
                self.meta[self.name]["teachers"] = [teachername]
                self.save()
            else:
                if teachername in self.meta[self.name]["teachers"]:
                    pass
                else:
                    self.meta[self.name]["teachers"].append(teachername)
                    self.save()

if __name__ == "__main__":
    obj = School("北京")
    obj.initialize()
    obj.school_add_class("B1003")
    obj.school_remove_class("B1002")
    # obj.remove()
    # obj.school_empoly_teacher("eraic")
    print(obj.meta)
    # obj.create()
    # School("all").display()

