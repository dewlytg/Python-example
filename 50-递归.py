
"""
经典递归案例
"""

comment_list = [
    {"id":1,"user":"张三","content":"php是最好的语言","parent_id":None},
    {"id":2,"user":"李四","content":"python也不错","parent_id":None},
    {"id":3,"user":"王五","content":"php不一定哟","parent_id":1},
    {"id":4,"user":"二桃","content":"php必须好","parent_id":1},
    {"id":5,"user":"张亮","content":"php一定好吗","parent_id":3},
    {"id":6,"user":"李逵","content":"java最棒","parent_id":None},
    {"id":7,"user":"宋江","content":"send也可以","parent_id":None},
    {"id":8,"user":"曹总","content":"java确实好","parent_id":6},
    {"id":9,"user":"世界","content":"巴拉巴拉","parent_id":6},
    {"id":10,"user":"师姐","content":"历险记","parent_id":9},
    {"id":11,"user":"师姐","content":"历险记","parent_id":10},
    {"id":12,"user":"师姐","content":"历险记","parent_id":11},
]

## 方法一
class Node:
    @staticmethod
    def recursive(ret,row):
        for i in ret:
            if i.get("id") == row.get("parent_id"):
                row["children"] = []
                i["children"].append(row)
            else:
                Node.recursive(i["children"], row)

    @staticmethod
    def create_tree(comment_list):
        ret = []
        for row in comment_list:
            # 一级评论
            if not row.get("parent_id"):
                row["children"] = []
                ret.append(row)
            # 非一级评论
            else:
                Node.recursive(ret,row)
        return ret


ret = Node.create_tree(comment_list)
for line in ret:
    print(line)


## 方法二
ret = []
comment_dict = {}
for line in comment_list:
    line.update({"children":[]})
    comment_dict[line["id"]] = line

for row in comment_list:
    if not row.get("parent_id"):
        ret.append(row)
    else:
        comment_dict.get(row.get("parent_id"))["children"].append(row)

for line in ret:
    print(line)