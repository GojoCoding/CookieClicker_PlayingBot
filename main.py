import os
import random
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# ChromeDriver is what connects Selenium to Chrome
chromeDriverPath = os.environ.get('chromeDriverPath')
chrome_options = Options()
# Keeps browser open
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

duration = 10
end_time = time.time() + duration
while time.time() < end_time:
    pass

cookiesAccept = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
cookiesAccept.click()

languageSelect = driver.find_element(By.ID, "langSelect-EN")
languageSelect.click()

# Clicking Cookie Button
cookieButton = driver.find_element(By.ID, "bigCookie")

while True:
    cookieButton.click()
    cookieAmt = driver.find_element(By.CSS_SELECTOR, "#sectionLeft #cookies ")
    cookieAmt = int(cookieAmt.text.split()[0])
    # orderedProductPrices = driver.find_elements(By.CSS_SELECTOR, "#sectionRight #products .price")
    # intPrices = [int(price.text) for price in orderedProductPrices]

    try:
        orderedProductPrices = driver.find_elements(By.CSS_SELECTOR, "#sectionRight #products .price")
        intPrices = [int(price.text) for price in orderedProductPrices]
        orderedProducts = driver.find_elements(By.CSS_SELECTOR, "#sectionRight #products "
                                                                ".unlocked.enabled .content .productName")
        for oP in orderedProducts:
            print(oP.text)
        # Product Selection
        i = 0
        for price in intPrices:
            if cookieAmt >= price:
                i = intPrices.index(price)
        orderedProducts[i].click()
    except NoSuchElementException:
        time.sleep(1)
    # rand = random.uniform(1, 2)
    # if rand == 1:
    # Product Selection
    # for Productp in orderedProductPrices:
    #     if cookieAmt >= int(Productp):
    #         i = orderedProductPrices.index(Productp)
    # orderedProducts[i].click()
    # else:
    #     # Upgrade Selection
    #     for Prodpi in orderedProductPrices:
    #         if cookieAmt >= int(Prodpi):
    #             i = orderedProductPrices.index(Prodpi)
    #     orderedProducts[i].click()
    time.sleep(1)
