#!/usr/bin/env python

from auth import login

@login
def atm(*args,**kwargs):
    print("atm programmer")
