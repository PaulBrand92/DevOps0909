from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
service = Service("C:/Users/pavelm/Downloads/chromedriver.exe")
my_driver = webdriver.Chrome(service=service)
my_driver.get("file://C:/Users/pavelm/Documents/tip_calc/index.html")
my_driver.find_element(By.ID, "billamt").send_keys("100")
my_driver.find_element(By.XPATH, '//*[@id="serviceQual"]/option[3]').click()
my_driver.find_element(By.ID, "peopleamt").send_keys("5")
my_driver.find_element(By.ID, "musicq").send_keys("5")
my_driver.find_element(By.ID, "calculate").click()
expected ="9.00"
actual = my_driver.find_element(By.ID, "tip").text
if expected == actual:
    print("all good")
sleep(5)
my_driver.close()