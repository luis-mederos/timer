import subprocess
import time
import datetime
time.gmtime(0)
def greating():
    print ("this is a pomodoro timer for ever 25 minutes")
    print ("    you work you get a 5 miute break")
    print ("       you will get a long break every 4 shorts breaks")






def work_time():
    hours = int(input("how many hours are you going to study for?"))
    minutes = int (input("how many minutes are you going to study for?"))
    mins = hours * 60 + minutes
    print (hours,"this is how many hours you will work")
    print (mins,"this is how many minutes you will work")
    global seconds
    seconds = mins * 60 
    print (seconds,"this is how many seconds you will work")
    input("press enter to start!")

def timer():
    break_time = 0
    long_break = 0
    global seconds
    for count in range(seconds):
        if break_time == 1500:
            print ("take a 5 minute break")
            time.sleep(300)
            break_time = 0
            long_break = long_break+1
        elif long_break == 4:
            print ("take a long 30 minute break")
            time.sleep(1800)
            long_break = 0
        else:
            print (seconds)
            time.sleep(1)
            seconds = seconds - 1
            break_time = break_time+1
        

work_time()
timer()