#!/usr/bin/env python
# coding: utf-8



# dependencies 
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from selenium import webdriver
import time 


def scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    # url of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='list_text').find('div', class_='content_title').text
    news_title

    news_blurb = soup.find('div', class_='article_teaser_body').text
    news_blurb

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(5)

    browser.find_by_id('full_image').click()
    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    img_url = soup.find('div', class_='fancybox-inner').find('img', class_='fancybox-image')['src']

    img = (f'https://www.jpl.nasa.gov{img_url}')

    print(img)

    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', class_='tablepress')
    table

    rows = table.find_all('tr')
    data_column = []
    value_column = []
    for row in rows:
        data = row.find('td', class_='column-1').text
        value = row.find('td', class_='column-2').text
        data_column.append(data)
        value_column.append(value)

    data_column

    value_column

    import pandas as pd


    mars_facts = pd.DataFrame(value_column, index = data_column, columns=['facts'])

    mars_facts

    mars_table = mars_facts.to_html(bold_rows=True)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(5)

    links = browser.links.find_by_partial_text('Hemisphere Enhanced')
    link_len = len(links)

    hemisphere_img_urls = []

    for i in range (0, link_len):
        browser.links.find_by_partial_text('Hemisphere Enhanced')[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find('div', class_='container')
        img_url = result.find('div', id='wide-image').find('img', class_='wide-image')['src']
        url = (f'https://astrogeology.usgs.gov{img_url}')
        title = result.find('div', class_='content').find('section', class_='block metadata').find('h2', class_='title').text
        post = {'title': title,'url': url}
        hemisphere_img_urls.append(post)
        browser.back()

    browser.quit()
    mars_data = {'headline': news_title, 
                'blurb': news_blurb,
                'img_url': img,
                'mars_table': mars_table, 
                'hemisphere_urls': hemisphere_img_urls
                }
    return mars_data




