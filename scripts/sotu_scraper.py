################
# sotu scraper #
################


import bs4 
import requests
import pandas as pd
import sys


BASE_URL = 'http://www.presidency.ucsb.edu/sou.php'


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


def scrape_sotu_text(df):
	'''
	Take a dataframe of urls and grabs the speech text from that url and its author
	'''
	speech_dict = {
		'president':[],
		'date':[],
		'speech':[]
	}
	for url in df.url:
		soup = get_soup(url)
		pres_name = str(soup.find('meta', {'name':'title'})).split(':')[0].lstrip('<meta content="')
		address_day = str(soup.find('meta', {'name':'title'})).split(':')[1].split(' - ')[1].strip('" name="title"/>')
		content = str(soup.get_text()).split('\nCitation')[0].split('ProjectPromote Your Page Too\n\n\n')[1]

		speech_dict['president'].append(pres_name)
		speech_dict['date'].append(address_day)
		speech_dict['speech'].append(content)

	return pd.DataFrame(speech_dict).sort_values(by='date', ascending=False)


if __name__ == '__main__':
	out_file = open(sys.argv[-1], 'w') if len(sys.argv) > 1 else 'sotu_content.pkl'
	urls_df = get_transcript_links(BASE_URL)
	content_df = scrape_sotu_text(urls_df)
	content_df.to_pickle(out_file)