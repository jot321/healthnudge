import logging
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup

all_links = []
all_headings = set()

START_PAGE = 1
END_PAGE = 58

def get_data(page=None):

    if(page == None):
        link = 'https://www.bewell.com/blog/health/'
    else:
        link = 'https://www.bewell.com/blog/health/page/' + str(page)

    res = requests.get(link)

    soup = BeautifulSoup(res.content, 'html.parser')
    return soup

def getAlllinks(data):
    links = data.find_all('a')
    return links

def filterLinks(links):
    links = filter(lambda x: ( "blog" in str(x) 
                                        and "page" not in str(x) 
                                        and not x.has_attr('rel')
                                        and x.has_attr('title')
                            ), links)
    return links

def getBlogLinks():
    global all_links
    global all_headings

    for page_number in range(START_PAGE, END_PAGE):
        print "Scarpping Page No : " + str(page_number)
        html = get_data(page=page_number)

        links = getAlllinks(html)
        links = filterLinks(links)

        for link in links:
            all_headings.add(link.get('title')) 