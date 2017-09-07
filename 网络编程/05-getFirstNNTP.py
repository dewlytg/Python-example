#!/usr/bin/env python
#coding:utf-8

"""
NNTP 对象的方法
方法                         描述
group(name)                  选择一个组的名字，返回一个元组(rsp,ct,fst,lst,group):服务器的返回信息，文章的数量，第一个和最后一个文章的号码以及组名，所有数据都是字符串。（返回的 group 与我们传进去的 name 应该是相同的）
xhdr(hdr, artrg,[ofile])     返回文章范围 artrg('头-尾'的格式)内文章 hdr 头的列表，或输出到文件 ofile 中
body(id[,ofile])             给定文章的 id，id 可以是消息的 ID（放在尖括号里），或一个文章号（是一个字符串），返回一个元组(rsp, anum, mid,data): 服务器的返回信息，文章号（是一个字符串），消息的                                            ID（放在尖括号里），和文章所有行的列表或把数据输出到文件 ofile 中。
head(id)                     与 body()相似，只是返回的元组中那个行的列表中只包含了文章的标题。
article(id)                  也跟 body()一样，只是返回的元组中那个行的列表中包含了文章的标题和内容。
stat(id)                     让文章的“指针”指向 id（同上，是一个消息的 ID 或是文章的号码）。返回一个跟 body 一样的元组(rsp, anum, mid)，但不包含文章的数据。
next()                       用法和 stat()类似，把文章指针移到下一篇文章，返回与stat()相似的元组
last()                       用法和 stat()类似，把文章指针移到最后一篇文章，返回与stat()相似的元组
post(ufile)                  上传 ufile 文件对象里的内容（使用 ufile.readline()），并在当前新闻组发表。
quit()                       关闭连接，然后退出
跟上一节的 FTP 对象表一样，还有一些 NNTP 对象的方法没有提及。为了避免混乱，我们只列出
了你可能用得到的。其余的，我们再次建议你参考 Python 手册
"""


import nntplib
import socket

HOST = "your.nntp.server"
GRNM = "comp.lang.python"
USER = "wesley"
PASS = "you'11NeverGuess"

def main():
    try:
        n = nntplib.NNTP(HOST)
    except socket.gaierror,e:
        print "ERROR: cannot reach host %s" % HOST
        print "%s" % str(e)
        return
    except nntplib.NNTPPermanentError,e:
        print "ERROR: access denied on %s" % HOST
        print "%s" % str(e)
        return
    print "*** Connected to host %s" % HOST

    try:
        rsp,ct,fst,lst,grp = n.group(GRNM)
    except nntplib.NNTPPermanentError,e:
        print "ERROR: cannot load group %s" % GRNM
        print "%s" % str(e)
        print "Server may require authenication"
        print "Uncomment/edit login line above"
        n.quit()
        return
    except nntplib.NNTPTemporaryError,e:
        print "ERROR: group %s unavailable" % GRNM
        print "%s" % str(e)
        n.quit()
        return
    print "*** Found newsgroup %s" % GRNM

    rng = "%s-%s" %(lst,lst)
    rsp,frm = n.xhdr("from",rng)
    rsp,sub = n.xhdr("subject",rng)
    rsp,dat = n.xhdr("date",rng)
    print """*** Found last article (#%s):
    
    From: %s
    Subject: %s
    Date: %s
    """% (lst,frm[0][1],sub[0][1],dat[0][1])

    rsp,anum,mid,data = n.body(lst)
    displayFirst20(data)
    n.quit()

def displayFirst20(data):
    print "*** First (<= 20) meaningful lines:\n"
    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True
    for line in lines:
        if line:
            lower = line.lower()
            if (lower.startswith(">")) and not \
                lower.startswith(">>>") or \
                lower.startswith("|") or \
                lower.startswith("in article") or \
                lower.endswith("writes:") or \
                lower.endswith("wrote:"):
                continue
            if not lastBlank or (lastBlank and line):
                print "%s" % line
                if line:
                    count += 1
                    lastBlank = False
                else:
                    lastBlank = True
                if count == 20:
                    break

if __name__ == "__main__":
    main()