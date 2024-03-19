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

_dollar_buy_kiev = parsing._dollar_buy_kiev
_dollar_sell_kiev = parsing._dollar_sell_kiev

_euro_buy_kiev = parsing._euro_buy_kiev
_euro_sell_kiev = parsing._euro_sell_kiev
#PROMTS
questionPromt_party = f"Розкажи будь-який цікавий факт, пов'язанний з датою {_day} {_month}. Таким фактом може бути офіційне або неофіційне свято, історична подія, або народна прикмета. В пріоритеті мають бути свята та дати, що стосуються Київа, Київської області, України або українців Почни відповідь з фрази (В цей день ). Не пиши нічого окрім відповіді. Дай стислу та лаконічну відповідь, не більше 500 символів. Не коментуй свою відповідь."
questionPromt_names = f"Дай мені список всіх іменин, які відмічаються {_day} {_month}. Список має бути через кому, в один рядок. У відповіді не пиши нічого крім списка іменин. Дай стислу та лаконічну відповідь, не більше 500 символів. Не коментуй свою відповідь."
questionPromt_goodDay = "Побажай чогось приємного. Почни відповідь зі слова (Бажаю). Не пиши нічного крім побажання. Дай стислу та лаконічну відповідь, не більше 500 символів. Не коментуй свою відповідь."
questionPromt_church = f"Розкажи, які церковні свята відзначаються в Україні  {_day} {_month} в 2024 році? Дай стислу та лаконічну відповідь, не більше 500 символів. Не коментуй свою відповідь."

#TEXTS

thisday = writecalendar.thisday

def gpt_party()->str:
    return gpttest.ask_gpt4(questionPromt_party)
def gpt_church()->str:
    return gpttest.ask_gpt4(questionPromt_church)
def weather_for_next_x_hours(hours:int) ->str:
    forecast = "\nПогода в Хотянівці наближчим часом:\n"
    for i in range(hours):
        forecast+=(parsing.weather_hourly(i))
    return forecast

currency_info = f"\nВ обмінних пунктах Вишгорода сьогодні такий середній курс: \nДоллар: {_dollar_buy}/{_dollar_sell} \nЄвро: {_euro_buy}/{_euro_sell}\n"
avantage_info = f"\nУ мережі АЗС «Авантаж 7» сьогодні такі ціни:\n{parsing.gas_all}\n"
currency_info_kiev = f"\nВ обмінних пунктах Києва сьогодні такий середній курс: \nДолар: {_dollar_buy_kiev}/{_dollar_sell_kiev} \nЄвро: {_euro_buy_kiev}/{_euro_sell_kiev}\n"