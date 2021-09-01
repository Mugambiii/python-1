import datetime

#date only
today = datetime.date.today()
print(today)

#date and current time
# today = datetime.datetime.now()
# print(today)
# print(today.year)
# print(today.month)
# print(today.weekday())

#days are indexed from zero - monday is zero and sunday is 6
#name of the weekday
print(today.strftime("%A"))
print(today.strftime("%B"))
print(today.strftime("%Y"))

x = datetime.datetime
month = x.today().month
print(month)

month = datetime.datetime.today().month
day = datetime.datetime.today().strftime(("%d"))
if month == 9 and day ==29:
    print("Happy Birthday Babra")
else:
    print("Today's date is {}/ {}".format(day,month))
