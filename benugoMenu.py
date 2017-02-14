import time, pptx, urllib.request

def menu(day = None):
	if day == None:
		day = time.strftime('%A')
	urllib.request.urlretrieve("https://intranet.justice.gov.uk/documents/2016/02/benugo-weekly-menu.pptx", "bwm1.pptx")
	prs = pptx.Presentation('bwm1.pptx')
	text_runs = []
	for slide in prs.slides:
		for shape in slide.shapes:
			if not shape.has_text_frame:
				continue
			for paragraph in shape.text_frame.paragraphs:
				par = []
				for run in paragraph.runs:
					par.append(run.text.lower())
				text_runs.append(par)
	return text_runs;

def halloumi(eats = 'halloumi'):
	MenU = []
	menU = sum(menu(),[])
	days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
	message = 'Sorry Karik, no ' + eats + ' this week.'
	for st in menU:
		c = st.find(eats)
		if c > -1:
			i = menU.index(st)
			MenU = menU[i::-1]
			break
	if len(MenU)>0:
		#print(MenU)
		dayIndex = []
		for day in days:
			if day in MenU:
				dayIndex.append(MenU.index(day))
				#print(dayIndex)
		day = MenU[min(dayIndex)]
		message = "Praise be! We havin' " + eats + ' ' + day + '.'
	return message;

def menu_search(t):
    '''Search the menu for t, return the days t is in the menu and the menu item'''
    menu_items = []
    day = []
    for i, x in enumerate(menu()):
        if t in ' '.join(x):
            #start at i, search backwards until we find day
            menu_items.append(' '.join(x))
            j = i
            while 'day' not in ' '.join(a[j]):
                j = j-1
            day.append(' '.join(a[j]))
            
    return (day, menu_items)
