import time, sys, os

seconds = 0
minutes = 0
hours = 0

clear = lambda: os.system('cls')

def chronometer():
    global seconds
    global minutes
    global hours
    
    seconds += 1
    if (seconds == 60):
        seconds = 0
        minutes += 1
        if (minutes == 60):
            minutes = 0
            hours += 1
    
    clear()
    if (seconds < 10):
        strSeconds = '0' + str(seconds)    
    else:
        strSeconds = str(seconds)
    if (minutes < 10):
        strMinutes = '0' + str(minutes)
    else:
        strMinutes = str(minutes)
    if(hours < 10):
        strHours = '0' + str(hours)
    else:
        strHours = str(hours)
    print(strHours + ':' + strMinutes + ':' + strSeconds)

run = True

while (run):
    time.sleep(1)
    chronometer()
