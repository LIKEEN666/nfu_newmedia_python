Find_the_weather


		
# 简介 
选取日期以及城市看天气，操练Python语言开发练习：使用requests以及flask


	

## 输入：
日期（可下拉选择），城市（手动输入所想要的城市）见templates/entry.html
## 输出：
预期用户得到输出结果为：该日期和该地所对应的天气温度和此时的天气现象（例如小雨，晴，暴雨等等），  见templates/results.html
## 从输入到输出，本组作品使用了：
### 模块
•urllib.request
### API
https://api.seniverse.com/v3/weather/now.json?key=hfkphvdhmqghnrfq&location=guangzhou&language=zh-Hans&unit=c
心知天气api（免费获取实时温度和天气现象）

Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

後端伺服器启动：执行 find_the_weather.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

後端伺服器web 响应：find_the_weather.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/entry.html会出现《欢迎来到网上天气查询！》的HTML页面

前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'city’和‘date’，，详见HTML模版templates/entry.html

前端浏览器web 请求：用户选取指标後按了提交钮「寻找」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_date'，以POST为方法，动作为／find_the_weather web 请求

後端服务器收到用户web 请求，匹配到@app.route('/pick_a_date', methods=['POST'])的函数 pick_a_date()

find_the_weather_4web.py 中 def pick_a_date() 函数，把用户提交的数据，以flask 模块request	取到Web 请求，再使用flask模块render_template 函数以templates/results.html模版为基础（输出）。

前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。



## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)


		成员列表，统计用，一人一行，输入Github 帐户名即可（此行完成後应删）
