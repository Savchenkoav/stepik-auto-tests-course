# не забываем оставить пустую строку в конце файла
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(int(x)+int(y))


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    x=calc(x)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(x)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
   
  
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()