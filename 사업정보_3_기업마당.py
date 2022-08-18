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

start = time.time()
current_time=datetime.datetime.now()
try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date()))
except:
    pass
df2=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/코드테이블.csv", encoding='euc-kr')
worknet = open("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/지원사업조회_기업마당_최신화.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr = csv.writer(worknet)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr.writerow(['지원사업조회']+[' '] + [' '] +[' '] +[' '] + [' '] + [' '] + [' ']+[' ']+[' ']+[' ']+[' ']+[' '])
wr.writerow([' ']+[' '] + [' '] +[' '] +[' '] + [' '] + [' '] + [' ']+[' ']+[' ']+[' ']+[' ']+[' '])
wr.writerow(['번호']+['분야'] + ['지원사업명'] +['사업개요'] +['상세 URL'] + ['신청시작일'] + ["신청마감일"] + ["신청기간"]+['소관부처']+['주관기관']+['접수기관']+['등록일']+['조회수'])  # csv파일의 컬럼을 지정

driver=webdriver.Chrome('C:\selenium\chromedriver')

url = 'https://www.bizinfo.go.kr/web/lay1/bbs/S1T122C128/AS/74/list.do'

driver.get(url)
driver.maximize_window()

경남울산=['경남','울산']

for 지역 in 경남울산:
    driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/form/div[1]/input[@type="text"]').send_keys(지역)
    driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/form/div[1]/input[@type="submit"]').click()
    페이지목록=len(driver.find_elements_by_xpath('/html/body/div[1]/section/div[3]/div[2]/a'))
    마지막페이지=int(driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/a['+str(페이지목록)+']').get_attribute('href').split("=")[-1])

    for i in range(1,마지막페이지+1):
        for j in range(1,페이지목록):
            try:
                if int(driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/a['+str(j)+']').get_attribute('href').split("=")[-1])==i:
                    driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/a['+str(j)+']').click()
                    공고목록=len(driver.find_elements_by_xpath("//div[@class='table_Type_1']//table/tbody/tr"))

                    for 공고 in range(1,공고목록+1):
                        번호=driver.find_element_by_xpath("//div[@class='table_Type_1']/table/tbody/tr["+str(공고)+"]/td[1]").text
                        분야=driver.find_element_by_xpath("//div[@class='table_Type_1']/table/tbody/tr["+str(공고)+"]/td[2]").text[0:]
                        driver.find_element_by_xpath("//div[@class='table_Type_1']/table/tbody/tr[" + str(공고) + "]/td[3]/a").click()
                        주관기관=driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/div[1]/div[3]/ul/li[2]/div').text
                        상세_URL=driver.current_url
                        사업개요=driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/div[2]/div[1]/div[3]/ul/li[4]/div').text
                        driver.back()
                        지원사업명 = driver.find_element_by_xpath("//div[@class='table_Type_1']/table/tbody/tr["+str(공고)+"]/td[3]").text
                        신청기간=driver.find_element_by_xpath("//div[@class='table_Type_1']/table/tbody/tr["+str(공고)+"]/td[4]").text
                        if len(신청기간)==23:
                            신청시작일=신청기간.split('-')[0]+신청기간.split('-')[1]+신청기간.split('-')[2][0:2]
                            신청마감일=신청기간.split('-')[2][5:]+신청기간.split('-')[3]+신청기간.split('-')[4]
                        else:
                            신청시작일 = '바로가기 참조'
                            신청마감일 = '바로가기 참조'
                        소관부처=driver.find_element_by_xpath("//div[@class='table_Type_1']/table/tbody/tr["+str(공고)+"]/td[5]").text

                        접수기관=''
                        등록일0=driver.find_element_by_xpath("//div[@class='table_Type_1']/table/tbody/tr["+str(공고)+"]/td[6]").text
                        등록일=등록일0.split('-')[0]+'.'+등록일0.split('-')[1]+'.'+등록일0.split('-')[2]
                        조회수=driver.find_element_by_xpath("//div[@class='table_Type_1']/table/tbody/tr["+str(공고)+"]/td[7]").text
                        wr.writerow([번호]+[분야] + [지원사업명] +[사업개요] +[상세_URL] + [신청시작일] + [신청마감일] + [신청기간]+[소관부처]+[주관기관]+[접수기관]+[등록일]+[조회수])
            except:
                continue


    driver.find_element_by_xpath('/html/body/div[1]/section/div[3]/form/div[1]/input[@type="text"]').clear()

기업마당=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/지원사업조회_기업마당_최신화.csv')

기업마당.to_excel('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/지원사업조회_기업마당_최신화.xls',encoding='UTF-8-sig', index=False)

print(time.time()-start)