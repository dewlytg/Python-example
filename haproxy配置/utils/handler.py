#!/usr/bin/env python

import  re
pattern = r"\w+\s+(?P<servername>\w+)\s+(?P<ip>\d+.\d+.\d+.\d+):(?P<port>\d+)(?P<options>.*)"
pattern_opt = re.compile(r"(\d+)")
pattern_req = "server\s+\w+\s+\d+.\d+.\d+.\d+:\d+"

def auth(string):
    result = {"status":True,"data":None}
    if re.match(pattern_req,string):
        result["data"] = string
    else:
        result["status"] = False
    return result

def lrspace(iterable):
    result = []
    if isinstance(iterable,list):
        for i in iterable:
            if i != "\n":
                i = i.strip()
                result.append(i)
    return result

def saveToFile(iterable,filename):
    result = ""
    if isinstance (iterable, list):
        for i in iterable:
            if i.startswith("backend"):
                result += "\n\n" +i
            elif i.startswith("server"):
                result += "\n\t" + i
        else:
            result = result.lstrip("\n\n")
    fd = open(filename,"w",encoding="utf-8")
    fd.writelines(result)
    fd.close()

def list2dic(iterable,be_patten="backend",sn_pattern="server"):
    result = {}
    if isinstance(iterable,list):
        for i in iterable:
            i = i.strip()
            if i.startswith(be_patten):
                keyname = i.split()[1]
                result[keyname] = {}
            elif i.startswith(sn_pattern):
                server_info_dic = re.search(pattern,i).groupdict()
                result[keyname][server_info_dic["servername"]] = {}
                result[keyname][server_info_dic["servername"]]["options"] = {}
                result[keyname][server_info_dic["servername"]]["ip"] = server_info_dic["ip"]
                result[keyname][server_info_dic["servername"]]["port"] = server_info_dic["port"]
                options_list = pattern_opt.split(server_info_dic["options"])
                options_list.remove("")
                quotient,remainer = divmod(len(options_list),2)
                if not remainer:
                    for i in range(len(options_list)):
                        if i%2 == 0:
                            result[keyname][server_info_dic["servername"]]["options"][options_list[i].strip()] = options_list[i+1]
        else:
            return result

def dic2list(iterable):
    result = []
    if isinstance(iterable,dict):
        for k,v in iterable.items():
            backend_str = "backend " + k
            result.append(backend_str)
            for m,n in v.items():
                options = ""
                server_str = "server " + m
                ip_port_str = n["ip"] + ":" + n["port"]
                for x,y in n["options"].items():
                    options += x + " " + y + " "
                else:
                    temp = server_str + " " + ip_port_str + " " + options
                    temp = temp.rstrip()
                    result.append(temp)

        else:
            return result

if __name__ == "__main__":
    # list2dic(["backend webserver","server web2 10.16.0.10:8085 cookie 2 weight 3 check inter 2000 rise 2 fall 3"])
    # auth("servera web2 10.16.0.10:8085")
    pass