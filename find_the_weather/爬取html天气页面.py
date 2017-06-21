import requests,json
def find_the_weather(city_name):
    try:
        with open('各城市代码（尝试除广州外的其他城市天气）.txt',encoding='utf-8')as g:
            lines=g.readlines()
            for line in lines:
                if city_name in lines:
                    city_data=line.split('=')[0].strip()
   #各个城市天气状况的Api
        url_api = "https://free-api.heweather.com/v5/suggestion?city=CN{code}&key=50246ea62fbd405c9315e51d2a1d29c0'.format(code=city_code)"
        response_life = urllib.request.urlopen(url_life)
        response = urllib.request.urlopen(url)
        weather_html = response.read()
        json_data = json.loads(weather_html)
        return[weather]
    except NameError:
        
        print('不存在此城市或暂无数据')
    
  

