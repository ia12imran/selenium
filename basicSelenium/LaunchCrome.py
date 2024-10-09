import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_path="/usr/bin/chromedriver"
service = Service(chrome_path)
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5)