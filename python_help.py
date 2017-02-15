#http://lmgtfy.com/?q=python+loop

def pyHelp(x):
	splt = x.split(" ")
	query = ""
	for i in splt:
		query += i + "+"
	return "http://lmgtfy.com/?q=" + query[:-1];
	
