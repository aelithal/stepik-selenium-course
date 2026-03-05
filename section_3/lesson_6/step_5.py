
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


class TestClass():
    @pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_1(self, number):
        browser = webdriver.Chrome()
        url = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(url)
        browser.implicitly_wait(20)
        link = browser.find_element(By.ID, "ember500")
        browser.execute_script("arguments[0].click();", link)
        email_input = browser.find_element(By.ID, "id_login_email")
        email_input.send_keys("ooleg.mal@gmail.com")
        password_input = browser.find_element(By.ID, "id_login_password")
        password_input.send_keys("&W6T9.8XK_hCW)#")
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        time.sleep(5)
        text_area = browser.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea")
        answer = math.log(int(time.time()))
        text_area.send_keys(answer)
        time.sleep(10)
        browser.quit()
