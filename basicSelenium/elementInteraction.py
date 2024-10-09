from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.careers360.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search_bar").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Colleges, Exams, Schools & more']").send_keys("LPU")

