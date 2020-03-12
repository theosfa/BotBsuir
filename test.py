from pytz import timezone
import requests
import json
from datetime import datetime

def get_current_time():
    return datetime.now(timezone('Europe/Minsk')).strftime('%H:%M')

def get_day_number():
    td = datetime.today().weekday()
    if td == 0:
        return f"Понедельник"
    if td == 1:
        return f"Вторник"
    if td == 2:
        return f"Среда"
    if td == 3:
        return f"Четверг"
    if td == 4:
        return f"Пятница"
    if td == 5:
        return f"Суббота"
    if td == 6:
        return f"Воскресенье"

def get_week_number():
    weeks = 'http://journal.bsuir.by/api/v1/week'
    week = requests.get(weeks).json()
    return week

def reading_schedules():
    with open("static/schedules.json", "r", encoding='utf-8') as read_file:
        schedules = json.load(read_file)
    return schedules

def reading_auditories():
    with open("static/auditories.json", "r", encoding='utf-8') as read_file:
        auditories = json.load(read_file)
    return auditories

def search_empty_auditory():
    # Preparation
    week = get_week_number()
    td = get_day_number()
    time = '10:00'
    schedules = reading_schedules()
    auditories = reading_auditories()

    for key in schedules:
        for i in schedules[key]["schedules"]:
            if i["weekDay"] == td:
                for j in i["schedule"]:
                    for n in j["weekNumber"]:
                        if n == week:
                            if time > j["startLessonTime"] and time < j["endLessonTime"]:
                                try:
                                    list = j["auditory"][0].rsplit('-', maxsplit=1)
                                    if int(list[1]) == 1:
                                        auditories["1"][str(list[0])] = 1
                                    if int(list[1]) == 2:
                                        auditories["2"][str(list[0])] = 1
                                    if int(list[1]) == 3:
                                        auditories["3"][str(list[0])] = 1
                                    if int(list[1]) == 4:
                                        auditories["4"][str(list[0])] = 1
                                    if int(list[1]) == 5:
                                        auditories["5"][str(list[0])] = 1
                                except:
                                    pass

    return auditories


def print_empty(building, auditories):
    a = []
    for j in auditories[str(building)]:
        if auditories[str(building)][j] == 1:
            print(j)
