# pip install pytest-dependancy
import pytest
from selenium import webdriver
import time

path = r"C:\Users\pkhdc\Desktop\chromedriver\chromedriver.exe "
driver = webdriver.Chrome(path)
driver.get("https://demowebshop.tricentis.com/login")
# maximize & minimize
driver.maximize_window()
driver.implicitly_wait(30)
# Loading the image
driver.get_screenshot_as_file("screenshot.png")
@pytest.mark.dependency()
def test_login():
    time.sleep(2)
    driver.find_element("xpath", "//input[@id='Email']").send_keys("Priyankar.sarkar66@gmail.com")
    time.sleep(2)
    driver.find_element("xpath", "//input[@id='Password']").send_keys("PK1234")
    # click Remember_me
    time.sleep(2)
    driver.find_element("xpath", "//input[@id='RememberMe']").click()
    # Loading the image


    # click Login Button
    time.sleep(2)
    driver.find_element("xpath", "//input[@value='Log in']").click()
def test_log_out():
    time.sleep(2)
    driver.find_element("xpath", "//a[@class='ico-logout']").click()
    # Loading the image
    driver.quit()