from webbrowser import open_new_tab
from random import choice
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_song_list():
    '''Return the top 100 songs from Apple's iTunes charts.'''
    URL = 'http://www.apple.com/itunes/charts/songs/'
    soup = BeautifulSoup(urlopen(URL).read(), "lxml")
    titles = (sp.a.string.encode('ascii', 'ignore') for sp in soup('h3')[:99]
              if len(sp('a')) == 1)
    artists = (sp.a.string.encode('ascii', 'ignore') for sp in soup('h4')[:99]
               if len(sp('a')) == 1)
    return ['{0} {1}'.format(a, t) for a, t in zip(artists, titles)]

def play_song(search_term):
    '''Create song link for YouTube.'''
    Temp = "{0}".format(search_term)
    Temp = Temp.replace("b'", "")
    Temp = Temp.replace("'", "")
    Temp = Temp.replace(" ", "%20")

    URL = "https://duckduckgo.com/?q=!ducky+" + Temp + "+site%3Ayoutube.com"

    return URL

def song_url():
    songs = get_song_list()
    return play_song(choice(songs))