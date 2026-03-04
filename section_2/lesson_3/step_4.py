from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.alert.accept()

    x = int(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
    input = browser.find_element(By.XPATH, "//input")
    input.send_keys(math.log(abs(12*math.sin(x))))
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()