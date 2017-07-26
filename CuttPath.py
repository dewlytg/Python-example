#!/usr/bin/env python
# coding:utf-8

__author__ = "dewly_tg"

import importlib

def getPath(module):
    mresult = importlib.import_module(module)
    mpath = mresult.__file__
    return  mpath