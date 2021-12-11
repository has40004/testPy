# from selenium import webdriver
# import time 

# link = "http://suninjuly.github.io/registration2.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Nastya")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Mikhailovna")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Taganrog")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("btn-default")
#     button.click()
# finally:
#     time.sleep(30)
#     browser.quit()

# не забываем оставить пустую строку в конце файла

# from selenium import webdriver
# import time 
# import math

# link = "http://suninjuly.github.io/find_link_text"
# link2 = "http://suninjuly.github.io/find_link_text_redirect13.html"

# try:
#     browser = webdriver.Chrome() 
#     browser.get(link)
#     links = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     links.click()
#     browser.get(link2)
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Nastya")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Mikhailovna")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Taganrog")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("btn-default")
#     button.click()
# finally:
#     time.sleep(30)
#     browser.quit()
 
 
# from selenium import webdriver
# import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form")
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Nastya")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Mikhailovna")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Taganrog")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     # elements = browser.find_elements_by_css_selector("button")
#     # for element in elements:
#     #     element.send_keys("Мой ответ")

#     button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# import time

# try: 
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#     time.sleep(1)
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     welcome_text = welcome_text_elt.text
#     assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
#     time.sleep(10)
#     browser.quit()



#########################################################


# from selenium import webdriver
# import time
# import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try: 
#     link = "http://suninjuly.github.io/selects1.html?"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
#     option1.click()
#     option2 = browser.find_element_by_css_selector("[id='robotsRule']")
#     option2.click()
#     x_element = browser.find_element_by_id("treasure")
#     x =  x_element.get_attribute("valuex")
#     y = calc(x)
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
  

# finally:
#     time.sleep(10)
#     browser.quit()


###########################################



# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import Select


# try: 
#     link = "http://suninjuly.github.io/selects2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x1_element = browser.find_element_by_id("num1")
#     x1 = x1_element.text
#     x2_element = browser.find_element_by_id("num2")
#     x2 = x2_element.text
#     sum = int(x1) + int(x2) 
#     sum1 = str(sum)
#     print(type(sum1))
#     select = Select(browser.find_element_by_tag_name("select"))
#     select.select_by_value(sum1)
#     # browser.find_element_by_tag_name("select").click()
#     # browser.find_element_by_css_selector(f"[value={sum1}]").click()
#     button = browser.find_element_by_css_selector("button")
#     button.click()
  

# finally:
#     time.sleep(10)
#     browser.quit()



#####################################



# from selenium import webdriver
# import time
# import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try: 
#     link = "http://suninjuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text 
#     y = calc(x)
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#     option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
#     option1.click()
#     option2 = browser.find_element_by_css_selector("[id='robotsRule']")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
#     option2.click()

#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#     button = browser.find_element_by_css_selector("button.btn")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
  

# finally:
#     time.sleep(10)
#     browser.quit()


#######################################



# from selenium import webdriver
# import time
# import os

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/file_input.html")
#     input1 = browser.find_element_by_name("firstname")
#     input1.send_keys("Nastya")
#     input2 = browser.find_element_by_name("lastname")
#     input2.send_keys("Mikhailovna")
#     input3 = browser.find_element_by_name("email")
#     input3.send_keys("test@mail.com")
#     current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#     file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#     input4 = browser.find_element_by_name("file")
#     input4.send_keys(file_path)    
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

####################################


# from selenium import webdriver
# import time
# import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/alert_accept.html")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#     alert = browser.switch_to.alert
#     alert.accept()
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text 
#     y = calc(x)
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     time.sleep(10)
#     browser.quit()


###############################################################################



# from selenium import webdriver
# import time
# import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/redirect_accept.html")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text 
#     y = calc(x)
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

# finally:
#     time.sleep(10)
#     browser.quit()

# from selenium.common.exceptions import NoAlertPresentException # в начале файла

# def solve_quiz_and_get_code(self):
#     alert = self.browser.switch_to.alert
#     x = alert.text.split(" ")[2]
#     answer = str(math.log(abs((12 * math.sin(float(x))))))
#     alert.send_keys(answer)
#     alert.accept()
#     try:
#         alert = self.browser.switch_to.alert
#         alert_text = alert.text
#         print(f"Your code: {alert_text}")
#         alert.accept()
#     except NoAlertPresentException:
#         print("No second alert presented")


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# def pytest_addoption(parser):
#     """Опции командной строки.
#     В командную строку передается параметр вида '--language="es"'
#     По умолчанию передается параметр, включающий английский интерфейс в браузере
#     """
#     parser.addoption('--language', action='store', default='en', help='Choose language')


# @pytest.fixture(scope="function")
# def browser(request):
#     # В переменную user_language передается параметр из командной строки
#     user_language = request.config.getoption('language')
    
#     # Инициализируются опции браузера
#     options = Options()
    
#     # В опции вебдрайвера передаем параметр из командной строки
#     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#     browser = webdriver.Chrome(options=options)
    
#     browser.implicitly_wait(5)
#     yield browser
#     browser.quit()