# не забываем оставить пустую строку в конце файла
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
 
   
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()   
    browser.find_element_by_css_selector("button.btn").click()
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()