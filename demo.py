#################For Registration###########

from selenium import webdriver
import time

path = r"C:\Users\pkhdc\Desktop\chromedriver\chromedriver.exe "
driver = webdriver.Chrome(path)

url = "https://demowebshop.tricentis.com/"
driver.get(url)
# maximize & minimize
driver.maximize_window()
# click Registrar
time.sleep(2)
driver.find_element("xpath", "//a[@class='ico-register']").click()
# click Gender
time.sleep(2)
driver.find_element("id", "gender-male").click()
# click F_name
time.sleep(2)
driver.find_element("id", "FirstName").send_keys("Priyankar")
# click L_name
time.sleep(2)
driver.find_element("id", "LastName").send_keys("Sarkar")
# click Email
time.sleep(2)
driver.find_element("id", "Email").send_keys("Priyankar.sarkar66@gmail.com")

# click Password
time.sleep(2)
driver.find_element("id", "Password").send_keys("PK1234")
time.sleep(2)
driver.find_element("id", "ConfirmPassword").send_keys("PK1234")


# click Register Button
time.sleep(2)
driver.find_element("xpath", "//input[@id='register-button']").click()
