 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape#在flash文件夹下找所有的python文件，找文件中类名称，符合的导入

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':#抓取html资料
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上广州天气查询！')

@app.route('/pick_a_date', methods=['POST'])#向服务器发送请求
def pick_a_date() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    user_date = request.form['user_date']	#请求request模块
    return render_template('results.html',
                           the_title = '以下是您选取的日期：',
                           the_date = user_date,
                           )

if __name__ == '__main__': #_name_为命名空间
    app.run(debug=True)
    
