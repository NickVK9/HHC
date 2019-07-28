from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Firefox()
browser.get('https://quiz.honorcup.ru/app/?id=31514&sign=5ffe6ebb52f21ea4eb18fb1dab50f028')

time.sleep(5)

knopka_srazhats = browser.find_element_by_class_name('about__buttons')
knopka_srazhats.click()

time.sleep(10)

slider = browser.find_elements_by_class_name('slider__item')
slider[2].click()

knopka_ai = browser.find_elements_by_class_name('profile__theme')
knopka_ai[1].click()

knopka_pt = browser.find_element_by_xpath('/html/body/app/div[1]/nomination/div/div/div[2]/div[3]/div[2]/div/div/div[2]/div')
knopka_pt.click()

#game__question-text найти текст вопроса 

