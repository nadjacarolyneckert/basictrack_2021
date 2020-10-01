
days= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def dayNameFromWeekday(weekday):
    if weekday>6:
        print('error');
        return 'an unknown day'
    return days[weekday]

nb = int(input('Enter weekday number [0 - 6]: '))
print('\n')


print('Today is ' + dayNameFromWeekday(nb))

