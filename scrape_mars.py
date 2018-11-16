from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #list urls
    titlep_url = 'https://mars.nasa.gov/news/'
    featured_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    mars_facts_url = 'http://space-facts.com/mars/'
    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    syrtis_major_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    valles_marineris_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    browser.visit(titlep_url)

    time.sleep(2)

    titlep_html = browser.html 
    soup = BeautifulSoup(titlep_html, 'html.parser')

    news_title = soup.find('div', class_='content_title').get_text()
    news_p = soup.find('div', class_='article_teaser_body').get_text()

    browser.visit(featured_url)

    time.sleep(2)

    featured_html = browser.html 
    soup = BeautifulSoup(featured_html, 'html.parser')

    featured_image = soup.find('article')['style']
    featured_image = featured_image.split("('")[1]
    featured_image = featured_image.split("')")[0]
    featured_image = featured_image.split("spaceimages")[1]
    featured_image_url = featured_url.split("/?")[0] + featured_image

    browser.visit(mars_weather_url)

    time.sleep(2)

    mars_weather_html = browser.html
    soup = BeautifulSoup(mars_weather_html, 'html.parser')

    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').get_text()

    browser.visit(mars_facts_url)

    time.sleep(2)

    facts_html = browser.html
    soup = BeautifulSoup(facts_html, 'html.parser')

    facts_table = soup.find('table', id='tablepress-mars')
    
    left_col_facts = facts_table.find_all('strong')
    col_one_facts = []
    for x in left_col_facts:
        col_one_facts.append(x.text)
    
    right_col_facts = facts_table.find_all('td', class_='column-2')
    col_two_facts = []
    for y in right_col_facts:
        col_two_facts.append(y.text)
    
    full_facts_table = dict(zip(col_one_facts, col_two_facts))

    hemisphere_image_urls = []

    browser.visit(cerberus_url)

    time.sleep(2)

    cerberus_html = browser.html
    soup = BeautifulSoup(cerberus_html, 'html.parser')

    cerberus_img_url = soup.find('div', class_='downloads')
    cerberus_img_url = cerberus_img_url.find('li')
    cerberus_img_url = cerberus_img_url.find('a')['href']

    cerberus_title = soup.find('h2', class_='title').get_text()
    cerberus_title = cerberus_title.split(' ')[0]+" "+cerberus_title.split(' ')[1]

    cerberus = {'title': cerberus_title, 'img_url': cerberus_img_url}
    hemisphere_image_urls.append(cerberus)

    browser.visit(schiaparelli_url)

    time.sleep(2)

    schiaparelli_html = browser.html
    soup = BeautifulSoup(schiaparelli_html, 'html.parser')

    schiaparelli_img_url = soup.find('div', class_='downloads')
    schiaparelli_img_url = schiaparelli_img_url.find('li')
    schiaparelli_img_url = schiaparelli_img_url.find('a')['href']

    schiaparelli_title = soup.find('h2', class_='title').get_text()
    schiaparelli_title = schiaparelli_title.split(' ')[0]+" "+schiaparelli_title.split(' ')[1]

    schiaparelli = {'title': schiaparelli_title, 'img_url': schiaparelli_img_url}
    hemisphere_image_urls.append(schiaparelli)

    browser.visit(syrtis_major_url)

    time.sleep(2)

    syrtis_major_html = browser.html
    soup = BeautifulSoup(syrtis_major_html, 'html.parser')

    syrtis_major_img_url = soup.find('div', class_='downloads')
    syrtis_major_img_url = syrtis_major_img_url.find('li')
    syrtis_major_img_url = syrtis_major_img_url.find('a')['href']

    syrtis_major_title = soup.find('h2', class_='title').get_text()
    syrtis_major_title = syrtis_major_title.split(' ')[0]+" "+syrtis_major_title.split(' ')[1]

    syrtis_major = {'title': syrtis_major_title, 'img_url': syrtis_major_img_url}
    hemisphere_image_urls.append(syrtis_major)

    browser.visit(valles_marineris_url)

    time.sleep(2)

    valles_marineris_html = browser.html
    soup = BeautifulSoup(valles_marineris_html, 'html.parser')

    valles_marineris_img_url = soup.find('div', class_='downloads')
    valles_marineris_img_url = valles_marineris_img_url.find('li')
    valles_marineris_img_url = valles_marineris_img_url.find('a')['href']

    valles_marineris_title = soup.find('h2', class_='title').get_text()
    valles_marineris_title = valles_marineris_title.split(' ')[0]+" "+valles_marineris_title.split(' ')[1]

    valles_marineris = {'title': valles_marineris_title, 'img_url': valles_marineris_img_url}
    hemisphere_image_urls.append(valles_marineris)

    mars_data = {
        'news_title': news_title,
        'news_paragraph': news_p,
        'featured_image': featured_image_url,
        'mars_weather': mars_weather,
        'mars_facts': full_facts_table,
        'hemisphere_image_urls': hemisphere_image_urls
    }

    browser.quit()

    return mars_data