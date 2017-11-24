#!/usr/bin/env python

from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42,None,"bob"])
    print("hello",conn.recv())
    conn.close()

if __name__ == "__main__":
    parent_conn,child_conn = Pipe()
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send("李阳")
    p.join()