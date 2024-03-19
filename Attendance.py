import math


def correctdate():
    global date, month, year, days
    if date > 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        date = 1
        month = 1 if month == 12 else month + 1
        year = year + 1 if month == 12 else year
    elif date > 30 and (month == 4 or month == 6 or month == 9 or month == 11):
        date = 1
        month += 1
    elif date > 28 and month == 2 and year % 4 != 0:
        date = 1
        month += 1
    elif date > 29 and month == 2 and year % 4 == 0:
        date = 1
        month += 1


def printdate():
    global date, month, year, days
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    print("{:^17} {:^10}".format(str(date) + " " + months[month-1] + " " + str(year), days[today-1]), end="")
    date += 1


future_delivered = delivered = int(input("Enter total number of delivered lectures: "))
future_attended = attended = int(input("Enter total number of attended lectures: "))
today = int(input("Enter today 1 2 3 4 5 for Mon Tue Wed Thu Fri: "))
date = int(input("Enter today's date: "))
month = int(input("Enter current month: "))
year = int(input("Enter current year: "))

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
classes = [6, 5, 4, 3, 3]

attendance = attended / delivered * 100
week = 1
print("\n{:^40}".format("Today"))
print("-" * 40)
print("{:^17} {:^10} {:^12}".format("Date", "Day", "Attendance"))
print("-" * 40)
printdate()
print("{:^12}".format(str(math.ceil(attendance)) + "%"))
today += 1


def noleave():
    global future_attended, future_delivered, attendance, classes, today, week, date
    print("\n{:^40}".format("Week " + str(week)))
    print("-" * 40)
    print("{:^17} {:^10} {:^12}".format("Date", "Day", "Attendance"))
    print("-" * 40)
    while today < 6:
        future_attended += classes[today-1]
        future_delivered += classes[today-1]
        attendance = future_attended / future_delivered * 100
        printdate()
        print("{:^12}".format(str(math.ceil(attendance)) + "%"))
        if today == 5:
            date += 2
            today = 1
            week += 1
            return
        today += 1


leave = int(input("\nWill you - \n 1. Attend all the classes\n 2. Take leaves\n"))
if leave == 1:
    continuePrinting = True
    while continuePrinting:
        for i in range(5):
            noleave()
        continuePrinting = True if int(input("\nContinue Printing ?\n 1. Yes \n 2. No\n")) == 1 else False

if leave == 2:
    i = today
    p = 'y'
    while p != 's':
        if i > 4:
            week += 1
            print("Week %d" % week)
            i = 0
        p = input("Will you attend %s's class: " % days[i])
        if p == 's':
            break
        if p == 'y':
            future_delivered += classes[i]
            future_attended += classes[i]
            attendance = future_attended / future_delivered * 100
            print("Your attendance will be %d" % math.ceil(attendance))
            i += 1
        else:
            future_delivered += classes[i]
            attendance = future_attended / future_delivered * 100
            print("Your attendance will be %d" % math.ceil(attendance))
            i += 1