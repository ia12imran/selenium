import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_path="/usr/bin/chromedriver"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.careers360.com/")
driver.maximize_window()  # Maximize the window:
# driver.minimize_window()   # Minimize the window:
# driver.refresh()  # Refresh the page:
currentURL = driver.current_url
print(currentURL)
page_title=driver.title
print(page_title)
page_source = driver.page_source
print(page_source)
driver.close()   #  Close the current window:
