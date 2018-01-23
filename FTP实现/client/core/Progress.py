#!/usr/bin/env python

import sys,time

class ProgressBar:
    def __init__(self,count=0,total=0,width=100):
        self.count = count
        self.total = total
        self.width = width

    def log(self,s,count):
        sys.stdout.write(" " * (self.width + 9) + "\r")
        sys.stdout.flush()
        print(s)
        progress = self.width * count / self.total
        sys.stdout.write("{0:3}/{1:3}".format(count,self.total))
        sys.stdout.write("#" * int(progress) + "-" * int(self.width - progress) +"\r")
        if progress == self.width:
            sys.stdout.write("\n")
        sys.stdout.flush()
