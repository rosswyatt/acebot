# https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/591009/prison-population-10-february-2017.xls
# https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/589346/prison-population-3-february-2017.xls

import xlrd as x, datetime
from time import strftime

# time.strftime("%A, %d %B %Y ")

# def link():
# 	data = lastFriday(int(time.strftime("%j")),int(time.strftime("%w")))


def lastFriday():
	y = int(strftime("%w"))
	x = int(strftime("%j")) 
	y = -((y+2)%7)
	x += y
	year = int(strftime("%Y"))
	return (datetime.datetime(year, 1, 1) + datetime.timedelta(x-1)).strftime("%d %B %Y");