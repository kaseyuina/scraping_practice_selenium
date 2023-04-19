from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

# chrome_path = os.environ.get('chrome_path')
chrome_path = '.\chromedriver'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

# url = 'https://tech-diary.net'
url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(3)

query = 'Dog'
search_box = driver.find_element(By.CLASS_NAME, 'SearchBox__searchInput')
search_box.send_keys(query)
search_box.submit()
sleep(3)

driver.quit()
