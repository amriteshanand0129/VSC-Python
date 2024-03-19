hours = 0
minutes = 0
seconds = 0
time = 1
print("Ready")
while time != 0:
    time = int(input())
    m = time // 100
    s = time % 100
    minutes += m
    seconds += s
    if seconds >= 60:
        minutes += 1
        seconds -= 60
    if minutes >= 60:
        hours += 1
        minutes -= 60
print(hours, "hours",  minutes, "minutes", "seconds", seconds)
