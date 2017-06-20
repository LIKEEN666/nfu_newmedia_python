Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
import urllib.requests,json
def get_the_weather(city_name):
  try:
    with open('各城市代码（尝试除广州外的其他城市天气）.txt',encoding='utf-8')as g:
      lines=g.readlines()
      for line in lines:
        if city_name in lines:
          city_data=line.split('=')[0].strip()
   #各个城市天气状况的Api
  url=
    
  

>>> r=requests.get("http://m.weather.com.cn/mweather/101280101.shtml")
>>> r.status_code
200
>>> r.encoding
'ISO-8859-1'
>>> r.text[:1000]
'ï»¿<!DOCTYPE HTML>\r\n<html>\r\n<head>\r\n<meta charset="utf-8">\r\n<meta name="viewport" content="width=device-width,initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">\r\n<link type="text/css" rel="stylesheet" href="http://i.tq121.com.cn/c/wap/wap.css?id=2016">\r\n<script type="text/javascript" src="http://i.tq121.com.cn/j/jquery-1.8.2.js?20140529_105543"></script>\r\n<style>\r\n.weather-two {\r\n\tposition:relative;\r\n\tcolor:#fff;\r\n\theight:108px;\r\n\tmargin: 20px auto 5px;\r\n\twidth:95%;\r\n\toverflow:hidden;\r\n\tmargin-bottom:5px;\r\n\t}\r\n.weather-two .weather-weather {\r\n\r\n}\r\n.weather-two .weather-weather i.svnicon {\r\n\r\n}\r\n.weather-wd {\r\n\tfont-size:100px;\r\n\tfloat: left;\r\n\theight:100px;\r\n\t\r\n\tmargin-left:10px;\r\n\t\r\n}\r\n.weather-wd-top {\r\n\tfloat:left;\r\n\tfont-size: 20px;\r\n    margin-top: 17px;\t\r\n}\r\n.weather-tqqk {\r\n\tfloat:left;\r\n\tmargin-top:41px;\r\n\r\n}\r\n.weather-tq {\r\nmargin-bottom: 12px;\r\n}\r\n.weather-gdw {\r\n}\r\n.weather-gdw i.iconfont {\r\n}\r\n.weather-three {\r\n\tclear:both;\r\n\twidth:95%;\r\n\tmargin:0 a'
>>> 
