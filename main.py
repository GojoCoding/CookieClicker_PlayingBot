from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# ChromeDriver is what connects Selenium to Chrome
chromeDriverPath = "/Users/mig/Development/chromedriver_mac_arm64/chromedriver"
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
orderedProductPrices = driver.find_elements(By.CSS_SELECTOR,)
orderedProducts = driver.find_elements(By.CSS_SELECTOR,)

while True:
    cookieButton.click()
    i = 0
    for Prodpi in orderedProductPrices:
        if cookieAmt >= int(Prodpi):
            i = orderedProductPrices.index(Prodpi)
    orderedProducts[i]
    try:
        cursor = driver.find_elements(By.CSS_SELECTOR, "#sectionRight #products .unlocked.enabled")
        cursor.click()
    except NoSuchElementException:
        time.sleep(1)
    time.sleep(1)
