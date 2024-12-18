from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium testing")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
print("Page title:",driver.title)
driver.quit()
