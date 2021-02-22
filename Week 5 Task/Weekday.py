# Write a program that outputs whether or not today is a weekday
# Author Catherine Leddy
#ref : https://www.w3schools.com/python/python_datetime.asp
# ref : https://www.xspdf.com/resolution/58438157.html



import datetime

weekno= datetime.datetime.today().weekday()

#x=datetime.datetime.now()
#print(x)-this will tell the date but not the day name. Need to change the code 
#so that program knows weekdays.The python weekday function of class date returns the day
#of the week as an integer. It starts from 0 for a Monday and ends at 6 for a Sunday
if weekno<5 :
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")  



