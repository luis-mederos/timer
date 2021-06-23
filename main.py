import SystemEvents
import subprocess
import time
import datetime

study_break = 0

long_break = 0 

hours = int(input("how many hours are you going to study"))
print (hours,"this is how many hours you will work")

mins = hours * 60
print (mins,"this is how many minutes you will work")
seconds = mins * 60 
print (seconds,"this is how many seconds you will work")

while mins>0:
    if study_break == 4:
        print ("take long break break")
        study_break = 0
    elif mins == mins-25:
        print ("take a 5 minutes")
        study_break = study_break+1


    


