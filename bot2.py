from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Firefox()
browser.get('https://quiz.honorcup.ru/app/?id=31514&sign=5ffe6ebb52f21ea4eb18fb1dab50f028')

knopka = browser.find_element_by_class_name('about__buttons')
knopka.click()