#!/usr/bin/env python
from app01 import models

class Page:
    def __init__(self,current_page,per_page_lines = 20,pagination_nums = 11,host_list = models.Host.objects.all()):
        self.current_page = current_page
        self.per_page_lines = per_page_lines
        self.pagination_nums = pagination_nums
        self.pagination_nums_half = int(self.pagination_nums / 2)
        self.host_list = host_list

    @property
    def start(self):
        start = self.per_page_lines * (self.current_page - 1)
        return start

    @property
    def end(self):
        end = self.per_page_lines * self.current_page
        return end

    @property
    def get_hostlist(self):
        # if self.start == 0:
        #     data = self.host_list.filter(id__gte=self.start, id__lte=self.end)
        # else:
        #     data = self.host_list.filter(id__gte=self.start, id__lt=self.end)
        data = self.host_list[self.start:self.end]
        return data

    def get_str(self,baseurl):
        pagination_counts, remainder = divmod(len(self.host_list), self.per_page_lines)
        page_str_list = []
        if remainder:
            pagination_counts = pagination_counts + 1

        if pagination_counts < self.pagination_nums_half + 1:
            start_index = 1
            end_index = pagination_counts + 1
        else:
            if self.current_page + self.pagination_nums - 1 > pagination_counts:
                start_index = self.current_page
                end_index = pagination_counts
            else:
                start_index = self.current_page
                end_index = self.current_page + self.pagination_nums
        if self.current_page != 1:
            page_str_list.append (
                "<a class='pagination' href='{baseurl}?p={number}'>上一页</a>".format(baseurl=baseurl,number=self.current_page - 1))
        else:
            page_str_list.append ("<a class='pagination' href='#'>上一页</a>")
        for i in range (start_index, end_index):
            page_str_list.append ("<a class='pagination' href='{baseurl}?p={number}'>{number}</a>".format(baseurl=baseurl,number=i))
        if self.current_page < pagination_counts:
            tmp= "<a class='pagination' href='{baseurl}?p={number}'>下一页</a>".format(baseurl=baseurl,number=self.current_page + 1)
        else:
            tmp="<a class='pagination' href='{baseurl}?p={number}'>下一页</a>".format(baseurl=baseurl,number=pagination_counts)
        page_str_list.append(tmp)
        jump = """
                <input type="text"/>
                <a onclick=jumpTo(this);>跳转</a>
                <script>
                    function jumpTo(ths){
                        var text = ths.previousElementSibling.value;
                        var jump_url = "%s?p=" + text
                        location.href = jump_url;
                    }
                </script>
            """ % baseurl
        page_str_list.append(jump)
        return page_str_list