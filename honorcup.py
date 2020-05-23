TOKEN = 'https://quiz.honorcup.ru/app/?id=31514&sign=5ffe6ebb52f21ea4eb18fb1dab50f028'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

import numpy as np
import pickle

num = int(input())

while True:
    browser = webdriver.Firefox()
    browser.get(TOKEN)
    print('Открыл браузер')

    def scorer():
        return int(browser.find_element_by_class_name('game__user-value').text)

    def learn(mode):
        if mode == 0:
            path = '/html/body/app/div[1]/nomination/div/div/div[2]/div[3]/div[1]/div/div/div[2]/div'
            sub_path = '/home/nick/pt/GoogleAI/'
        elif mode == 1:
            path = '/html/body/app/div[1]/nomination/div/div/div[2]/div[3]/div[2]/div/div/div[2]/div'
            sub_path = '/home/nick/pt/Python/'
        elif mode == 2:
            path = '/html/body/app/div[1]/nomination/div/div/div[2]/div[3]/div[3]/div/div/div[2]/div'    
            sub_path = '/home/nick/pt/Deep Learning/'
        else:
            path = '/html/body/app/div[1]/nomination/div/div/div[2]/div[3]/div[4]/div/div/div[2]/div'
            sub_path = '/home/nick/pt/TensorFlow/'
        mid = []
        print('Считываю массивы')
        questions = []
        with open(sub_path + 'questions.txt', 'r') as file:
            for line in file:
                questions_current = line[:-1]
                questions.append(questions_current)
        q_answers = []
        with open(sub_path + 'answers.txt', 'r') as file:
            for line in file:
                q_answers_current = line[:-1]
                q_answers.append(q_answers_current)
        print(len(questions) == len(q_answers))
        
        time.sleep(5)

        try:
            battle_button = browser.find_element_by_class_name('about__buttons')
            battle_button.click()
            print('Зашел в викторину')

            time.sleep(2)

            slider = browser.find_elements_by_class_name('slider__item')
            slider[2].click()
            print("Выбрал AI")

            time.sleep(2)

            menu = browser.find_elements_by_class_name('profile__theme')
            menu[mode].click()
            print('Выбрал категорию')

            time.sleep(2)

            play = browser.find_element_by_xpath(path)
            play.click()
            print('Начинаю битву')

            time.sleep(20)

            for game in range(5):
                print('Раунд {}'.format(game+1))

                question = browser.find_element_by_class_name('game__question-text')
                answers = browser.find_elements_by_class_name('game__answer')

                print('Вопрос: {}'.format(question.text))
                for i in answers:
                    print('Нашел ответ: {}'.format(i.text))
                    mid.append(i.text)

                if question.text in questions:
                    print("Вопрос есть в базе")
                    q_index = questions.index(question.text)
                    index = int(mid.index(q_answers[q_index]))
                    print('Ответ:', index)
                    time.sleep(0.3)
                    answers[index].click()
                else:                
                    game_score = scorer()
                    print("Вопроса в базе нет") 
                    rand_index = np.random.randint(0, 4)
                    print('Кликаю наугад')
                    print('Кликнул', answers[rand_index].text)
                    answers[rand_index].click()
                    time.sleep(1)
                    game_score_after_q = scorer()
                    if game_score_after_q > game_score:
                        print('Ответ верен, добавляю в базу')
                        questions.append(question.text)
                        q_answers.append(answers[rand_index].text)
                    else:
                        print('Ответ неверный')
                mid.clear()
                time.sleep(40)
            time.sleep(5)

            print('Перезаписываю массивы')
            with open(sub_path + 'questions.txt', 'w') as file:
                for item in questions:
                    file.write('%s\n' % item)
            
            with open(sub_path + 'answers.txt', 'w') as file:
                for item in q_answers:
                    file.write('%s\n' % item)
            print('Выхожу из браузера')
            browser.quit()
        except:
            print("Все крашнулось")
            time.sleep(5)
            print('Перезаписываю массивы')
            with open(sub_path + 'questions.txt', 'w') as file:
                for item in questions:
                    file.write('%s\n' % item)
            
            with open(sub_path + 'answers.txt', 'w') as file:
                for item in q_answers:
                    file.write('%s\n' % item)
            print('Выхожу из браузера')
            browser.quit()
    learn(num)


print('Я тестирую гитхаб')