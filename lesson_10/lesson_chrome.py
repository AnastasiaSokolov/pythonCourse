from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(executable_path='D:\github\pythonCourse\lesson_10\selenium\chromedriver.exe'))
driver.get('http://itcareer.pythonanywhere.com')

web_form = driver.find_element(By.CLASS_NAME, "form-group")
print(web_form.get_attribute('innerHTML'))

name_field = driver.find_element(By.ID, 'name')
name_field.send_keys('Inna')

surname_field = driver.find_element(By.ID, 'surname')
surname_field.send_keys('Didnt')

email_field = driver.find_element(By.ID, 'email')
email_field.send_keys('inn_did@gmail.com')

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('12345qwert')

time.sleep(3)
driver.close()