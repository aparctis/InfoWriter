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

# CURENCY
link_curency = "https://minfin.com.ua/ua/currency/vyshgorod/"
responseCurency = requests.get(link_curency).text

soup_curency = BeautifulSoup(responseCurency, 'lxml')
block_curency = soup_curency.find_all('td')

_dollar_buy = (block_curency[21].text)[:5]
_dollar_sell = (block_curency[22].text)[:5]

_euro_buy = (block_curency[24].text)[:5]
_euro_sell = (block_curency[25].text)[:5]


#WEATHER
weather_key = "495a964eee926a3247a8b3e05ea862f9"
lat = 50.59578586580147
lon = 30.56590316399478
weather_request = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&lang=ua&appid={weather_key}"

weather_request = requests.get(weather_request)
weather_json = weather_request.json()

_list = weather_json['list']

def weather_hourly(hourIndex:int)->str:
	weather_time = _list[0]['dt_txt'][11:16]
	weather_sky = _list[0]['weather'][0]['description']
	

list_1 = _list[0]['dt_txt'][11:16]

sky = _list[0]['weather'][0]['description']

print(list_1)

#def celsius(kelvin):
	#c = kelvin-273.15
	#return c


#for i in range(len(_list)):
	#print(_list[i]['dt_txt'])
