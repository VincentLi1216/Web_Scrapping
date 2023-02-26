import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver = Service("/Users/lishande/Downloads/chromedriver_mac64/chromedriver")

driver = webdriver.Chrome(service=chrome_driver)
url = "https://leetcode.com/accounts/login/"
driver.get(url)
# time.sleep(3)
user_name_input = driver.find_element(By.ID, "id_login")
password_input = driver.find_element(By.ID, "id_password")
user_name_input.send_keys("vincentli1216")
password_input.send_keys("sunnus931216\n")
# input()
time.sleep(5)
driver.get("https://leetcode.com/problemset/all/")
time.sleep(3)
statElement = driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]")
print(statElement.text)
time.sleep(3)