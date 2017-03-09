
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import re


def TrainTimes(origin,destination,time_input="now",day="today"):
	# if time is set to now, make time equal to nearest 15 min
	if time_input == "now":
		tm = datetime.datetime.now()
		tm = tm + datetime.timedelta(minutes=tm.minute % 15,
	                             seconds=tm.second,
	                             microseconds=tm.microsecond)
		tm = str(tm)
		tm = tm[11:16]
		tm = tm.replace(":", "")
		time_input = tm
		
	# otherwise, take input and set it to the nearest 15 min
	else:
		tm = datetime.datetime.strptime(time_input,"%H:%M")
		tm = tm + datetime.timedelta(minutes=tm.minute % 15,
	                             seconds=tm.second,
	                             microseconds=tm.microsecond)
		tm = str(tm)
		tm = tm[11:16]
		tm = tm.replace(":", "")
		time_input = tm
	# create url	
	url= "http://ojp.nationalrail.co.uk/service/timesandfares/"+origin+"/"+destination+"/"+day+"/"+time_input+"/dep"

	# pull the page, if error, try the origin with London prefix
	page = urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	Origins = []
	for hit in soup.findAll(attrs={'class' : 'from'}):
		if hit.text != "From" and hit.text != '':
			d = re.sub('\s+', ' ', hit.text)
			d = re.sub(r'\[[A-Z]{3}\]','', d)
			Origins.append(d)

	Destinations = []
	for hit in soup.findAll(attrs={'class' : 'to'}):
		if hit.text != "To" and hit.text != '':
			d = re.sub('\s+', ' ', hit.text)
			d = re.sub(r'\[[A-Z]{3}\]','', d)
			Destinations.append(d)

	Departs = []
	for hit in soup.findAll(attrs={'class' : 'dep'}):
		if hit.text != "Dep.":
			d = re.sub('\s+', ' ', hit.text)
			Departs.append(d)

	Arrives = []
	for hit in soup.findAll(attrs={'class' : 'arr'}):
		if hit.text != "Arr.":
			d = re.sub('\s+', ' ', hit.text)
			Arrives.append(d)

	Duration = []
	for d,a in zip(Departs[1:6], Arrives[1:6]):
		Duration.append("Duration: %s" % str(datetime.datetime.strptime(a,"%H:%M") - datetime.datetime.strptime(d,"%H:%M")))
	
	Delay = []
	for hit in soup.findAll(attrs={'class' : 'journey-status'}):
		d = re.sub('\s+', ' ', hit.text)
		d = re.sub('Alternative trains', '', d)
		Delay.append("Status: %s" % d)

	Fares = []
	for hit in soup.findAll(attrs={'class' : 'opsingle'}):
		d = re.sub('\s+', ' ', hit.text)
		Fares.append("Fare: %s" % d)

	Changes = []
	for hit in soup.findAll(attrs={'class' : 'chg'}):
		if hit.text != "Chg.":
			d = re.sub('\s+', ' ', hit.text)
			Changes.append("Changes: %s" % d)

	SendToAceBot = []
	for ori, des, dep, arr, dur, dela, pri, chg in zip(Origins, Destinations, Departs, Arrives,Duration, Delay, Fares, Changes):
		SendToAceBot.append(ori + ' ' + des + ' ' + dep + ' ' + arr)
		SendToAceBot.append(dur + ' ' + dela + ' ' + pri + ' ' + chg)
	return SendToAceBot
	'''
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
	'''
def CallTrainTimes(command):
	command_list = command.split()
	
	command_list.remove("traintimes")

	if len(command_list) == 4:
		results = TrainTimes(command_list[0],command_list[1],command_list[2],command_list[3])
	elif len(command_list) == 3:
		results = TrainTimes(command_list[0],command_list[1],command_list[2])
	elif len(command_list) == 2:
		results = TrainTimes(command_list[0],command_list[1])
	return results

#x = CallTrainTimes("traintimes London Derby")
#print(x)



