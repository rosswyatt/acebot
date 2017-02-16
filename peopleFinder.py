#https://peoplefinder.service.gov.uk/people/andrew-poulton
def pf(name):	
	nam = name.split(" ")
	if nam[0]=="pf":
		post = "https://peoplefinder.service.gov.uk/people/" + nam[1] + "-" + nam[2]
	else:
		query = ""
		for i in nam[1:]:
			query += i + "+"
		post = r"https://peoplefinder.service.gov.uk/search?utf8=%E2%9C%93&query=" + query[:-1] + "Submit+search"
	return post;


#r"https://peoplefinder.service.gov.uk/search?utf8=%E2%9C%93&query=102+petty+france&commit=Submit+search"