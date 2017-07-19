 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape#在flash文件夹下找所有的python文件，找文件中类名称，符合的导入

app = Flask(__name__)#app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。 

@app.route('/')#@app.route是“装饰器”，接受route为参数，返回一个新的函数。
@app.route('/entry')
def entry_page() -> 'html':#抓取html资料
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上广州天气查询！')

@app.route('/pick_a_date', methods=['POST'])#向服务器发送请求
def pick_a_date() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    user_date = request.form['user_date']	#请求request模块
    return render_template('results.html',#render_template的功能是先引入results.html，同时根据后面传入的参数，对html进行修改渲染。
                           the_title = '以下是您选取的日期：',
                           the_date = user_date,
                           )

if __name__ == '__main__': #_name_为命名空间,__name__是指示当前py文件调用方式的方法。如果它等于"__main__"就表示是直接执行.
    app.run(debug=True)
    
