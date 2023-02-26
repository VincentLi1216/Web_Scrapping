import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver = Service("/Users/lishande/Downloads/chromedriver_mac64/chromedriver")

driver = webdriver.Chrome(service=chrome_driver)
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# print(driver.page_source)





def get_titles():
    tags = driver.find_elements(By.CLASS_NAME, "title")
    for tag in tags:
        print(tag.text)

def prev_page():
    link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
    link.click()

def main(times=1):
    for i in range(times):
        get_titles()
        prev_page()

main(10)

time.sleep(5)