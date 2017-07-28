#coding:utf-8

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

for i,v in enumerate(l1):
    print i,v

for i in range(10):
    if i == 3:
        continue
    elif i == 8:
        break
    print i

num = 0
while num < 10:
    print num
    num += 1
