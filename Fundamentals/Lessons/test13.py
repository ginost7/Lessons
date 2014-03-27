


def day(name):
    while True:
        day= raw_input('what day is it?: ')
        if name in ['Saturday', 'Sunday']:
            return 'weekend'
        elif name in ['Monday','Tuesday','wednesday','thursday','friday']:
            return 'weekday'
        else:
            return 'not a day'

print day('Monday')
