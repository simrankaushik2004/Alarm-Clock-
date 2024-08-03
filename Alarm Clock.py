import os
import datetime
import time


try:
    year,month,date = map(int,input("enter the year,date,month:YYYY:MM:DD").split("/"))
    hour,minute,second=map(int,input("enter the hour, minute and time:HH:MM:SS").split(":"))

except valueerror:
    print("invalid YYYY:MM:DD")
    exit(1)


schedule=datetime.datetime(year,month,date,hour,minute,second)
print(schedule)

while True:
    now = datetime.datetime.now()
    if now >=schedule:
        try:
            os.startfile("C:\\Users\\simra\\Downloads\\alarm-clock-short-6402.mp3")
        except:
            print("file not found")
        break
    time.sleep(1)

