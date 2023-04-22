from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd
import requests

query = input('Please input search keyword: ')

chrome_path = '.\chromedriver'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(2)

search_box = driver.find_element(By.CLASS_NAME, 'SearchBox__searchInput')
search_box.send_keys(query)
search_box.submit()
sleep(3)

height = 1000
while height < 3000:
    driver.execute_script("window.scrollTo(0, {});".format(height))
    height += 100

    sleep(1)

# Select images
elements = driver. find_elements(By.CLASS_NAME, ('sw-Thumbnail'))

d_list = []
for i, element in enumerate(elements, start=1):
    name = f'{query}_{i}'
    # print(name)
    raw_url = element.find_element(By.CLASS_NAME, 'sw-ThumbnailGrid__details').get_attribute('href')
    yahoo_image_url = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
    title = element.find_element(By.TAG_NAME, 'img').get_attribute('alt')

    d = {
        'filename': name,
        'raw_url': raw_url,
        'yahoo_image_url': yahoo_image_url,
        'title': title
    }
    d_list.append(d)

df = pd.DataFrame(d_list)
df.to_csv('image_urls_20230420.csv')

driver.quit()

IMAGE_DIR = '.\\' + query + '\\'
if os.path.isdir(IMAGE_DIR):
    print('Already exists')
else:
    os.makedirs(IMAGE_DIR)

df = pd.read_csv('image_urls_20230420.csv')
for file_name, yahoo_image_url in zip(df.filename, df.yahoo_image_url):
    image = requests.get(yahoo_image_url)
    with open(IMAGE_DIR + file_name + '.jpg', 'wb') as f:
        f.write(image.content)
    
    sleep(1)
    