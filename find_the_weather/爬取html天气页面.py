import requests,json,urllib.request
def find_the_weather(city_name):
   #各个城市天气状况的Api
        url_api = ( 'https://api.seniverse.com/v3/weather/now.json?key=hfkphvdhmqghnrfq&location=%s&language=zh-Hans&unit=c'%city_name)
        response = urllib.request.urlopen(url_api)
        weather_html = response.read()
        json_data = json.loads(weather_html)
        
        return json_data()
    
  

