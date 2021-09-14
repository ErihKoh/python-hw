import datetime

users = [

    {'Andr': datetime.date(year=1986, month=8, day=5)},
    {'Ted': datetime.date(year=1990, month=8, day=3)},
    {'Bred': datetime.date(year=1990, month=8, day=3)},
    {'Bill': datetime.date(year=1990, month=8, day=2)},
    {'Bob': datetime.date(year=1983, month=8, day=7)},
    {'Vasya': datetime.date(year=1965, month=8, day=1)},
    {'Tom': datetime.date(year=1965, month=7, day=31)},
    {'Roy': datetime.date(year=1995, month=7, day=25)},
    {'Olga': datetime.date(year=1986, month=10, day=2)},
]


def find_birthday(colleagues):
    next_week = []
    current_time = datetime.datetime.now().date()
    start_of_period = current_time - datetime.timedelta(days=current_time.weekday() - 5)
    end_of_period = start_of_period + datetime.timedelta(days=6)
    for item in colleagues:
        for i, val in item.items():
            if end_of_period.strftime('%m-%d') >= val.strftime('%m-%d') >= start_of_period.strftime('%m-%d'):
                next_week.append(item)
    return next_week


def congratulate():
    my_list = find_birthday(users)
    dict_birthday = {}

    for item in my_list:
        for i, val in item.items():
            if val.strftime('%A') == 'Sunday' or val.strftime('%A') == 'Saturday':
                if dict_birthday.get('Monday'):
                    dict_birthday['Monday'] = dict_birthday['Monday'] + ', ' + i
                else:
                    dict_birthday.update({'Monday': i})
            else:
                if dict_birthday.get(val.strftime('%A')):
                    dict_birthday[val.strftime('%A')] = dict_birthday[val.strftime('%A')] + ', ' + i
                else:
                    dict_birthday.update({val.strftime('%A'): i})

    for i, val in dict_birthday.items():
        print(f"{i}: {val}")


if __name__ == "__main__":
    congratulate()
