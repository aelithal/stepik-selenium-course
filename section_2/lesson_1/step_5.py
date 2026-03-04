from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    x = int(browser.find_element(By.ID, "input_value").text)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(math.log(abs(12*math.sin(x))))
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()