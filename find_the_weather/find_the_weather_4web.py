
# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/pick_a_date', methods=['POST'])
def pick_a_date() -> 'html':
    date = request.form['date'] #输入日期
    city = request.form['city'] #输入城市名称
    results = find_the_weather #输出有关日期和城市的相关天气
    return render_template('results.html',
                           the_title = '以下是您所查询的天气：',#请求返回title和data.
                           the_date=date,
                           the_temperature=results[1],
                           the_condition=results[2]
                           
                          )

@app.route('/')#@app.route是“装饰器”，接受route为参数，返回一个新的函数。
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上天气查询！')#返回输入title界面。




                        
if __name__ == '__main__':#__main__为命名空间，__name__是指示当前py文件调用方式的方法。如果它等于"__main__"就表示是直接执行.
    app.run(debug=True)
    
