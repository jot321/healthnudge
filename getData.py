import logging
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup

all_links = []
all_headings = []

START_PAGE = 1
END_PAGE = 100

def get_data(page=None):

    if(page == None):
        res = requests.get('https://wellnessmama.com/blog')
    else:
        res = requests.get('https://wellnessmama.com/blog/page/' + str(page))

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
        html = get_data(page=page_number)
        div_html = html.find('div', attrs={"class": "content-sidebar-wrap"})

        links = getAlllinks(div_html)

        for link in links:
            if (link.has_attr('title')):
                all_links.append(link.get('href'))
                all_headings.append(link.get('title'))