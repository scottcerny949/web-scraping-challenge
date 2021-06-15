import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import os
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape():
	# Setup splinter
	executable_path = {'executable_path': ChromeDriverManager().install()}
	browser = Browser('chrome', **executable_path, headless=False)

	# website for articles
	url = 'https://redplanetscience.com/'
	browser.visit(url)

	time.sleep(1)

	html = browser.html
	soup = bs(html, 'html.parser')
	# get title
	results = soup.find('div', class_='content_title')
	news_title = results.text  
	# get paragraph
	results2 = soup.find('div', class_='article_teaser_body')
	news_p = results2.text  

	# website for image
	url2 = 'https://spaceimages-mars.com/'
	browser.visit(url2)
	html2 = browser.html
	soup2 = bs(html2,'html.parser')
	results3 = soup2.find('div', class_='floating_text_area')
	image = results3.find('a')['href']
	featured_image_url = f'{url2}{image}'

	# website for facts
	url3 = 'https://galaxyfacts-mars.com/'
	browser.visit(url3)
	html3 = browser.html
	soup3 = bs(html3,'html.parser')
	table = pd.read_html(url3)
	facts = table[0]
	facts.columns = ["","Mars","Earth"]
	facts.set_index("", inplace=True)
	facts_html = facts.to_html('facts.html')

	main_url = 'https://marshemispheres.com/'

	# website for mars images cerberus
	url4 = 'https://marshemispheres.com/cerberus.html'
	browser.visit(url4)
	html4 = browser.html
	soup4 = bs(html4,'html.parser')
	cerberus = soup4.find('img', class_="wide-image")['src']
	cerberus_image_url = f'{main_url}{cerberus}'
	cerberus_title = soup4.find('h2', class_="title")
	cerberus_title2 = cerberus_title.text

	# website for mars images schiaparelli
	url5 = 'https://marshemispheres.com/schiaparelli.html'
	browser.visit(url5)
	html5 = browser.html
	soup5 = bs(html5,'html.parser')
	schiaparelli = soup5.find('img', class_="wide-image")['src']
	schiaparelli_image_url = f'{main_url}{schiaparelli}'
	schiaparelli_title = soup5.find('h2', class_="title")
	schiaparelli_title2 = schiaparelli_title.text

	# website for mars images syrtis
	url6 = 'https://marshemispheres.com/syrtis.html'
	browser.visit(url6)
	html6 = browser.html
	soup6 = bs(html6,'html.parser')
	syrtis = soup6.find('img', class_="wide-image")['src']
	syrtis_image_url = f'{main_url}{syrtis}'
	syrtis_title = soup6.find('h2', class_="title")
	syrtis_title2 = syrtis_title.text

	# website for mars images valles
	url7 = 'https://marshemispheres.com/valles.html'
	browser.visit(url7)
	html7 = browser.html
	soup7 = bs(html7,'html.parser')
	valles = soup7.find('img', class_="wide-image")['src']
	valles_image_url = f'{main_url}{valles}'
	valles_title = soup7.find('h2', class_="title")
	valles_title2 = valles_title.text

	# create dictionary
	hemisphere_image_urls = [
    {"title": cerberus_title2, "img_url": cerberus_image_url},
    {"title": schiaparelli_title2, "img_url": schiaparelli_image_url},
    {"title": syrtis_title2, "img_url": syrtis_image_url},
    {"title": valles_title2, "img_url": valles_image_url}
	]

	# Close the browser after scraping
    browser.quit()

    # Return results
    return mars_scrape
