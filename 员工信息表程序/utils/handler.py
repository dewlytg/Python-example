#!/usr/bin/env python

class FileHandler(object):
    def __init__(self,filename):
        self.filename = filename
        self.data = open(self.filename).readlines()

    @property
    def get_columns(self):
        return self.data[0].strip().split(",")

    @property
    def _get_meta(self):
        return self.data[1:]

    @property
    def _get_staff_id(self):
        meta_list = self._get_meta
        staff_id_list = []
        for i in meta_list:
            staff_id = i.strip().split(",")[0]
            staff_id_list.append(staff_id)
        return max(staff_id_list)

    def get_info(self):
        columns_list = self.get_columns
        meta_list = self._get_meta
        info_list = []
        for i in meta_list:
            record = i.strip().split(",")
            info_list.append(dict(zip(columns_list,record)))
        return info_list

    def save2file(self,obj):
        if isinstance(obj,str):
            staff_id = int (self._get_staff_id) + 1
            staff_new_record = "\n" + str(staff_id) + "," + str(obj)
            fd = open(self.filename, "a")
            fd.write(staff_new_record)
            fd.close()
        elif isinstance(obj,list):
            fd = open(self.filename, "w")
            write_list = []
            first_line = ",".join(self.get_columns) + "\n"
            write_list.append(first_line)
            for i in obj:
                line = ",".join(i.values()) + "\n"
                write_list.append(line)
            fd.writelines(write_list)

if __name__ == "__main__":
    obj = FileHandler("../db/staff_table")
    # obj.save2file("Mack,40,13561453430,HR,2009-03-11")
    # obj.save2file([{'staff_id': '2', 'name': 'Jack', 'age': '30', 'phone': '13304320533', 'dept': 'HR', 'enroll_date': '2015-05-03'}, {'staff_id': '3', 'name': 'Rain', 'age': '25', 'phone': '13832353220', 'dept': 'Sales', 'enroll_date': '2016-04-22'}, {'staff_id': '4', 'name': 'Mack', 'age': '40', 'phone': '13561453430', 'dept': 'HR', 'enroll_date': '2009-03-11'}])
    # print(obj.get_info())