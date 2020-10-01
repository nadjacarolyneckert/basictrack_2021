days= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def dayNameFromWeekday(weekday):
    if weekday>6:
        print('error');
        return 'an unknown day'
    return days[weekday]

day_of_the_week = int(input('What day of the week did you leave for holidays [0 - 6]: '))

duration_holiday= int(input("How long are you on holidays? (in days)"))
holiday_return = (day_of_the_week + duration_holiday)%7


print('You come back from your holidays on a' + dayNameFromWeekday(holiday_return))