import writecalendar
import parsing
import gpttest

_day = writecalendar._day
_month = writecalendar._month


_95 = parsing.gas_95
_dizel = parsing.gas_dizel
_gaz = parsing.gas_gaz

_dollar_buy = parsing._dollar_buy
_dollar_sell = parsing._dollar_sell

_euro_buy = parsing._euro_buy
_euro_sell = parsing._euro_sell

#PROMTS
questionPromt_party = f"Розкажи будь-який цікавий факт, пов'язанний з датою {_day} {_month}. Таким фактом може бути офіційне або неофіційне свято, історична подія, або народна прикмета. В пріоритеті мають бути свята та дати, що стосуються Київа, Київської області, України або українців Почни відповідь з фрази (В цей день ). Не пиши нічого окрім відповіді"
questionPromt_names = f"Дай мені список всіх іменин, які відмічаються {_day} {_month}. Список має бути через кому, в один рядок. У відповіді не пиши нічого крім списка іменин. "
questionPromt_goodDay = "Побажай чогось приємного. Почни відповідь зі слова (Бажаю). Не пиши нічного крім побажання"
questionPromt_church = f"Розкажи, які церковні свята відзначаються в Україні  {_day} {_month} в 2024 році"

#TEXTS

thisday = writecalendar.thisday

def pgt_party()->str:
    return gpttest.ask_gpt4(questionPromt_party)
def pgt_church()->str:
    return gpttest.ask_gpt4(questionPromt_church)
def weather_for_next_x_hours(hours:int) ->str:
    forecast = ""
    for i in range(hours):
        forecast+=(parsing.weather_hourly(i))
    return forecast

currency_info = f"В обмінних пунктах Вишгорода сьогодні такий курс: \nДоллар: {_dollar_buy}/{_dollar_sell} \nЄвро: {_euro_buy}/{_euro_sell}"

print(currency_info)