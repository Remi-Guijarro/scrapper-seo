from time import sleep
from typing import BinaryIO
from selenium import webdriver
from selenium import *

option = webdriver.ChromeOptions()
option.add_argument('headless')
chromeBinary = "C:/Users/remig/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromeBinary, options=option)
driver.get("https://www.google.com/search?q=allintitle%3A\"voiture+électrique\"")

cookies_btn = driver.find_elements_by_class_name('jyfHyd')

for btn in cookies_btn:
    if btn.text == 'J\'accepte':
        btn.click()

result_stat = driver.find_element_by_id('result-stats')
print(str(result_stat.text))


# next_btn = driver.find_element_by_id('pnnext')
# cpt = 0
# next_btn.click()
# while next_btn:
#     try:   
#         next_btn = driver.find_element_by_id('pnnext')
#         next_btn.click()    
#     except n:     
#         break
#     cpt += len(driver.find_elements_by_class_name('yuRUbf'))

# print('there is '+ str(cpt) + ' results ')
