import Stock

print("Enter time in hours and minutes")
hour = int(input("Hour: "))
minute = int(input("Minutes: "))


def calc_angle():
    # Function to Calculate angle b/w hour hand and minute hand
    global hour
    global minute

    # Validate the input
    if hour < 0 or minute < 0 or hour > 24 or minute > 60 or (hour == 24 and minute != 0):
        print('Wrong input')
        return
    if minute == 60:
        minute = 0
        hour += 1

    #  Checking for ante/post meridian
    if hour == 12 and minute == 0:
        meridian = "noon"
    elif hour == 24:
        meridian = "midnight"
    elif hour < 12:
        meridian = "AM"
    else:
        meridian = "PM"

    #  Changing 24-hour format into 12-hour format
    if hour > 12:
        hour = hour % 12

    # Calculate the angles moved by hour and minute hand with reference to 12:00
    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute

    # Find the difference between two angles
    hands_angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two
    hands_angle = min(360 - hands_angle, hands_angle)
    hands_angle = str(hands_angle) + chr(176)
    time = "%02d : %02d %s" % (hour, minute, meridian)
    print("Time is:", time)
    print("Angle between hour and minute hand: ", hands_angle)
    display_clock(hour_angle, minute_angle, time, hands_angle)


def display_clock(hour_angle, minute_angle, time, angle):
    #  Drawing the outer circle of clock
    turtle.width(3)
    turtle.circle(100)

    #  Printing the numbers 1 to 12 in circular manner
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 180)
    for i in range(1, 13):
        for j in range(15):
            turtle.right(2)
            turtle.forward(3)
        turtle.backward(3)
        turtle.write(i)
        turtle.forward(3)

    turtle.goto(0, 100)
    turtle.pendown()
    turtle.width(3)
    turtle.circle(2)

    #  Drawing the hour hand
    turtle.pendown()
    turtle.setheading(90)
    turtle.right(hour_angle)
    turtle.forward(50)
    turtle.backward(50)

    #  Drawing the minute hand
    turtle.setheading(90)
    turtle.right(minute_angle)
    turtle.forward(70)
    turtle.penup()

    #  Printing the time and angle data
    turtle.goto(-85, -100)
    turtle.width(5)
    turtle.write(time, font=("Verdana", 30, "normal"))
    turtle.goto(-185, -150)
    turtle.write(("Angle between hands: " + str(angle)), font=("Verdana", 19, "normal"))

    #  Drawing rectangle around the clock
    turtle.goto(-200, -160)
    turtle.pendown()
    turtle.setheading(0.0)
    for i in range(2):
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
    turtle.exitonclick()


#  Calling the calc_angle function
calc_angle()
