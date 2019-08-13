from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def huawei():
    Ask = ["Каким будет вывод функции print('xY!2'.swapcase())?", "Какой режим доступа используется для открытия файла только для записи?", "Что такое кортеж?", "Какой из следующих операторов не является оператором Python?", 'Каков вывод функции "test"+1+2+3?', "Какое из следующих утверждений о Vim неверно?", "Функция () удаляет кэш регулярных выражений и не принимает аргументы.", "Какой из следующих модулей используется для получения информации об ОС?", "Какое выражение используется для повторения блока кода определенное количество раз?", "Ключевые слова в Python - это зарезервированные слова, которые нельзя использовать в качестве константы, переменной или любого другого идентификатора. Какое слово не является ключевым в Python?", 'Какой формат словаря некорректен?', "Мы можем использовать () для считывания двух символов из проекта файла hfile.", "Какой вывод будет при применении формата к строке?", "Кто является создателем языка Python?", "Какая команда используется для добавления нового элемента в список?", "Какое утверждение о регулярных выражениях в Python неверно?", "Какое свойство ООП позволяет смешивать разные классы и добавлять к другим классам для расширения функциональности и повторного использования кода?", "Когда list1 - [388, 38, 3883,838], каково значение list1[-1]?", "Какая функция используется для проверки того, являются ли все символы в строке цифрами?", "У какой из операций самый высокий приоритет?", "Какая команда используется для запуска Python в Windows?", "Какой режим доступа используется, чтобы открыть файл для добавления в двоичном формате?", 'Каким будет результат действия "test".replace("t","s")?', "Какое свойство ООП можно использовать для создания аналогичного класса с другими функциями?", 'Когда d = {"mary":30, "ann":25}, какая команда используется для получения количества записей в словаре?', "Функция () может использоваться для поиска времени по UTC, если модуль datetime уже был импортирован.", 'Какой из примеров ниже является примером создания кортежа?', "Какой результат будет получен при выполнении математической операции 50 % 4 в Python?", "Какой режим доступа используется для записи и чтения файла в двоичном формате?", "Какой символ используется для обозначения неравенства в Python?", "Какой арифметический оператор нельзя использовать со строками?", "Какое утверждение о кортеже верно?"]
    Answ = ["Xy!2", "w", "Упорядоченное множество элементов, доступ к которым осуществляется с помощью указания индекса. Когда элементы определены, их нельзя изменить.", "Оператор вывода", 'Ошибка', "Vim обеспечивает корректную работу только на локальных серверах, но не на удаленных серверах", "re.purge()", "sys.platform", "for", "eval", '{1,"X",2"Y"}', "hfile.read(2)", "str", "Гвидо ван Россум", "list.append(obj)", "Регулярные выражения re могут обрабатывать только строковые данные, но не числовые данные.", "Композиция (Composition)", "838", "isdigit()", "Скобка", "python", "ab", 'sess', "Наследование (Derivation)", 'len(d)', "datetime.datetime.utcnow()", 'group_A = ("M", "N", "O", "P")', "2", "wb+", "!=", "-", "Кортежи не изменяются."]
    Mid = []

    browser = webdriver.Firefox()
    browser.get('https://quiz.honorcup.ru/app/?id=31514&sign=5ffe6ebb52f21ea4eb18fb1dab50f028')

    time.sleep(5)

    try:
        knopka_srazhats = browser.find_element_by_class_name('about__buttons')
        knopka_srazhats.click()

        time.sleep(10)

        slider = browser.find_elements_by_class_name('slider__item')
        slider[2].click()

        knopka_ai = browser.find_elements_by_class_name('profile__theme')
        knopka_ai[1].click()

        knopka_pt = browser.find_element_by_xpath('/html/body/app/div[1]/nomination/div/div/div[2]/div[3]/div[2]/div/div/div[2]/div')
        knopka_pt.click()

        time.sleep(20)
    except:
        huawei()

    while True:
        try:
            question = browser.find_element_by_class_name('game__question-text')
            print('Найден элемент ${}$ с данным именем класса'.format(question.text))
            answers = browser.find_elements_by_class_name('game__answer')
            for i in answers:
                print('Нашел ответ ${}$'.format(i.text))
                Mid.append(i.text)
            print(Mid)
            a = browser.find_element_by_class_name('game__user-value')
            print(a.text)


            if question.text in Ask:
                print("отвечу сам")
                ind = Ask.index(question.text)
                print(Answ[ind])
                ind2 = Mid.index(Answ[ind])
                print(ind2)
                answers[ind2].click()
            else:
                print("Ебану наугад") 
                answers[1].click()
            Mid.clear()
            time.sleep(30)
        except:
            print('Нихера не нашел')
            browser.quit()
            huawei()


huawei()



#game__question-text найти текст вопроса 
#game__answer текст ответа
#button stretch play сыграть ещё
#game__answer selected right правильный ответ

#game__user-value