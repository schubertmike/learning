import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025,11,27)

days_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print('My next birthday is ' + str(days_away.days) + ' days away!')
