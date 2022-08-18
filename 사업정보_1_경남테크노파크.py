from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

import time
import bs4
import datetime
import requests
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
import os

current_time=datetime.datetime.now()
try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date()))
except:
    pass
start = time.time()
df2=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/코드테이블2.csv", encoding='euc-kr')
worknet = open("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/경남테크노파크_insert.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr = csv.writer(worknet)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr.writerow(['num']+['부처명'] + ['공고기관명'] + ['공고명'] + ['접수일'] + ["마감일"] + ["공고문바로가기URL"]+['insert']+['코드'])  # csv파일의 컬럼을 지정

driver=webdriver.Chrome('C:\selenium\chromedriver')

url = 'https://www.gntp.or.kr/biz/apply'
driver.get(url)
driver.maximize_window()



select = Select(driver.find_element_by_id("register"))  # 10개 적용
select.select_by_value("ing") #접수중
driver.find_element_by_xpath('/html/body/section/div[2]/div[5]/div[3]/div/button').click() # 검색버튼 클릭
n=0
for a in range(3,len(driver.find_elements_by_xpath('/html/body/section/div[2]/div[5]/div[5]/div/a'))-1):

    driver.find_element_by_xpath('/html/body/section/div[2]/div[5]/div[5]/div/a['+str(a)+']').click()
    for i in range(1,len(driver.find_elements_by_xpath('/html/body/section/div[2]/div[5]/div[4]/div/table/tbody/tr'))+1):
        n = n + 1
        num=3000+n
        공고명=driver.find_element_by_xpath('/html/body/section/div[2]/div[5]/div[4]/div/table/tbody/tr['+str(i)+']/td[5]/a').text
        print(driver.find_element_by_xpath('/html/body/section/div[2]/div[5]/div[4]/div/table/tbody/tr['+str(i)+']/td[5]/a').text)
        공고기관명 = driver.find_element_by_xpath('/html/body/section/div[2]/div[5]/div[4]/div/table/tbody/tr['+str(i)+']/td[2]').text
        driver.find_element_by_xpath('/html/body/section/div[2]/div[5]/div[4]/div/table/tbody/tr['+str(i)+']/td[5]/a').click()
        부처명='경남테크노파크'
        for j in range(df2.shape[0]):
            if 부처명 == df2.iloc[j, 4]:
                부처명2=df2.iloc[j,0]
        접수일=driver.find_element_by_xpath('/html/body/section/div[2]/div[5]/div[4]/table/tbody/tr[2]/td[4]').text.split('~')[0]
        마감일=driver.find_element_by_xpath('/html/body/section/div[2]/div[5]/div[4]/table/tbody/tr[2]/td[4]').text.split('~')[1][1:]
        공고문바로가기URL=driver.current_url
        insert=''
        wr.writerow([num]+[부처명] + [공고기관명] + [공고명] + [접수일] + [마감일] + [공고문바로가기URL]+[insert]+[부처명2])
        driver.back()
time.sleep(3)

print(time.time()-start)
