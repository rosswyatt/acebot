
import datetime
import mechanicalsoup
from bs4 import BeautifulSoup
import urllib
from lxml import html




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
	print(url)

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
			journeys.append(journey_time)
	return journeys

journey = TrainTimes("Victoria","Brighton",time_input="15:15")

print(journey)