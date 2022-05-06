# /usr/bin/env python2.6
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from time import sleep

4
from tqdm import tqdm

myUser = "login"  # define login
myPassword = "password"  # define password

urls = list()


def getDriver(headless=True):
    if headless:
        options = FirefoxOptions()
        options.add_argument("--headless")
        return webdriver.Firefox(options=options)
    return webdriver.Firefox()


driver = getDriver(headless=False)
# driver.maximize_window()
driver.get('https://login.aliexpress.ru/')
sleep(5)
# Login
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "fm-login-id")))
element = driver.find_element(By.ID, 'fm-login-id')
element.send_keys(myUser)
element = driver.find_element(By.ID, 'fm-login-password')
element.send_keys(myPassword)
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div[3]/div/button").click()
driver.switch_to.default_content()
sleep(5)

for i in tqdm(range(1, 51, 1)):  # 50 pages for wishlist
    driver.get(
        'https://my.aliexpress.com/wishlist/wish_list_product_list.htm?&currentGroupId=0&page=' + str(
            i))  # you may set group id for u wishlist
    links = driver.find_elements(By.XPATH, (
        '/html/body/div[4]/div[2]/div/div[2]/div[2]/ul/li[@class="product sold-out util-clearfix js-product"]/div['
        '2]/p/a'))

    for a in links:
        print(links)
        #        print(title.text)
        urls.append(a.get_attribute("href"))

for u in tqdm(urls):
    print(u)
    driver.get(u)
