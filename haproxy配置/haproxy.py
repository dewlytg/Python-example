#!/usr/bin/env python

from utils import handler

class HaConfig(object):

    def __init__(self,hafile):
        self.hafile = hafile
        self.data = open(hafile,encoding="utf-8").readlines()
        self.requried = ["server","ip","port"]
        self.optional = ["cookie","check inter","weight","fall","rise"]
        self.ha_list = handler.lrspace(self.data)
        self.ha_dic = handler.list2dic(self.ha_list)

    def showHa(self):
        print("".join(self.data))

    def addHa(self,backend=None):
        if backend in self.ha_dic:
            print("The backendname is exist!")
        else:
            is_sure = input("Are you sure to add backend [%s] (y/n) ?"%backend)
            if is_sure == "y":
                self.ha_list.append("backend %s" %backend)
                while True:
                    print("Please input the required items [%s]" % " ".join(self.requried))
                    required_str = input("server [xxxxx] ip:port [x.x.x.x:x]")
                    ret = handler.auth(required_str)
                    if ret["status"]:
                        temp = ret["data"]
                        print("Please input the optional items [%s]" % " ".join(self.optional))
                        for i in range(len(self.optional)):
                            optional_item = input("Please input the optional [%s]" % self.optional[i])
                            if optional_item:
                                temp += " " + self.optional[i] + " " + optional_item
                                print(temp)
                        else:
                            self.ha_list.append(temp)
                    else:
                        print("You's inputs is wrong")
                        continue
                    is_quit = input("Please input your choice q or g? (q/Q)")
                    if is_quit == "q":
                        break
                    elif is_quit == "g":
                        continue
                handler.saveToFile(self.ha_list,self.hafile)

    def editHa(self):
        print(self.ha_dic.keys())
        edit_choice = input("Please choice a backend what do you want to edit?")
        print(self.ha_dic[edit_choice])
        edit_server = input("Please choice a server what do you want to edit?")
        while True:
            edit_option = input("Please choice a option what do you want to edit?")
            edit_value = input("Edit [%s] to a new value "% edit_option)
            if edit_option == "port" or edit_option == "ip":
                self.ha_dic[edit_choice][edit_server][edit_option] = edit_value
            else:
                self.ha_dic[edit_choice][edit_server]["options"][edit_option] = edit_value
            is_quit = input("Please input your choice q or g? (q/Q)")
            if is_quit == "q":
                break
            elif is_quit == "g":
                continue
        ha_list = handler.dic2list(self.ha_dic)
        handler.saveToFile(ha_list,self.hafile)

    def removeHa(self):
        remove_choice = input("Please choice a backend what do you want to delete?")
        del self.ha_dic[remove_choice]
        ha_list = handler.dic2list(self.ha_dic)
        handler.saveToFile(ha_list,self.hafile)

if __name__ == "__main__":
    obj = HaConfig("conf/haproxy.cfg")
    # obj.showHa()
    # obj.addHa(backend="test")
    # obj.editHa()
    obj.removeHa()