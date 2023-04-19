from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_path = os.environ.get('chrome_path')

# print(chrome_path)
options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

url = 'https://tech-diary.net'
driver.get(url)

sleep(5)

driver.quit()
