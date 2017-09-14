#!/usr/bin/env python
#coding:utf-8

"""
组件 						描述
Button 按钮。				类似标签，但提供额外的功能，例如鼠标掠过、按下、释放以及键盘操作/事件
Canvas 画布。				提供绘图功能（直线、椭圆、多边形、矩形）；可以包含图形或位图
Checkbutton 选择按钮。		一组方框，可以选择其中的任意个（类似 HTML 中的 checkbox）
Entry 文本框。				单行文字域，用来收集键盘输入（类似 HTML 中的 text）
Frame 框架。				包含其他组件的纯容器
Label 标签。				用来显示文字或图片
Listbox 列表框。			一个选项列表，用户可以从中选择
Menu 菜单。					点下菜单按钮后弹出的一个选项列表，用户可以从中选择
Menubutton 菜单按钮。		用来包含菜单的组件（有下拉式、层叠式等等）
Message 消息框。			类似于标签，但可以显示多行文本
Radiobutton 单选按钮。		一组按钮，其中只有一个可被“按下”（类似 HTML 中的 radio）
Scale 进度条。				线性“滑块”组件，可设定起始值和结束值，会显示当前位置的精确值
Scrollbar 滚动条。			对其支持的组件（文本域、画布、列表框、文本框）提供滚动功能
Text 文本域。				多行文字区域，可用来收集（或显示）用户输入的文字（类似HTML中的textarea）
Toplevel 顶级。				类似框架，但提供一个独立的窗口容器。
"""


import Tkinter

top = Tkinter.Tk()
lable = Tkinter.Label(top,text="Hello World!")
lable.pack()
Tkinter.mainloop()