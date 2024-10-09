import time
from ast import Bytes
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_path="/usr/bin/chromedriver"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.careers360.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login")))
element.click()
driver.find_element(By.CSS_SELECTOR,"#name_focus").send_keys("Dummy Users")
driver.find_element(By.CSS_SELECTOR,"#emailInput").send_keys("Dummyuser@yopmial.com")
driver.find_element(By.CSS_SELECTOR,"input[name='mobile']").send_keys("9876787678")
driver.find_element(By.CSS_SELECTOR,".css-lagbch").click()
# dropdown = select(studying_dropdown)
# dropdown.select
time.sleep(10)
