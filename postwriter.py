import writecalendar
import parsing
import gpttest

thisday = writecalendar.thisday
_day = writecalendar._day
_month = writecalendar._month


_95 = parsing.gas_95
_dizel = parsing.gas_dizel
_gaz = parsing.gas_gaz

#PROMTS
questionPromt_party = f"Розкажи будь-який цікавий факт, пов'язанний з датою {_day} {_month}. Таким фактом може бути офіційне або неофіційне свято, історична подія, або народна прикмета. В пріоритеті мають бути свята та дати, що стосуються Київа, Київської області, України або українців Почни відповідь з фрази (В цей день ). Не пиши нічого окрім відповіді"
questionPromt_names = f"Дай мені список всіх іменин, які відмічаються {_day} {_month}. Список має бути через кому, в один рядок. У відповіді не пиши нічого крім списка іменин. "
questionPromt_goodDay = "Побажай чогось приємного. Почни відповідь зі слова (Бажаю). Не пиши нічного крім побажання"

_partys_4 = gpttest.ask_gpt4(questionPromt_party)
_names_4 = gpttest.ask_gpt4(questionPromt_names)
_goodDay = gpttest.ask_gpt4(questionPromt_goodDay)

maintext = f"Добри ранок, Хотянівка! \n{thisday} \n\
Ціни на пальне зараз такі:  \n\
бензин - {_95}\n\
дизельне пальне - {_dizel}\n\
газ - {_gaz}\n\
\n\
{_partys_4}\n\
іменин сьогодні відзначають {_partys_4}\n\
{_goodDay} "

print(maintext)