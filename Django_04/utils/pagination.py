#!/usr/bin/env python
class Page:
    def __init__(self,current_page,data_len,per_page_data=10,per_page_num=7):
        self.current_page = current_page
        self.data_len = data_len
        self.per_page_data = per_page_data
        self.per_page_num = per_page_num

    @property
    def start(self):
        return (self.current_page -1 ) * self.per_page_data

    @property
    def end(self):
        return (self.current_page +1 ) * self.per_page_data

    def page_str(self,base_url):
        str_list = []
        page_counts, remainder = divmod(self.data_len,self.per_page_data)
        pager_num_half = int(self.per_page_num / 2)
        if remainder:
            total_counts = int(page_counts + 1)
        else:
            total_counts = int(page_counts)

        if self.per_page_num > total_counts:
            start_index = 1
            end_index = total_counts + 1
        else:
            if self.current_page > pager_num_half + 1:
                start_index = self.current_page - pager_num_half
                end_index = self.current_page + pager_num_half + 1
                if self.current_page + pager_num_half > total_counts:
                    start_index = total_counts - self.per_page_num + 1
                    end_index = total_counts + 1
            else:
                start_index = 1
                end_index = self.per_page_num + 1

        if self.current_page == 1:
            prev_page = '<a class="page" href="#">上一页</a>'
        else:
            prev_page = '<a class="page" href="{base_url}?p={num}">上一页</a>'.format(base_url=base_url,num=self.current_page - 1)
        str_list.append (prev_page)
        for i in range (start_index, end_index):
            if i == self.current_page:
                str_list.append ('<a class="page active" href="{base_url}?p={num}">{num}</a>'.format(base_url=base_url,num=i))
            else:
                str_list.append ('<a class="page" href="{base_url}?p={num}">{num}</a>'.format(base_url=base_url,num=i))
        next_page = '<a class="page" href="{base_url}?p={num}">下一页</a>'.format(base_url=base_url,num=self.current_page + 1)
        str_list.append (next_page)
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
            """ % base_url
        str_list.append(jump)
        return str_list
