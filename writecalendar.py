from datetime import datetime
import calendar

months_genitive = [
    "січня",
    "лютого",
    "березня",
    "квітня",
    "травня",
    "червня",
    "липня",
    "серпня",
    "вересня",
    "жовтня",
    "листопада",
    "грудня"
]

current_date = datetime.now()
_month = months_genitive[current_date.month-1]
_day = current_date.day
_year = current_date.year

weekDay = calendar.weekday(current_date.year, current_date.month, current_date.day)
weekdays = [
	"понеділок",
	"вівторок",
	"середа",
	"четвер",
	"п'ятниця",
	"субота",
	"неділя",
	]

_weekday = weekdays[weekDay-1]


thisday = (f"Сьогодні {_weekday}, {_day} {_month} {_year} року")