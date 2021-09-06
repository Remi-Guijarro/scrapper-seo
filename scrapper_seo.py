from time import sleep
from typing import BinaryIO
from selenium import webdriver
from selenium import *
from sys import argv


def search_keywords_result_count(keywords):
    request = "https://www.google.com/search?q=allintitle%3A"
    for index,key in enumerate(keywords):
        if index == 0:
            request += key
        else:
            request += "+" + key
    print(request)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    chromeBinary = "C:/Users/remig/Desktop/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(chromeBinary, options=option)
    driver.get(request)

    cookies_btn = driver.find_elements_by_class_name('jyfHyd')

    for btn in cookies_btn:
        if btn.text == 'J\'accepte':
            btn.click()

    result_stat = driver.find_element_by_id('result-stats')
    print(str(result_stat.text))


if __name__ == "__main__":
    print(argv[1:])
    search_keywords_result_count(argv[1:])



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
