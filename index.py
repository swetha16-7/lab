import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
html_file_path = os.path.abspath("C:/Users/M SWETHA/OneDrive/Desktop/sexp6/index.html")
driver=webdriver.Chrome()
driver.get(f"file:///{html_file_path}")
driver.find_element(By.ID,"num1").send_keys("5")
driver.find_element(By.ID,"num2").send_keys("10")
driver.find_element(By.XPATH,"//button").click()
time.sleep(5)
result_text=driver.find_element(By.ID,"result").text
assert result_text=="Sum:15",f"Test failed:Expected 'Sum:15' but got '{result_text}'"
print("Test Passed")
driver.quit()