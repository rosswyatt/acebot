
import datetime
from bs4 import BeautifulSoup
import urllib
import sys



def TrainTimes(origin,destination,time_input="09:00",day="today"):
	# if time is set to now, make time equal to nearest 15 min
	if time_input == "now":
		tm = datetime.datetime.now()
		tm = tm - datetime.timedelta(minutes=tm.minute % 15,
	                             seconds=tm.second,
	                             microseconds=tm.microsecond)
		tm = str(tm)
		time_input = tm
	# otherwise, take input and set it to the nearest 15 min
	else:
		tm = datetime.datetime.strptime(time_input,"%H:%M")
		tm = tm - datetime.timedelta(minutes=tm.minute % 15,
	                             seconds=tm.second,
	                             microseconds=tm.microsecond)
		tm = str(tm)
		tm = tm[11:16]
	
	# create url	
	url= "http://traintimes.org.uk/"+origin+"/"+destination+"/"+time_input+"/"+day

	# pull the page, if error, try the origin with London prefix
	try:
		page = urllib.request.urlopen(url).read()
	except(urllib.error.HTTPError):
		origin = "London " + origin
		url= "http://traintimes.org.uk/"+origin+"/"+destination+"/"+time_input+"/"+day
		page = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	# get first 5 trains
	journeys = []
	for i in range(0,5):
		for_time = soup.find(id="result%s" % i)
		journey_time = for_time.strong.text
		late = for_time.find_all('a', class_="status late")
		late_list = [l.text for l in late]
		try:
			journeys.append(journey_time + " " + late_list[0])
		except(IndexError):
			journeys.append(journey_time + " On time")
	return journeys

def CallTrainTimes(command):
	command_list = command.split()
	
	command_list.remove("traintimes")

	if len(command_list) == 4:
		results = TrainTimes(command_list[0],command_list[1],command_list[2],command_list[3])
	if len(command_list) == 3:
		results = TrainTimes(command_list[0],command_list[1],command_list[2])
	elif len(command_list) == 2:
		results = TrainTimes(command_list[0],command_list[1])
	for response in results:

		slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
	sys.exit()
