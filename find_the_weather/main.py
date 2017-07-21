import requests,json,urllib.request #python中的import语句是用来导入模块的,在这里导入了requests和json模块
def find_the_weather(city_name): #定义def函数查询天气 变量为city_name
   try: 
      with open('city_name.txt','r',encoding='utf8)as fp:
                lines=fp.readlines()
                for line in lines:
                 if city in line:
                city_code=line.split('=')[0].strip()
                
   #各个城市天气状况的Api
        url_api = ( 'https://api.seniverse.com/v3/weather/now.json?key=hfkphvdhmqghnrfq&location=%s&language=zh-Hans&unit=c'%city_name)
        response = urllib.request.urlopen(url_api)#使用urllib.request 来抓取api资源.
        weather_html = response.read()
        json_data = json.loads(weather_html)
        
        return [json_data()]
   except NameError :
        print('不存在此城市或暂无数据')
              
    
  

