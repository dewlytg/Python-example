#!/usr/bin/env python
#coding:utf-8

"""
Web框架把我们从WSGI中拯救出来了。现在，我们只需要不断地编写函数，带上URL，就可以继续Web App的开发了。
但是，Web App不仅仅是处理逻辑，展示给用户的页面也非常重要。在函数中返回一个包含HTML的字符串，简单的页面还可以，但是，想想新浪首页的6000多行的HTML，你确信能在Python的字符串中正确地写出来么？反正我是做不到。
俗话说得好，不懂前端的Python工程师不是好的产品经理。有Web开发经验的同学都明白，Web App最复杂的部分就在HTML页面。HTML不仅要正确，还要通过CSS美化，再加上复杂的JavaScript脚本来实现各种交互和动画效果。总之，生成HTML页面的难度很大。
由于在Python代码里拼字符串是不现实的，所以，模板技术出现了。
使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：

1.浏览器请求 ---> GET /Michael?name="Michael"
                 |
2.app.py  ---> @app.route("/<name>")
               def home(name):
                    return render_template("home.html",name=name) #变量{{ name }} 替换为'Michael'

3.模板 ---> <html>
                   <body>
                          <p>Hello, {{ name }}</p>
                   </body>
            </html>
               | 输出
4.用户看到的 ---> <html>
                   <body>
                          <p>Hello, Michael</p>
                   </body>
            </html>

这就是传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”。
Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。




上面的例子中，Model就是一个dict：
{ 'name': 'Michael' }
只是因为Python支持关键字参数，很多Web框架允许传入关键字参数，然后，在框架内部组装出一个dict作为Model。
现在，我们把上次直接输出字符串作为HTML的例子用高端大气上档次的MVC模式改写一下：
"""
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()