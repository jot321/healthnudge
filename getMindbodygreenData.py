import logging
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup

all_links = []
all_headings = []

START_PAGE = 1
END_PAGE = 75

def get_data(page=None):

    res = requests.get('https://www.mindbodygreen.com/health/page/' + str(page))

    soup = BeautifulSoup(res.content, 'html.parser')
    return soup

def getAlllinks(data):
    return data.find_all('a')

def filter(tag):
    return tag.has_attr('title')

def getBlogLinks():
    global all_links
    global all_headings

    for page_number in range(START_PAGE, END_PAGE):
        print "Loading mindbodygreen page number - " + str(page_number)
        html = get_data(page=page_number)
        div_html = html.find_all('h2', attrs={"class": "search-result__heading"})

        links = []
        for link in div_html:
            links.append(link.find('a'))

        for link in links:
            all_links.append(link.get('href'))
            all_headings.append(link.text)

#getBlogLinks()
#print all_headings