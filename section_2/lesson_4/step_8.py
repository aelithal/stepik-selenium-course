from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.XPATH, "//button[@id='book']")
    price = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100")
    )
    button.click()

    x = int(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
    input = browser.find_element(By.XPATH, "//input")
    input.send_keys(math.log(abs(12*math.sin(x))))
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(300)
    browser.quit()