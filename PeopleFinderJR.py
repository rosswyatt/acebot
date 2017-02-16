

# https://peoplefinder.service.gov.uk/
# https://peoplefinder.service.gov.uk/people/jonathan-roberts1
# https://peoplefinder.service.gov.uk/search?utf8=%E2%9C%93&query=jonathan+roberts&commit=Submit+search



# put in someone's name and either return their site or the search


def pf(name):
	
	n = name.split(" ")
	nam = [""]*max(len(n),3)
	nam[0:len(n)] = n

	person = "https://peoplefinder.service.gov.uk/people/" + nam[1].lower() + "-"+ nam[2].lower()

	generic_nam = ""
	for i in nam[1:]:
		generic_nam	+= i + "+"

	generic = "https://peoplefinder.service.gov.uk/search?utf8=%E2%9C%93&query=" + generic_nam[:-1] + "&commit=Submit+search"
#	post = person
	post = nam[1] + "'s page should be here: " + person + " If not, search for them here: " + generic

	return post;




