the_
# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/pick_a_date', methods=['POST'])
def pick_a_date() -> 'html':
    date = request.form['date']
    city = request.form['city']
    results = find_the_weather
    return render_template('results.html',
                           the_title = '以下是您所查询的天气：',
                           the_date=date,
                           the_temperature=results[1],
                           the_condition=results[2]
                           
                          )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上天气查询！')




                        
if __name__ == '__main__':
    app.run(debug=True)
    
