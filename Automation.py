from Notification import notify
import csv
import datetime, time

fileName = 'Events.csv'
dateHit = datetime.datetime.today() + datetime.timedelta(days=1)

with open(fileName, newline='') as f:
    reader=csv.reader(f)
    data = list(reader)

data.pop(0)

for x in data:
    eventDate = x[0].split('-')
    #print(eventDate)
    eventDay = eventDate[0].lstrip("0")
    eventMonth = eventDate[1].lstrip("0")
    eventYear = int(eventDate[2])

    if(eventDay==str(dateHit.day) and eventMonth==str(dateHit.month) and eventYear<=int(dateHit.year)):
        notify(x[1]+" alert!",x[2]+"'s "+x[1]+" tomorrow")
        #print(x[1]+" alert!",x[2]+"'s "+x[1]+" tomorrow")
        time.sleep(7)

#print(str(dateHit.day))
#print(str(dateHit.month))