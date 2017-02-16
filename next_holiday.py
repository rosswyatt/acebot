
import urllib.request
from icalendar import Calendar,Event 
from datetime import date

def nh():
    today=date.today()
    urllib.request.urlretrieve("https://www.gov.uk/bank-holidays/england-and-wales.ics","bhcal.ics")
    g=open('bhcal.ics')
    gcal=Calendar.from_ical(g.read())
    g.close()
    holiday_dates=[]
    holiday_descriptions=[]

    for event in gcal.walk('vevent'):
        holiday_dates.append(event['dtstart'].dt)    
        holiday_descriptions.append(event['summary'])

    past_hol=1
    i=0
    while past_hol==1:
        if holiday_dates[i] > today:
            answer="%s, %s %s %s (%s)"%(holiday_dates[i].strftime("%A"),holiday_dates[i].strftime("%B"),holiday_dates[i].day,holiday_dates[i].year,holiday_descriptions[i])
            past_hol=0
        elif i>len(holiday_dates)-1:
            answer="No future holidays!"
            past_hol=0
        else:
            i=i+1
    return answer

        