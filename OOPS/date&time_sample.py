#to print date and time
import datetime


print(datetime.datetime.now())
#to find the code time
starttime=datetime.datetime.now()
#to print date only
print(datetime.date.today())

#to change the order of the day month year

today=datetime.date.today()
print(today.strftime("%d-%m-%Y"))
#to asing a date
x = datetime.datetime(year=2021,month=3,day=11)
y = datetime.datetime(year=2020,month=3,day=11)
print(x)
print(y)
#to find the difference bitween x and y
difference = x-y
print(difference)
#to find the code start to end time
end=datetime.datetime.now()
differ=end-starttime


print(differ)