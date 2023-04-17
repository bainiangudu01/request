import datetime

date1,date2= datetime.date(2023, 4, 18),datetime.date(2023, 5, 4)
s1,s2= date1.strftime("%j").lstrip('0'),date2.strftime("%j").lstrip('0')

print(int(s2) - int(s1))