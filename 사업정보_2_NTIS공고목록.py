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
import shutil

current_time=datetime.datetime.now()


driver=webdriver.Chrome('C:\selenium\chromedriver')
try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date()))
except:
    pass
url='https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do'
driver.get(url)
driver.maximize_window()

driver.find_element_by_xpath('//tr[@id="statusBtn"]/td[2]').click()
time.sleep(5)
driver.find_element_by_xpath('//tr[@id="statusBtn"]/td[3]').click()
time.sleep(5)
driver.find_element_by_xpath('//div[@class="table_option"]/a[3]').click()
time.sleep(10)



file_oldname = os.path.join("C:/Users/82106/Downloads", "공고목록.xls")
file_newname_newfile = os.path.join("C:/Users/82106/Downloads", "지원사업조회_NTIS_최신화.xls")

os.rename(file_oldname, file_newname_newfile)

time.sleep(5)

src='C:/Users/82106/Downloads/' #다운로드받는 위치
dir="C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/" # 옮길위치
file_list=os.listdir(src) #다운로드받는 위치의 파일들

filename=[s for s in file_list if '지원사업조회_NTIS_최신화' in s] #다운받은 연구기관 파일들 'orgComparison_' 라는 문자를 가진 파일만 찾기
for i in filename:
    shutil.move(src + (i), dir + (i))
