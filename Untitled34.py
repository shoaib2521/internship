#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-1      WEB SCRAPING

# 1-ANSWER

# In[1]:


import requests
from bs4 import BeautifulSoup

def get_header_tags(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        for header in headers:
            print(header.text.strip())
url = "https://www.wikipedia.org"
get_header_tags(url)


# In[ ]:





# 2-ANSWER

# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_top_100_movies_data(url):
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        movies_list = soup.find('div', class_='lister-list')
        
        names = []
        ratings = []
        years = []
        
        movies = movies_list.find_all('div', class_='lister-item-content')
        
        for movie in movies:
            name = movie.find('h3').a.text.strip()
            rating = movie.find('span', class_='ipl-rating-star__rating').text.strip()
            year = movie.find('span', class_='lister-item-year').text.strip('()')
            
            names.append(name)
            ratings.append(rating)
            years.append(year)
            
        df = pd.DataFrame({'Name': names, 'rating': ratings, 'year of rwlease': years})
        
        return df
    
url = "https://www.imdb.com/list/ls091520106/"
top_100_movies_df = get_top_100_movies_data(url)
print(top_100_movies_df)
        


# In[ ]:





# ANSWER-3

# In[14]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_dineout_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        restaurant_names = []
        cuisines = []
        locations = []
        ratings = []
        image_urls = []

        restaurant_elements = soup.find_all('div', class_='restnt-info')
        for restaurant in restaurant_elements:
            name = restaurant.find('div', class_='restnt-name ellipsis').text.strip()
            restaurant_names.append(name)
            cuisine = restaurant.find('span', class_='double-line-ellipsis').text.strip()
            cuisines.append(cuisine)
            location = restaurant.find('div', class_="restnt-loc ellipsis").text.strip()
            locations.append(location)
            rating = restaurant.find('div', class_='rating-widget').text.strip()
            ratings.append(rating)
            image_url = restaurant.find('div', class_='img-cvr').img['data-src']
            image_urls.append(image_url)
    
        df = pd.DataFrame({
            'Restaurant Name': restaurant_names,
            'Cuisine': cuisines,
            'Location': locations,
            'Ratings': ratings,
            'Image URL': image_urls
        })
        
        return df
    else:
        print("Failed to fetch data:", response.status_code)
        return None

url = "https://www.dineout.co.in/hyderabad"
restaurant_df = scrape_dineout_details(url)

restaurant_df.head()


# In[ ]:





# ANSWER-4

# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_former_finance_ministers(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        names = []
        terms_of_office = []
        rows = soup.find_all('tr')[1:]  
        
        for row in rows:
            cells = row.find_all('td')
            
            name = cells[0].text.strip()
            term_of_office = cells[1].text.strip()
            
            names.append(name)
            terms_of_office.append(term_of_office)
        
        df = pd.DataFrame({'Name': names, 'Term of Office': terms_of_office})
        
        return df
    else:
        print("Failed to fetch data:", response.status_code)
        return None

url = "https://presidentofindia.nic.in/former-presidents"

finance_minister_df = scrape_former_finance_ministers(url)
print(finance_minister_df)


# In[ ]:




