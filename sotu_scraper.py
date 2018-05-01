################
# sotu scraper #
################


import bs4 
import requests
import csv
import pandas as pd
import re
import os
from urllib.request import urlretrieve
from urllib.parse import urlparse


def get_soup(url):
    '''
    Gets soup for a url
    '''
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'lxml')
    return soup


def scrape_committees(url):
    '''
    Returns list of urls to committee pages
    '''
    url_dict = {
        'committee_name':[],
        'committee_id':[],
        'committee_url':[]
    }
    soup = get_soup(url)        
    for table in soup.find_all('div', {'class': 'module'}):
        for tag in table.find_all('a', {'class': 'module-title'}):
            l = tag['href'].split('/')
            committee_id = l[4]
            full_link = url+l[4]+'/documents/'
            url_dict['committee_name'].append(tag.text)
            url_dict['committee_id'].append(committee_id)
            url_dict['committee_url'].append(full_link)
    return pd.DataFrame(url_dict)