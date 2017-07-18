
# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__) #初始化生成一个app对象，这个对象就是Flask的当前实例对象，后面的各个方法调用都是这个实例，Flask会进行一系列自己的初始化

@app.route('/pick_a_date', methods=['POST']) #method是function与对象的结合。我们调用一个方法的时候，有些参数是隐含的传递过去的。
def pick_a_date() -> 'html':
    date = request.form['date'] #输入日期
    city = request.form['city'] #输入城市名称
    results = find_the_weather #输出有关日期和城市的相关天气
    return render_template('results.html',#return是返回数值的意思
                           the_title = '以下是您所查询的天气：',#请求返回title和data.
                           the_date=date,
                           the_temperature=results[1],
                           the_condition=results[2]
                           
                          )

@app.route('/')#@app.route是“装饰器”，接受route为参数，返回一个新的函数。
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',#render_template的功能是先引入results.html，同时根据后面传入的参数，对html进行修改渲染。
                           the_title='欢迎来到网上天气查询！')#返回输入title界面。




                        
if __name__ == '__main__':#__main__为命名空间，__name__是指示当前py文件调用方式的方法。如果它等于"__main__"就表示是直接执行.
    app.run(debug=True) #debug通常称为调试版本，通过一系列编译选项的配合，编译的结果通常包含调试信息，而且不做任何优化，以为开发 人员提供强大的应用程序调试能力。而
    
