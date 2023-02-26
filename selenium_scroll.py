import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver = Service("/Users/lishande/Downloads/chromedriver_mac64/chromedriver")

driver = webdriver.Chrome(service=chrome_driver)
url = "https://www.linkedin.com/jobs/jobs-in-台北?countryRedirected=1&position=1&pageNum=0"
driver.get(url)


def scroll_window():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

job_count = 0
def main(times = 10):
    global job_count
    for i in range(times):
        scroll_window()
    # time.sleep(3)
    title_tags = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
    for title_tag in title_tags:
        job_count += 1
        print(title_tag.text)

main(10)
print(f'{job_count} jobs found')
time.sleep(5)
# print(driver.page_source)
