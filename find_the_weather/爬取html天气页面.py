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
   url = ('https://api.seniverse.com/v3/weather/now.json?key=hfkphvdhmqghnrfq&location=beijing&language=zh-Hans&unit=c'.format(location=city_code))

        response = urllib.request.urlopen(url)
        weather_html = response.read()
        json_data = json.loads(weather_html)
        #print(json_data)
        
        
        
        return[weather]
      
      
      except NameError :
        print('不存在此城市或暂无数据')
    
  

