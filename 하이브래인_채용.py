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

시작=time.time()

current_time=datetime.datetime.now()
try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/하이브레인넷/"+str(current_time.date()))
except:
    pass
start = time.time()

등록입력=input("등록 시작일을 입력하세요 ex:2022-04-23\n")
등록일=datetime.date(int(등록입력[0:4]),int(등록입력[5:7]),int(등록입력[8:]))
오늘날짜=current_time.date()

하이브레인넷 = open("C:/Users/82106/PycharmProjects/selenium/venv/하이브레인넷/"+str(current_time.date())+"/하이브레인넷.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr = csv.writer(하이브레인넷)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr.writerow(['공고명'] + ['채용유형'] + ['기관유형'] + ['근무예정지'] + ['학력자격'] + ['접수시작']+['접수마감']+ ['바로가기']+['select * from bio_pride_gyeongnam.tbl_researcher_careers_info;\ninsert into bio_pride_gyeongnam.tbl_researcher_careers_info ( APPLY_TITLE, COMP_TYPE , QUALIFY, EMPLOY_TYPE,ST_DT, END_DT, URL ,INPUT_TYPE,RESOURCE_CODE)\nvalues']+['not'])  # csv파일의 컬럼을 지정

driver=webdriver.Chrome('C:\selenium\chromedriver')
url = 'https://www.hibrain.net/recruitment/categories/JOB/categories/RES/recruits'
driver.get(url)
driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/ul/li[5]/a').click()#로그인페이지
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/form/input[1]').send_keys('cj7591')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/form/input[3]' ).send_keys('*-ckdwns*-1')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/form/input[2]').click()#로그인
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/nav/ul/li[1]/a').click()#채용정보페이지
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/nav/div/div[3]/ul/li[3]/a').click()#연구원 정보만

time.sleep(2)

NUM=0
while NUM==0:
    리스트 = len(driver.find_elements_by_xpath('//li[@class="row sortRoot"]'))
    for i in range(1,리스트+1):
        time.sleep(1)
        공고=driver.find_element_by_xpath('//li[@class="row sortRoot"]['+str(i)+']/span[2]/a/span')
        공고명=공고.text


        공고.click()
        접수기간=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]').text
        try:
            접수시작=접수기간.split(" ~ ")[0][0:8].replace(".",'/')
            접수마감=접수기간.split(" ~ ")[1][0:8].replace(".",'/')
        except:
            접수시작=접수기간
            접수마감=접수기간
        채용유형=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[2]').text
        기관유형=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[4]').text
        근무예정지=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[4]').text
        학력자격=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[2]').text
        바로가기=driver.current_url
        print(공고명)
        wr.writerow([공고명] + [채용유형] + [기관유형] + [근무예정지] + [학력자격] + [접수시작]+[접수마감]+ [바로가기])
        driver.back()

    try:
        driver.find_element_by_xpath("//div[@class='listNavi']/a/span[@class='imgNext']").click()
    except:
        try:
            driver.find_element_by_xpath("//div[@class='listNavi']/a[1]/span[@class='imgNext']").click()
        except:
            print('끝')
            NUM=1

high=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/하이브레인넷/'+str(current_time.date())+'/하이브레인넷.csv')

for i in range(high.shape[0]):
    if str(high.iloc[i,5][0])!='2':
        high.iloc[i, 9] = '삭제'
    if str(high.iloc[i,3]).find('경남')!=-1:
        high.iloc[i, 9] = '삭제'
    elif str(high.iloc[i,3]).find('울산')!=-1:
        high.iloc[i, 9] = '삭제'
high = high.drop(high[high['not'] == '삭제'].index)
for i in range(high.shape[0]):
    high.iloc[i,8]="('"+str(high.iloc[i,0])+"','"+str(high.iloc[i,2])+"','"+str(high.iloc[i,4])+"','"+\
                   str(high.iloc[i,1])+"','"+str(high.iloc[i,5])+"','"+str(high.iloc[i,6])+"','"+str(high.iloc[i,7])+"','C','BP30050002'),"
    high.iloc[i,8]=high.iloc[i,8].replace("'nan'","''")
high.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/하이브레인넷/'+str(current_time.date())+'/하이브레인넷_insert.csv',encoding='UTF-8-sig', index=False)

for i in range(high.shape[0]):
    if 등록일<=datetime.date(int("20"+high.iloc[i,5][0:2]),int(high.iloc[i,5][3:5]),int(high.iloc[i,5][6:]))<=오늘날짜:
        high.iloc[i,9]='유지'


high_before=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/하이브레인넷/"+등록입력+"/최종/하이브레인넷_완료"+등록입력+".csv")

for i in range(high.shape[0]):
    for j in range(high_before.shape[0]):
        if high.iloc[i,0]==high_before.iloc[j,0]:
            high.iloc[i,9]='삭제'

high = high.drop(high[high['not'] != '유지'].index)
try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/하이브레인넷/"+str(current_time.date())+"/최종")
except:
    pass

high=high.sort_values(by=['접수시작','공고명'])

if high.iloc[-1,-2][-1]==",":
    high.iloc[-1,-2]=high.iloc[-1, -2][:-1]+";"


high.to_csv("C:/Users/82106/PycharmProjects/selenium/venv/하이브레인넷/"+str(current_time.date())+"/최종/하이브레인넷_완료"+str(current_time.date())+".csv",encoding='UTF-8-sig', index=False)

print(time.time()-시작)