import logging
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup

all_links = []
all_headings = []

def get_data(page=None):

    if(page == None):
        link = 'http://www.healthifyme.com/blog/'
    else:
        link = 'http://www.healthifyme.com/blog/page/' + str(page)

    print(link)
    res = requests.get(link)

    soup = BeautifulSoup(res.content, 'html.parser')
    return soup

def getAlllinks(data):
    return data.find_all('a')

def filterLinks(links):
    return filter(lambda x: "blog" in links)

def getBlogLinks():
    global all_links
    global all_headings

    for page_number in range(2,3):
        html = get_data(page=page_number)

        links = getAlllinks(html)
        links = filterLinks(links)

        for link in links:
            print("\n")
            print link

            
            if (link.has_attr('title')):
                all_links.append(link.get('href'))
                all_headings.append(link.get('title'))

getBlogLinks()