# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


url = 'https://www.uat.drtalk.com.tw/'    #母網站
#cookies = {'isComfirmedSEY':'1'}

headers ={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
html = requests.get(url, headers= headers)
if html.status_code ==200:
    #print(html.text)
    print('status code=200')
else:
    print('連線不成功')
    
html.encoding = 'UTF-8'    
soup = BeautifulSoup(html.text, 'html.parser')



options = Options()
options.add_argument("--disable-notifications")     #阻擋彈跳視窗
drivers_path="C:/Users/CI-Mark.Huang/Downloads/自動化測試檔/chromedriver"
chrome = webdriver.Chrome(drivers_path, options=options)
chrome.get(url)
time.sleep(3)

#email.send_keys('example@gmail.com') 填入欄位值
chrome.find_element(By.ID,"navbarDropdown").click()
time.sleep(1)
print("=========================================導覽列  turing_navbar")

print("ul.navbar-ul.navbar-nav.mr-auto.ga_navbar")
#ul_var=soup.find_all('ul', {    'class': 'navbar-ul navbar-nav mr-auto ga_navbar'})
ul_var=soup.ul['navbar-ul navbar-nav mr-auto ga_navbar']

print(ul_var)
if ul_var:    
    print("ok")

'''
print(" li.ga_navbar_item")
if soup.find_all('li', {
    'class': 'dropdown-item ga_video_category_link'}):
    print("ok")

print(" a.nav-link.ga_navbar_item_link")
titles = soup.find_all('a', {
    'class': 'dropdown-item ga_video_category_link'})
'''


print("=========================================導覽列-課程分類  turing_navbar_video_category")

print("=========================================首頁搜尋框  turing_homepage_hero_search")

print("=========================================首頁搜尋標籤  turing_homepage_hero_keyword_search")

print("=========================================導覽列-搜尋  turing_navbar_search")




chrome.close()




