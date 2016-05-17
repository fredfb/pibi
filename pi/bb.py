from bs4 import BeautifulSoup as bs
import requests


sitio = 'https://www.bible.com/pt/bible/129/jhn.1.nvi'
page = requests.get(sitio)
soup = bs(page.text)

book = soup.find_all('div', 'book')
links = soup.find_all(attrs={"data-book":True})
links[1].attrs

#debug FUNCTIONS
def ea (arquivo, source):
    import os
    os.chdir('c:\\pi')
    with open(arquivo,'a', encoding='utf-8') as f:
        for stuff in source:
            f.write(str(stuff))
            
def loop (source):
    for stuff in source:
        print(stuff)
        print('---')