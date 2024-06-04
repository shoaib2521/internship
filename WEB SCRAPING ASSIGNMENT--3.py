#!/usr/bin/env python
# coding: utf-8

# #    WEB-SCRAPING ASSIGNMENT--3

# QUESTION--1

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

product = input("Enter the product to be searched: ")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(product)
search_box.send_keys(Keys.RETURN)

time.sleep(3)


# QUESTION--2

# In[4]:


product_details = []

def scrape_page():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    for product in products:
        try:
            brand = product.find('span', class_='a-size-base-plus a-color-base').text.strip()
        except AttributeError:
            brand = "-"
        
        try:
            name = product.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
        except AttributeError:
            name = "-"
        
        try:
            price = product.find('span', class_='a-price-whole').text.strip()
        except AttributeError:
            price = "-"
        
        try:
            product_url = "https://www.amazon.in" + product.find('a', class_='a-link-normal a-text-normal')['href']
        except TypeError:
            product_url = "-"
        
        try:
            product_page = product_url
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(product_page)
            time.sleep(3)
            
            soup_product = BeautifulSoup(driver.page_source, 'html.parser')
            try:
                return_exchange = soup_product.find('div', id='returnsPolicy').text.strip()
            except AttributeError:
                return_exchange = "-"
            
            try:
                delivery = soup_product.find('div', id='ddmDeliveryMessage').text.strip()
            except AttributeError:
                delivery = "-"
            
            try:
                availability = soup_product.find('div', id='availability').find('span').text.strip()
            except AttributeError:
                availability = "-"
            
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception:
            return_exchange, delivery, availability = "-", "-", "-"
        
        product_details.append({
            "Brand Name": brand,
            "Name of the Product": name,
            "Price": price,
            "Return/Exchange": return_exchange,
            "Expected Delivery": delivery,
            "Availability": availability,
            "Product URL": product_url
        })

for _ in range(3):
    scrape_page()
    try:
        next_page = driver.find_element(By.CLASS_NAME, 's-pagination-next')
        next_page.click()
        time.sleep(3)
    except Exception:
        break

driver.quit()

df = pd.DataFrame(product_details)
df.to_csv(f"{product}_details.csv", index=False)

print(f"Data saved to {product}_details.csv")


# QUESTION--3

# In[7]:


import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

keywords = ['fruits', 'cars', 'Machine Learning', 'Guitar', 'Cakes']
num_images = 10

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

def download_image(url, folder_name, num):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder_name, f"image_{num}.jpg"), 'wb') as file:
                file.write(response.content)
    except Exception as e:
        print(f"Could not download image {num}: {e}")

def search_and_download_images(keyword):
    # Create a folder for the keyword
    folder_name = keyword.replace(" ", "_")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    driver.get('https://images.google.com')
    
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.clear()
    search_bar.send_keys(keyword)
    search_bar.send_keys(Keys.RETURN)

    time.sleep(2)

    for _ in range(2):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(2)

    image_elements = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i')
    urls = []
    for image in image_elements:
        try:
            image.click()
            time.sleep(1)
            large_image = driver.find_element(By.CSS_SELECTOR, 'img.n3VNCb')
            url = large_image.get_attribute('src')
            if url and url.startswith('http'):
                urls.append(url)
            if len(urls) >= num_images:
                break
        except Exception as e:
            print(f"Error finding image URL: {e}")

    for i, url in enumerate(urls):
        download_image(url, folder_name, i + 1)

for keyword in keywords:
    search_and_download_images(keyword)

driver.quit()


# QUESTION---4

# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_smartphone_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    details = []
    results = soup.find_all('div', class_='_1AtVbE')

    for result in results:
        try:
            brand = result.find('div', class_='_4rR01T').text
        except AttributeError:
            brand = '-'

        try:
            name = result.find('a', class_='IRpwTa').text
        except AttributeError:
            name = '-'

        try:
            color = result.find('a', class_='_1uWtKd').text
        except AttributeError:
            color = '-'

        try:
            ram = result.find_all('li', class_='rgWa7D')[0].text
        except IndexError:
            ram = '-'

        try:
            rom = result.find_all('li', class_='rgWa7D')[1].text
        except IndexError:
            rom = '-'

        try:
            primary_camera = result.find_all('li', class_='rgWa7D')[2].text
        except IndexError:
            primary_camera = '-'

        try:
            secondary_camera = result.find_all('li', class_='rgWa7D')[3].text
        except IndexError:
            secondary_camera = '-'

        try:
            display_size = result.find_all('li', class_='rgWa7D')[4].text
        except IndexError:
            display_size = '-'

        try:
            battery_capacity = result.find_all('li', class_='rgWa7D')[5].text
        except IndexError:
            battery_capacity = '-'

        try:
            price = result.find('div', class_='_30jeq3 _1_WHN1').text
        except AttributeError:
            price = '-'

        try:
            product_url = 'https://www.flipkart.com' + result.find('a', class_='IRpwTa')['href']
        except AttributeError:
            product_url = '-'

        details.append({
            'Brand': brand,
            'Name': name,
            'Color': color,
            'RAM': ram,
            'ROM': rom,
            'Primary Camera': primary_camera,
            'Secondary Camera': secondary_camera,
            'Display Size': display_size,
            'Battery Capacity': battery_capacity,
            'Price': price,
            'Product URL': product_url
        })

    return details

def main():
    search_query = input("Enter the smartphone you want to search for: ")
    search_query = search_query.replace(' ', '+')
    url = f'https://www.flipkart.com/search?q={search_query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'

    details = get_smartphone_details(url)
    df = pd.DataFrame(details)
    df.to_csv('smartphone_details.csv', index=False)

    print("Scraping and saving complete.")

if __name__ == "__main__":
    main()


# QUESTION--5

# In[9]:


import requests

def get_coordinates(city):
    api_key = 'AIzaSyBLtFfF-evzexggUkHY50vZvOlsl0Vgbc'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={api_key}'

    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        print("Error: Unable to retrieve coordinates.")

def main():
    city = input("Enter the city name: ")
    coordinates = get_coordinates(city)
    if coordinates:
        latitude, longitude = coordinates
        print(f"Coordinates of {city}: Latitude = {latitude}, Longitude = {longitude}")

if __name__ == "__main__":
    main()


# QUESTION---6

# In[10]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_laptop_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    laptops = []
    results = soup.find_all('div', class_='right-container')

    for result in results:
        name = result.find('div', class_='heading-wraper').text.strip()
        specs = result.find_all('div', class_='value')

        specs_dict = {}
        for spec in specs:
            key = spec.find_previous('div', class_='heading').text.strip()
            value = spec.text.strip()
            specs_dict[key] = value
            
        laptops.append({
            'Name': name,
            **specs_dict
        })

    return laptops

def main():
    url = 'https://www.digit.in/top-products/best-gaming-laptops-40.html'
    laptops = get_laptop_details(url)
    df = pd.DataFrame(laptops)
    df.to_csv('gaming_laptops_details.csv', index=False)

    print("Scraping and saving complete.")

if __name__ == "__main__":
    main()


# QUESTION---7

# In[16]:


import requests
from bs4 import BeautifulSoup

def get_billionaires_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    billionaires = []
    results = soup.find_all('div', class_='person')

    for result in results:
        rank = result.find('div', class_='rank').text.strip()
        name = result.find('div', class_='name').text.strip()
        net_worth = result.find('div', class_='networth').text.strip()
        age = result.find('div', class_='age').text.strip()
        citizenship = result.find('div', class_='countryOfCitizenship').text.strip()
        source = result.find('div', class_='source').text.strip()
        industry = result.find('div', class_='category').text.strip()

        billionaires.append({
            'Rank': rank,
            'Name': name,
            'Net Worth': net_worth,
            'Age': age,
            'Citizenship': citizenship,
            'Source': source,
            'Industry': industry
        })

    return billionaires

def main():
    url = 'https://www.forbes.com/billionaires/'
    billionaires = get_billionaires_details(url)
    for billionaire in billionaires:
        print(billionaire)
        print()

    print("Scraping complete.")

if __name__ == "__main__":
    main()


# QUESTION---8

# //

# QUESTION---9

# //

# In[17]:


import requests
from bs4 import BeautifulSoup

def scrape_hostels(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    hostels = []
    results = soup.find_all('div', class_='fabresult')

    for result in results:
        name = result.find('h2', class_='title').text.strip()
        distance = result.find('span', class_='description').text.strip()
        rating = result.find('span', class_='rating').text.strip()
        total_reviews = result.find('div', class_='reviews').text.strip().split()[0]
        overall_reviews = result.find('div', class_='score').text.strip()
        privates_from_price = result.find('span', class_='price').text.strip().split()[0]
        dorms_from_price = result.find('div', class_='dormfromprice').text.strip().split()[0]
        facilities = ', '.join([item.text.strip() for item in result.find_all('span', class_='facilities')])
        description = result.find('p', class_='extended').text.strip()

        hostels.append({
            'Name': name,
            'Distance from City Centre': distance,
            'Rating': rating,
            'Total Reviews': total_reviews,
            'Overall Reviews': overall_reviews,
            'Privates From Price': privates_from_price,
            'Dorms From Price': dorms_from_price,
            'Facilities': facilities,
            'Description': description
        })

    return hostels

def main():
    url = 'https://www.hostelworld.com/hostels/London'
    hostels = scrape_hostels(url)

    for hostel in hostels:
        print(hostel)
        print()

if __name__ == "__main__":
    main()


# In[ ]:




