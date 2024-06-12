#!/usr/bin/env python
# coding: utf-8

# # WEB SCRAPING---ASSIGNMENT-4

# 1---ANSWER

# In[ ]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class": "wikitable"})

rows = table.find_all("tr")[1:] 
for row in rows:
    data = row.find_all("td")
    rank = data[0].text.strip()
    name = data[1].text.strip()
    artist = data[2].text.strip()
    upload_date = data[3].text.strip()
    views = data[4].text.strip()

    print("Rank:", rank)
    print("Name:", name)
    print("Artist:", artist)
    print("Upload Date:", upload_date)
    print("Views:", views)
    print("-------------------------")


# In[ ]:





# ANSWER--2

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.bcci.tv/")

try:
    international_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@data-nav-index='0']/a[@href='/international']"))
    )
    international_link.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "js-list"))
    )

    fixtures = driver.find_elements_by_class_name('js-list-item')
    for fixture in fixtures:
        series = fixture.find_element_by_class_name('fixture__format-strip').text.strip()
        place = fixture.find_element_by_class_name('fixture__description').text.strip()
        date = fixture.find_element_by_class_name('fixture__date').text.strip()
        time = fixture.find_element_by_class_name('fixture__time').text.strip()

        print("Series:", series)
        print("Place:", place)
        print("Date:", date)
        print("Time:", time)
        print("-----------------------------")

except Exception as e:
    print("An error occurred:", e)

finally:

    driver.quit()


# In[ ]:





# ANSWER---3

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://statisticstimes.com/")

try:

    economy_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='navbar']/div/a[contains(@href,'economy')]"))
    )
    economy_link.click()

    gdp_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@style='float:left;background-color:seashell;width:33%;']/ul/li/a[contains(@href,'indian-states-gdp')]"))
    )
    gdp_link.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//table[@id='table_id']/tbody/tr"))
    )
    rows = driver.find_elements_by_xpath("//table[@id='table_id']/tbody/tr")
    for row in rows:
        rank = row.find_element_by_xpath("./td[1]").text
        state = row.find_element_by_xpath("./td[2]").text
        gsdp_18_19_current = row.find_element_by_xpath("./td[3]").text
        gsdp_19_20_current = row.find_element_by_xpath("./td[4]").text
        share_18_19 = row.find_element_by_xpath("./td[5]").text
        gdp_billion = row.find_element_by_xpath("./td[6]").text

        print("Rank:", rank)
        print("State:", state)
        print("GSDP(18-19) - Current Prices:", gsdp_18_19_current)
        print("GSDP(19-20) - Current Prices:", gsdp_19_20_current)
        print("Share(18-19):", share_18_19)
        print("GDP($ billion):", gdp_billion)
        print("-----------------------------")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()


# In[ ]:





# ANSWER---4

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://github.com/")

try:

    explore_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//summary[contains(text(),'Explore')]"))
    )
    explore_menu.click()
    
    trending_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Trending')]"))
    )
    trending_option.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//article[@class='Box-row']"))
    )

    repositories = driver.find_elements_by_xpath("//article[@class='Box-row']")
    for repo in repositories:
        repo_title = repo.find_element_by_xpath(".//h1/a").text.strip()
        repo_description = repo.find_element_by_xpath(".//p").text.strip()
        contributors_count = repo.find_element_by_xpath(".//span[contains(@class,'text-gray')]/a[last()]").text.strip()
        language_used = repo.find_element_by_xpath(".//span[@itemprop='programmingLanguage']").text.strip()

        print("Repository Title:", repo_title)
        print("Repository Description:", repo_description)
        print("Contributors Count:", contributors_count)
        print("Language Used:", language_used)
        print("-----------------------------")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()


# In[ ]:





# ANSWER---5

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.billboard.com/")

try:
    charts_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@class='header__subnav__item']/a[contains(@href,'charts')]"))
    )
    charts_option.click()

    hot_100_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='charts-landing__link charts-landing__video--background']"))
    )
    hot_100_link.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "chart-list__element"))
    )

    songs = driver.find_elements_by_xpath("//li[@class='chart-list__element']")
    for song in songs:
        song_name = song.find_element_by_class_name("chart-element__information__song").text.strip()
        artist_name = song.find_element_by_class_name("chart-element__information__artist").text.strip()
        last_week_rank = song.find_element_by_class_name("chart-element__meta.text--center.color--secondary.text--last").text.strip()
        peak_rank = song.find_element_by_class_name("chart-element__meta.text--center.color--secondary.text--peak").text.strip()
        weeks_on_board = song.find_element_by_class_name("chart-element__meta.text--center.color--secondary.text--week").text.strip()

        print("Song Name:", song_name)
        print("Artist Name:", artist_name)
        print("Last Week Rank:", last_week_rank)
        print("Peak Rank:", peak_rank)
        print("Weeks on Board:", weeks_on_board)
        print("-----------------------------")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()


# In[ ]:





# ANSWER---6

# In[ ]:


import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
    columns = row.find_all("td")
    book_name = columns[0].text.strip()
    author_name = columns[1].text.strip()
    volumes_sold = columns[2].text.strip()
    publisher = columns[3].text.strip()
    genre = columns[4].text.strip()

    print("Book Name:", book_name)
    print("Author Name:", author_name)
    print("Volumes Sold:", volumes_sold)
    print("Publisher:", publisher)
    print("Genre:", genre)
    print("-----------------------------")


# In[ ]:





# ANSWER---7

# In[ ]:


import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls095964455/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

series_container = soup.find("div", class_="lister-list")

series = series_container.find_all("div", class_="lister-item-content")

for serie in series:
    name = serie.find("h3", class_="lister-item-header").a.text.strip()

    year_span = serie.find("span", class_="lister-item-year").text.strip()

    genre = serie.find("span", class_="genre").text.strip()

    run_time = serie.find("span", class_="runtime").text.strip()

    ratings = serie.find("div", class_="ipl-rating-star").strong.text.strip()

    votes = serie.find("span", attrs={"name": "nv"})["data-value"].strip()

    print("Name:", name)
    print("Year Span:", year_span)
    print("Genre:", genre)
    print("Run Time:", run_time)
    print("Ratings:", ratings)
    print("Votes:", votes)
    print("-----------------------------")


# In[ ]:





# ANSWER--8

# In[ ]:


import requests
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

show_all_link = soup.find("a", href="/ml/datasets.php")

if show_all_link:
    show_all_url = url + show_all_link["href"]
    
    show_all_response = requests.get(show_all_url)

    show_all_soup = BeautifulSoup(show_all_response.content, "html.parser")

    table = show_all_soup.find("table", {"border": "1", "cellpadding": "5"})

    if table:
        rows = table.find_all("tr")[1:]  
        for row in rows:
            columns = row.find_all("td")
            dataset_name = columns[0].text.strip()
            data_type = columns[1].text.strip()
            task = columns[2].text.strip()
            attribute_type = columns[3].text.strip()
            instances = columns[4].text.strip()
            attributes = columns[5].text.strip()
            year = columns[6].text.strip()

            print("Dataset Name:", dataset_name)
            print("Data Type:", data_type)
            print("Task:", task)
            print("Attribute Type:", attribute_type)
            print("No of Instances:", instances)
            print("No of Attributes:", attributes)
            print("Year:", year)
            print("-----------------------------")
    else:
        print("Table not found on the 'Show All Dataset' page.")
else:
    print("Link to the 'Show All Dataset' page not found on the homepage.")


# In[ ]:




