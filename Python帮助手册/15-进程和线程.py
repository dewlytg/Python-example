#coding:utf-8


"""
    在语句os.fork()之前，只有一个进程在执行这段代码，但在这条语句之后，就变成两个进程在执行了，这两个进程的几乎完全相同，将要执行的下一条语句都是if pid == 0……
    为什么两个进程的fpid不同呢，这与fork函数的特性有关。fork调用的一个奇妙之处就是它仅仅被调用一次，却能够返回两次，它可能有三种不同的返回值：
    1）在父进程中，fork返回新创建子进程的进程ID；
    2）在子进程中，fork返回0；
    3）如果出现错误，fork返回一个负值；

    在fork函数执行完毕后，如果创建新进程成功，则出现两个进程，一个是子进程，一个是父进程。在子进程中，fork函数返回0，在父进程中，fork返回新创建子进程的进程ID。我们可以通过fork返回的值来判断当前进程是子进程还是父进程。
"""
#1)linux 平台多进程，单个子进程
import os

print "Process (%s) start..." % os.getpid()
pid = os.fork()
if pid == 0:
    print "I am child process (%s) and my parent is %s." %(os.getpid(),os.getppid())
else:
    print "I (%s) just created a child process (%s)." %(os.getpid(),pid)

#2)跨平台多进程，单个子进程
from multiprocessing import Process

def run_proc(name):
    print "Run child process %s (%s)" %(name,os.getpid())

if __name__ == "__main__":
    print "Parent process %s." % os.getpid()
    p = Process(target=run_proc,args=("test_code",))
    print "Child process will start."
    p.start()
    p.join()
    print "Child process end."

#3)跨平台多进程，多个子进程
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print "Run task %s (%s)..." %(name,os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print "Task %s run %0.f seconds." %(name,(end - start))

if __name__ == "__main__":
    print "Parent process %s." % os.getpid()
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print "Waiting for all subprocess done..."
    p.close()
    p.join()
    print "All subprocess done."

#4)suprocess子进程
import subprocess
print "nslookup www.qq.com"
r = subprocess.call(["nslookup","www.qq.com"])
print "Exit cod:"

print "nslookup"
p = subprocess.Popen(["nslookup"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,error = p.communicate(b"set q=mx\nqq.com\nexit\n")
print output.decode("utf-8")
print "Exit cod:",p.returncode

#5)threading多线程
import threading
def loop():
    print "thread %s is running..." % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print "thread %s >>> %s" %(threading.current_thread().name,n)
        time.sleep(1)
    print "thread %s ended." % threading.current_thread().name

print "thread %s is running..." % threading.current_thread().name
t = threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
print "thread %s ended." % threading.current_thread().name

"""
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时修改一个变量，把内容给改乱了。
"""

# 假定这是你银行的存款
balance = 0

def change_it(n):
    # 先存后取，结果应该是0
    global balance
    balance = balance + n
    balance = balance - n
    print balance

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

"""
两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。
"""

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    print balance

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance


# 创建全局ThreadLocal对象：
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

#6)分布
"""
在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
"""

# _*_ coding:utf-8 _*_
import random, time, Queue
from multiprocessing.managers import BaseManager

# the Queue of send tasks
task_Queue = Queue.Queue()
# the Queue of recive tasks
result_Queue = Queue.Queue()

# cong BaseManager jicheng de QueueManager
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_Queue', callable=lambda: task_Queue)
QueueManager.register('get_result_Queue', callable=lambda: result_Queue)

# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')

# 启动Queue
manager.start()

# 获得通过网络访问的Queue对象
task = manager.get_task_Queue()
result = manager.get_result_Queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

# Close
manager.shutdown()
print('master exit.')


#coding:utf-8

import time, sys, Queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_Queue')
QueueManager.register('get_result_Queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_Queue()
result = m.get_result_Queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task Queue is empty.')
# 处理结束:
print('worker exit.')