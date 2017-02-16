

# https://peoplefinder.service.gov.uk/
# https://peoplefinder.service.gov.uk/people/jonathan-roberts1
# https://peoplefinder.service.gov.uk/search?utf8=%E2%9C%93&query=jonathan+roberts&commit=Submit+search



# put in someone's name and either return their site or the search


def pf(name):
	nam = name.split(" ")

	person = "https://peoplefinder.service.gov.uk/people/" + nam[1] + "-"+ nam[2]
	generic = "https://peoplefinder.service.gov.uk/search?utf8=%E2%9C%93&query=" + nam[1] + "+" + nam[2] + "&commit=Submit+search"
#	post = person
	post = nam[1] + "'s page: " + person + ". Or search: " + generic

	return post;




