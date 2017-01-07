import calendar

print [i for i in range(1006, 2006, 10) if calendar.weekday(i, 1, 1) == 3 and calendar.isleap(i)][-2]