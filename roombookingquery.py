import webbrowser  
import time
import datetime

def roombooking(date="", attendees="",length=""):

	today = datetime.date.today()
	thismonday = today - datetime.timedelta(days=today.weekday())
	thissunday = thismonday + datetime.timedelta(days=6)
	tomorrow = today + datetime.timedelta(days=1)
	nextmonday = thismonday + datetime.timedelta(days=7)
	nextsunday = thissunday + datetime.timedelta(days=7)

	startdate=today
	enddate=today
	mystery=1

	if date.lower()=="now":
		startdate=0
	elif date.lower()=="today":
		startdate=today
		mystery=3
	elif date.lower()=="tomorrow":
		startdate=tomorrow
		mystery=3
	elif date.lower()=="thisweek":
		startdate=thismonday
		mystery=3
	elif date.lower()=="nextweek":
		startdate=nextmonday
		mystery=3
	else:
		startdate=0

	if date.lower()=="now":
		enddate=0
	elif date.lower()=="today":
		enddate=today
		mystery=3
	elif date.lower()=="tomorrow":
		enddate=tomorrow
		mystery=3
	elif date.lower()=="thisweek":
		enddate=thissunday
		mystery=3
	elif date.lower()=="nextweek":
		enddate=nextsunday
		mystery=3
	else:
		enddate=0

	if date.lower() in ["today","tomorrow","thisweek","nextweek"]:
		start = datetime.datetime(startdate.year, startdate.month, startdate.day,0,0,0,0)
		start_time = int(time.mktime(start.timetuple()))*1000
		end = datetime.datetime(enddate.year, enddate.month, enddate.day,23,59,59,999)
		end_time = int(time.mktime(end.timetuple()))*1000
	else:
		start_time=0
		end_time=0

	webbrowser.open("https://app.matrixbooking.com/ui/#/find/rooms/results/{s}/{e}/{l}/{a}/718321/{m}/0/0".format(s=start_time, e=end_time, a=attendees, l =length, m=mystery), new=2, autoraise=True)

	message = "Your search will open in a new window"

	return message

def roomcleaning(command):
		command_list = command.split()
		command_list.remove("book")
		command_list.remove("a")
		command_list.remove("room")

		if len(command_list) == 3:
			results = roombooking(command_list[0],command_list[1],command_list[2])
		elif len(command_list) == 2:
			results = roombooking(command_list[0],command_list[1],0)
		elif len(command_list) == 1:
			results = roombooking(command_list[0],"","")
		elif len(command_list) == 0:
			results = roombooking("","","")

		return results
