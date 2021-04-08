# не забываем оставить пустую строку в конце файла
from selenium import webdriver
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Кликаем кнопку
    browser.find_element_by_css_selector("button.btn").click()
   
    
    #Принять confirm
    browser.switch_to.alert.accept()

    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_css_selector("button.btn").click()
    
    #Копируем результат из окна
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()