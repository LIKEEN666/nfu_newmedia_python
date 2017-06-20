 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/content', methods=['POST'])
def show_content() -> 'html':
    date = request.form['data']
    results = find_the_weather
    return render_template('results.html',
                           the_date=date,
                           the_day_weather=results[1],
                          )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上天气查询！')



if __name__ == '__main__':
    app.run(debug=True)
    
