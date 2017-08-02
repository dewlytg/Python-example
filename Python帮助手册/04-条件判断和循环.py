#coding:utf-8

"""
if,for,while都可以使用else，for和while使用else的时候必须是正常结束循环才会触发else语句，注意使用not，and，or，is
"""

score = int(raw_input("Please input a number: "))
if score >= 90:
    print "A"
elif score >=80 and score < 90:
    print "B"
elif score >=60 and score < 80:
    print "C"
else:
    print "D"

l1 = ["apple","vivo","hawei","mi"]
for i in l1:
    print i
else:
    print "over cycle"

for i,v in enumerate(l1):
    print i,v
else:
    print "over cycle"

for i in range(10):
    if i == 3:
        continue
    elif i == 8:
        break
    print i
else:
    print "over cycle"

num = 0
while num < 10:
    print num
    num += 1
else:
    print "over cycle"
