#!/usr/bin/env python
# coding: utf-8

# # Assignment for WebScraping BeautifulSoup Evaluation 

# 1---answer

# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/list/ls056092300/"

response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
movie_containers =soup.find_all("div", class_="lister-item-content")

names = []
ratings = []
years = []

for container in movie_containers:
    name = container.find("a").text.strip()
    names.append(name)
    
    rating = container.find("span",class_="ipl-rating-star__rating").text.strip()
    ratings.append(rating)
    
    year = container.find("span",class_="lister-item-year").text.strip("()")
    years.append(year)
    
df = pd.DataFrame({
        "Name": names,
        "rating": ratings,
        "year of release": years
    })

print(df)


# In[ ]:





# answer--4

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get("https://www.patreon.com/coreyms")
page


# In[4]:


soup = BeautifulSoup(page.content)
soup


# In[5]:


date = soup.find('div',class_="sc-lgu5zg-0 dXpjXs")
date


# In[ ]:





# 5---answer

# In[6]:


from bs4 import BeautifulSoup
import requests


# In[7]:


url = "https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn0seyJsYXQiOjEyLjk3ODM2OTIsImxvbiI6NzcuNjQwODM1NiwicGxhY2VJZCI6IkNoSUprUU4zR0tRV3Jqc1JOaEJRSnJoR0Q3VSIsInBsYWNlTmFtZSI6IkluZGlyYW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Jayanagar,Rajajinagar,Indiranagar"
page = requests.get(url)


# In[8]:


soup = BeautifulSoup(page.content, "html.parser")
house_containers = soup.find_all("div", class_="card")

house_titles = []
locations = []
areas = []
emis = []
prices = []

for container in house_containers:
    
        title = container.find("h2", class_="heading-6 font-semi-bold nb__1AShY").text.strip()
        house_titles.append(title)
        location = container.find("div", class_="nb__2CMjv").text.strip()
        locations.append(location)
        area = container.find("div", class_="nb__3oNyC").text.strip()
        areas.append(area)
        emi = container.find("div", class_="font-semi-bold heading-6").text.strip()
        emis.append(emi)
        price = container.find("div", class_="heading-7").text.strip()
        prices.append(price)
    
for i in range(len(house_titles)):
    print("House Title:", house_titles[i])
    print("Location:", locations[i])
    print("Area:", areas[i])
    print("EMI:", emis[i])
    print("Price:", prices[i])
    print()
    


# In[ ]:




answer---6
# In[9]:


import requests
from bs4 import BeautifulSoup

url = "https://www.bewakoof.com/bestseller?sort=popular"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
product_containers = soup.find_all("div", class_="productCardWrapper_0")

product_names = []
product_prices = []
image_urls = []


for container in product_containers[:10]:
    product_name = container.find("h3", class_="name_3WzT").text.strip()
    product_names.append(product_name)

    product_price = container.find("span", class_="price_dhyC").text.strip()
    product_prices.append(product_price)

    image_url = container.find("img", class_="image_1KfY")["src"]
    image_urls.append(image_url)

num_products = min(10, len(product_names)) 
for i in range(num_products):
    print("Product Name:", product_names[i])
    print("Product Price:", product_prices[i])
    print("Image URL:", image_urls[i])
    print()


# In[ ]:





# answer--7

# In[10]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
article_containers = soup.find_all("div", class_="Card-titleContainer")

headings = []
dates = []
links = []

for container in article_containers:
    heading = container.find("a").text.strip()
    headings.append(heading)
    
    date = container.find("div", class_="Card-time").text.strip()
    dates.append(date)
    
    link = "https://www.cnbc.com" + container.find("a")["href"]
    links.append(link)

for i in range(len(headings)):
    print("Heading:", headings[i])
    print("Date:", dates[i])
    print("News Link:", links[i])
    print()


# In[ ]:





# answer--8

# In[ ]:


import requests
from bs4 import BeautifulSoup

url = "https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
article_containers = soup.find_all("div", class_="aia-article")

titles = []
dates = []
authors = []

for container in article_containers:
    title = container.find("h3", class_="aia-article-title").text.strip()
    titles.append(title)
    
    date = container.find("div", class_="aia-article-date").text.strip()
    dates.append(date)
    
    author = container.find("div", class_="aia-article-authors").text.strip()
    authors.append(author)

for i in range(len(titles)):
    print("Paper Title:", titles[i])
    print("Date:", dates[i])
    print("Author:", authors[i])
    print()

    


# In[ ]:




