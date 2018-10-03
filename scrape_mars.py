 # Dependencies
import os
import pandas as pd
import requests
from splinter import Browser
from selenium import webdriver
import time
import pymongo
from bs4 import BeautifulSoup as bs
# Import Twitter API keys
from api_key import consumer_key,consumer_secret,access_token,access_token_secret

# Defining 'scrape' function
def scrape():

    print("MISSION TO MARS WEBSCRAPING - STARTING")
    print("----------------------------------")

    # Create Empty Main Mars dictionary
    mars_dict = {}

    # NASA Mars News

    # Mars News URL
    url = "https://mars.nasa.gov/news/"

    # Retrieve url with request
    html = requests.get(url)

    # Create BeautifulSoup object
    soup = bs(html.text, 'html.parser')

    # Get title & description
    news_title = soup.find('div', 'content_title', 'a').text
    news_p = soup.find('div', 'rollover_description_inner').text

    # Adding Mars News entry into Main Mars dictionary
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p

    print("MARS NEWS INFO ACQUIRED")
    print("----------------------------------")

# JPL Mars Space Images

    # JPL Mars URL
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # Create splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    browser.visit(url)

    # Select pages
    time.sleep(2) 
    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(2)
    browser.click_link_by_partial_text("more info")
    time.sleep(2)

    # BeautifulSoup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # Retreive most recent full image from JPL Mars URL
    results = soup.find('article')
    extension = results.find('figure', 'lede').a['href']
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension
    
    # Adding JPL Image entry into Main Mars dictionary
    mars_dict["featured_image_url"] = featured_image_url

    print("FEATURED IMAGE ACQUIRED")
    print("----------------------------------")

    # Mars Weather
    # Pulling recent Mars Weather tweet from twitter
    url_weather = "https://twitter.com/marswxreport?lang=en"
    weather_response = requests.get(url_weather)
    weather_soup = bs(weather_response.text, "html.parser")

    weather_result = weather_soup.find('div', class_='js-tweet-text-container')
    mars_weather = weather_result.find('p', class_='js-tweet-text').text

    mars_dict["mars_weather"] = mars_weather

    print("WEATHER INFO ACQUIRED")
    print("----------------------------------")

  # Mars Facts

    # Mars facts website
    facts_url = "https://space-facts.com/mars/"

    facts_request = requests.get(facts_url)
    soup = bs(facts_request.content,'lxml')
    FactsTable = soup.find_all('table')[0] 
    MarsFacts = pd.read_html(str(FactsTable))

    # Create pandas dataframe
    dataframe = MarsFacts [0]
    dataframe.columns = ["Description", "Value"]

    dataframe.set_index("Description", inplace=True)
    MarsFacts_df = dataframe

    # Convert pandas dataframe to html
    HTMLMars = MarsFacts_df.to_html()
    HTMLMars.replace('\n', '')
    MarsFacts_df.to_html('HTML_Facts.html')

    # Adding to dictionary
    mars_dict["HTMLMars"] = HTMLMars

    print("FACTS DATA ACQUIRED")
    print("-----------------------------")

    # Mars Hemispheres

    print("MARS HEMISPHERES DATA INFO STARTING")
    print("-----------------------------------------------")

    # Mars Hemispheres URL 
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Empty image url list
    mars_hemisphere_urls = []

    # Cerebus Hemisphere

    # Create splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Select pages
    time.sleep(2)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(2)

    # Create BeautifulSoup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    cerberus_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": cerberus_link
    }

    # Append dictionary
    mars_hemisphere_urls.append(cerberus)

    # Schiaparelli Hemisphere
    # Create splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Select pages
    time.sleep(2)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(2)

    # Create BeautifulSoup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    schiaparelli_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": schiaparelli_link
    }

    # Append dictionary
    mars_hemisphere_urls.append(schiaparelli)

    # Syrtis Major Hemisphere
    # Create splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Select pages
    time.sleep(2)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(2)

    # Create BeautifulSoup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    syrtis_major_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    syrtis_major = {
        "title": "Syrtis Major Hemisphere",
        "img_url": syrtis_major_link
    }

    # Append dictionary
    mars_hemisphere_urls.append(syrtis_major)

    # Valles Marineris Hemisphere
    # Create splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Select pages
    time.sleep(2)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(2)

    # Create BeautifulSoup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    valles_marineris_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_marineris_link
    }

    # Append dictionary
    mars_hemisphere_urls.append(valles_marineris)

    mars_dict["mars_hemisphere_urls"] = mars_hemisphere_urls
    
    print("MARS HEMISPHERE DATA INFO ACQUIRED")
    print("----------------------------------")
    print("MISSON TO MARS WEBSCRAPING - COMPLETED")

    return mars_dict