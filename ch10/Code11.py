import json
from tkinter import *
import requests

win = Tk()
win.title('weather API')
win.geometry('700x700')

api_key = '6fe6f8dc606fd5d52f7429fbeca908a8'
city_name = 'Busan'
weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

print(weather_url)

response = requests.get(weather_url)
print('response = ', response)

weather_info = response.json()
print(type(weather_info))
print(json.dumps(weather_info, indent='\t'))

print(weather_info['weather'])
print(weather_info['weather'][0]['description'])
print(weather_info['sys']['sunrise'])

win.mainloop()
