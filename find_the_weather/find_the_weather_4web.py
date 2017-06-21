
# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from main import find_the_weather

app = Flask(__name__)

@app.route('/pick_a_date', methods=['POST'])
def pick_a_date() -> 'html':
    city = request.form['city']
    results = find_the_weather(city)
    return render_template('results.html',
                           the_title = '以下是您所查询的天气：',
                           the_results = results
                           
                          )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上天气查询！')




                        
if __name__ == '__main__':
    app.run(debug=True)
    
