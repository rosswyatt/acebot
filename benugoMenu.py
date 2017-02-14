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


