from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome('C:/Users/AMIT/Downloads/chromedriver')
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)

target= ' " " '

string =""

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"]'
print("hi")
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
print(input_box)
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)

