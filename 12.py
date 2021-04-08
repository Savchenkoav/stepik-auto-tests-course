# не забываем оставить пустую строку в конце файла
from selenium import webdriver
import time
import math
import os
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    print(os.path.abspath(__file__)) 
    print(os.path.abspath(os.path.dirname(__file__)))
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("input_value").text
    
    
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_id("robotCheckbox").click()
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("robotsRule").click()   
    browser.find_element_by_css_selector("button.btn").click()
    
   
   
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()