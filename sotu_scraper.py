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


def get_transcript_links(url):
	'''
	Given a page, return data structue of years and corresponding link to address
	'''
	url_dict = {
		'year':[],
		'url':[]
	}
	soup = get_soup(url)
	for td in soup.find_all('td', {'align':'center', 'class':'ver12'}):
		for a in td.find_all('a', href=True):
			if len(a.text) == 4:
				if int(a.text) > 1936:
					url_dict['year'].append(a.text)
					url_dict['url'].append(a['href'])

	return pd.DataFrame(url_dict).sort_values(by='year', ascending=False)