#!/usr/bin/env python

import  os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_HOME_DIR = os.path.join(BASE_DIR ,"db","user_files")
HOST,PORT = "localhost",9999
help_list = ["list","help","dir","get","put"]