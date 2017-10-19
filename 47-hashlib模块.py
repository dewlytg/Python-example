#!/usr/bin/env python
#-*-coding:utf-8-*-

import hashlib

m = hashlib.md5()
m.update(b"Hello")
print m.hexdigest()
m.update(b"It's me")
print m.hexdigest()
m.update(b"It's been a long time since we spoken...")
print m.hexdigest()

s = hashlib.sha256()
s.update(b"Hello")
print s.hexdigest()