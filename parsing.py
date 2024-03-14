import requests
from bs4 import BeautifulSoup

#парсим цены на бензин
link_avantage = "https://index.minfin.com.ua/ua/markets/fuel/tm/avantazh_7/"
responseAvantage = requests.get(link_avantage).text

soup_gas = BeautifulSoup(responseAvantage, 'lxml')
block_gas = soup_gas.find('div', id="idx-topcontent")

gas = block_gas.find_all('td')[12].text

gas_95 = block_gas.find_all('td')[2].text
gas_dizel = block_gas.find_all('td')[7].text
gas_gaz = block_gas.find_all('td')[12].text

gas_all = (f"Бензин А-95 - {gas_95}\nДизельне паливо - {gas_dizel}\nГаз автомобільний - {gas_gaz}\n")

# CURENCY
link_curency = "https://minfin.com.ua/ua/currency/vyshgorod/"
responseCurency = requests.get(link_curency).text

soup_curency = BeautifulSoup(responseCurency, 'lxml')
block_curency = soup_curency.find_all('td')

_dollar_buy = (block_curency[21].text)[:5]
_dollar_sell = (block_curency[22].text)[:5]

_euro_buy = (block_curency[24].text)[:5]
_euro_sell = (block_curency[25].text)[:5]

# CURENCY KYIV
link_curency_kiev = "https://minfin.com.ua/ua/currency/kiev/"
responseCurency_kiev = requests.get(link_curency_kiev).text

soup_curency_kiev = BeautifulSoup(responseCurency_kiev, 'lxml')
block_curency_kiev = soup_curency_kiev.find_all('td')

_dollar_buy_kiev = (block_curency_kiev[21].text)[:5]
_dollar_sell_kiev = (block_curency_kiev[22].text)[:5]

_euro_buy_kiev = (block_curency_kiev[24].text)[:5]
_euro_sell_kiev = (block_curency_kiev[25].text)[:5]

#WEATHER
weather_key = "495a964eee926a3247a8b3e05ea862f9"
lat = 50.59578586580147
lon = 30.56590316399478
weather_request = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&lang=ua&appid={weather_key}"

weather_request = requests.get(weather_request)
weather_json = weather_request.json()

_list = weather_json['list']

def weather_hourly(hourIndex:int)->str:
	weather_time = _list[hourIndex]['dt_txt'][11:16]
	weather_sky = _list[hourIndex]['weather'][0]['description']
	temp_real = _list[hourIndex]['main']['temp']
	temp_feels_like = _list[hourIndex]['main']['feels_like']
	weather_hourly_text = f"{weather_time} - {weather_sky}, {temp_real}C (відчувається як {temp_feels_like}) \n"
	return weather_hourly_text

