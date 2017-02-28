from nltk import metrics, stem, tokenize
from bs4 import BeautifulSoup
import lxml
import requests

url = "https://www.gov.uk/government/organisations/ministry-of-justice/about/statistics"
html = requests.get(url).text
soup = BeautifulSoup(html,'lxml')
allAs = soup.find('h3').findAllNext("a", href = True)

vec = [link.text for link in allAs]
urls = [link["href"] for link in allAs]

stemmer = stem.PorterStemmer()

def fuzzy_match(s1, s2):
    words = tokenize.wordpunct_tokenize(s1.lower().strip())
    l = set()
    for w in words:
        v = stemmer.stem(w)
        for s in s2:
            swords = tokenize.wordpunct_tokenize(s.lower().strip())
            t = [stemmer.stem(sw) for sw in swords]
            if v in t:
                l.add(s)
    return(list(l))

def getlatest(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'lxml')
    res = soup.findAll("h3")
    link = res[1].contents[1].get("href")
    return "http://www.gov.uk" + link

# lets do something
def linker(term):
    f = fuzzy_match(term,vec)
    if len(f) == 1:
        url = urls[vec.index(f[0])]
        response = getlatest(url)
        # slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
    else:
        s = "Did you mean:\n"
        for w in f:
            s += "<" + urls[vec.index(w)] + "|" + w + ">" + "\n"
        response = s
        # slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
    return(response)
