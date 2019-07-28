from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Firefox()
browser.get('https://honorcup.ru/auth/?backurl=/quiz/frame/')

login = browser.find_element_by_name('USER_LOGIN')
login.send_keys('nikitkakorepanov2014@yandex.ru')
password = browser.find_element_by_name('USER_PASSWORD')
password.send_keys('simplyclever343')
password.submit()

wait = WebDriverWait(browser, 30).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"frame-default")))

button1 = browser.find_element_by_class_name("about__buttons")
type(button1)

#button = browser.find_elements_by_css_selector(' angular-ripple animate')
#print('Нашел элемент ебать')
#type(button)
