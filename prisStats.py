# https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/591009/prison-population-10-february-2017.xls
# https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/589346/prison-population-3-february-2017.xls

import xlrd, datetime, urllib.request
from bs4 import BeautifulSoup
from time import strftime
import requests, re


# time.strftime("%A, %d %B %Y ")

# def link():
# 	data = lastFriday(int(time.strftime("%j")),int(time.strftime("%w")))
# def sayTheAnswer():
# 	k=link()
# 	slack_client.api_call("chat.postMessage", channel=channel, text="Total prisoners: " + str(k[0]+k[1]), as_user=True)
# 	slack_client.api_call("chat.postMessage", channel=channel, text="Male prisoners: " + str(k[0]), as_user=True)
# 	slack_client.api_call("chat.postMessage", channel=channel, text="Female prisoners: " + str(k[1]), as_user=True)
# 	return "";

def link(wk, findWeek):
	Date=lastFriday(wk).replace(" ","-")
	t=Date.lower()
	if t[0] == "0":
		t = t[1:]
	r = []
	for i in ['2015', '2016', '2017']:
		e=requests.get("https://www.gov.uk/government/statistics/prison-population-figures-"+i)
		e=BeautifulSoup(e.text, "lxml")
		e=e.findAll(class_ = "title")
		for lk in e:
			w=lk.find("a")["href"]
			r.append(w)
	try:
		l=[i for i in r if (t in i)][0]
	except:
		return "Oh dear.  I suspect there's something gone wrong with the ridiculous way files are named on gov.uk";
	link = "https://www.gov.uk" + l

	urllib.request.urlretrieve(link, "prisPop.xls")
	bk=xlrd.open_workbook("prisPop.xls")
	sh = sh=bk.sheet_by_index(0)
	for j in range(sh.ncols):
		for i in range(sh.nrows):
			if sh.cell(i,j).value == "Male population":
				mp = int(sh.cell(i,j+1).value)
				fp = int(sh.cell(i+1,j+1).value)
				break
	return [mp,fp, Date, findWeek, wk];

def handleResponse(y):
	x=0
	findWeek = True
	digiFind = re.search("\d", y.lower())
	dateFind = re.search("\d{1,2}\/\d{1,2}(\/\d{2,4})?|\d{1,2}([a-z]{2})? \w{1,20}( \d{2,4})?",y.lower())
	if len(y) > len("prison population"):
		findWeek = False
	if digiFind:
		x = int(digiFind.group(0))
		findWeek = True
	elif "1"in y.lower()  or "one" in y.lower() or "last" in y.lower():
		x = 1
		findWeek = True
	elif "2" in y.lower() or "two" in y.lower():
		x = 2
		findWeek = True
	elif "3" in y.lower() or "three" in y.lower():
		x=3
		findWeek = True
	elif "4" in y.lower() or "four" in y.lower():
		x=4
		findWeek = True
	if "month" in y.lower():
		x=x*4
		findWeek = True
	if "year" in y.lower():
		x=x*52
		findWeek = True
	print(x)
	return link(x,findWeek)




def lastFriday(wk =0):
	y = int(strftime("%w"))
	x = int(strftime("%j")) 
	y = -((y+2)%7)-wk*7
	x += y
	year = int(strftime("%Y"))
	return (datetime.datetime(year, 1, 1) + datetime.timedelta(x-1)).strftime("%d %B %Y");