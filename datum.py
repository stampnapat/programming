import calendar 

day = input().split()
day = [ int(x) for x in day]
year = 2009

weekday = calendar.weekday(year, day[1], day[0])

day_eng = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(weekday)
print(day_eng[weekday])
