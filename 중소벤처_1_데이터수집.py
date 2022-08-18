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

키워드목록=['원전','환경','기계설계','지원','연구개발','빅데이터','에너지']

try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+str(current_time.date()))
except:
    pass
start = time.time()

정책뉴스 = open("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+str(current_time.date())+"/정책뉴스.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr = csv.writer(정책뉴스)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr.writerow(['제목'] + ['URL'] + ['작성일'] + ['크롤링날짜']+['구분']+['키워드'])  # csv파일의 컬럼을 지정

driver=webdriver.Chrome('C:\selenium\chromedriver')

url='https://www.korea.kr/news/policyNewsList.do'
driver.get(url)
driver.maximize_window()

driver.find_element_by_xpath('//button[@class="detail_sch"]/span').click()
driver.find_element_by_xpath('//ul[@class="tab-nav"]/li[2]').click()
driver.find_element_by_xpath('//label[@for="A00032"]').click()
driver.find_element_by_xpath('//button[@class="app"]').click()
time.sleep(3)

print(driver.find_element_by_xpath('/html/body/main/section[3]/div/article/div[1]/div[4]/ul/li[1]/a/span[2]/strong').text)

페이지목록=int(driver.find_element_by_xpath('//a[@class="last"]').get_attribute('onclick').split("(")[1].split(")")[0])
for 페이지 in range(1,페이지목록+1):
    if 페이지==1:
        driver.find_element_by_xpath('//div[@class="paging"]/span[@class="num on"]').click()
    else:
        try:
            driver.find_element_by_xpath('//div[@class="paging"]/span/a[@onclick="pageLink('+str(페이지)+'); return false;"]').click()
        except:
            driver.find_element_by_xpath('//div[@class="paging"]/a[@onclick="pageLink(' + str(페이지) + '); return false;"]').click()
    print(페이지)
    time.sleep(3)
    리스트목록=len(driver.find_elements_by_xpath('//div[@class="list-type"]/ul/li'))
    for 기사 in range(1,리스트목록+1):
        제목=driver.find_element_by_xpath('//div[@class="list-type"]/ul/li['+str(기사)+']/a/span[@class="text"]/strong').text
        URL=driver.find_element_by_xpath('//div[@class="list-type"]/ul/li['+str(기사)+']/a').get_attribute('href')
        작성일 = driver.find_element_by_xpath('//div[@class="list-type"]/ul/li[' + str(기사) + ']/a/span[@class="text"]/span[@class="source"]/span').text
        크롤링날짜=str(current_time.date())
        구분='정책동향'

        driver.find_element_by_xpath('//div[@class="list-type"]/ul/li['+str(기사)+']/a').click()
        # time.sleep(2)
        내용 = driver.find_element_by_xpath('/html/body/main/section[3]/div/article/div[2]/div[1]').text
        키워드최종목록=[]
        for 키워드서칭 in 키워드목록:
            내제=내용+제목
            키워드서칭여부=내제.find(키워드서칭)
            if 키워드서칭여부!=-1:
                print(키워드서칭)
                키워드최종목록.append(키워드서칭)
        키워드=str(키워드최종목록).replace("[","").replace("]","").replace("'","")
        driver.back()


        wr.writerow([제목] + [URL] + [작성일] + [크롤링날짜]+[구분]+[키워드])

print(time.time()-start)

중소벤처 = open("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+str(current_time.date())+"/중소벤처.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr = csv.writer(중소벤처)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr.writerow(['제목'] + ['URL'] + ['작성일'] + ['크롤링날짜']+['구분']+['키워드'])  # csv파일의 컬럼을 지정

driver=webdriver.Chrome('C:\selenium\chromedriver')

url='https://www.mss.go.kr/site/smba/ex/bbs/List.do?cbIdx=86'
driver.get(url)
driver.maximize_window()
크롤링날짜=str(current_time.date())
시작날짜=크롤링날짜[0:4]+'0101'

driver.find_element_by_xpath('//div[@class="calendar_box"][1]/input').send_keys(시작날짜)
driver.find_element_by_xpath('//div[@class="calendar_box"][2]/input').send_keys(크롤링날짜.replace("-",""))
driver.find_element_by_xpath('//i[@class="ri-search-line"]').click()

페이지목록=int(driver.find_element_by_xpath('//div[@class="paging"]/a[4]').get_attribute('onclick').split("(")[1].split(")")[0])
for 페이지 in range(1, 페이지목록+1):
    if 페이지 == 1:
        driver.find_element_by_xpath(
            '//div[@class="paging"]/a[@onclick="doBbsFPag(' + str(페이지) + ');return false; "][1]').click()
    else:
        driver.find_element_by_xpath('//a[@onclick="doBbsFPag(' + str(페이지) + ');return false; "]').click()
    time.sleep(2)
    리스트목록 = len(driver.find_elements_by_xpath('//div[@class="board_list type_notice"]/table/tbody/tr'))
    for 리스트 in range(1, 리스트목록+1):

        제목 = driver.find_element_by_xpath('//tr[' + str(리스트) + ']/td[@class="subject bss-sub-text"]/a').text
        작성일 = driver.find_element_by_xpath('//tr[' + str(리스트) + ']/td[5]').text.replace(".", "-")
        driver.find_element_by_xpath('//tr[' + str(리스트) + ']/td[@class="subject bss-sub-text"]/a').click()
        time.sleep(1)
        URL = driver.current_url
        내용=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/table/tbody/tr[7]/td/div[1]/div/div').text
        키워드최종목록=[]
        for 키워드서칭 in 키워드목록:
            내제 = 내용 + 제목
            키워드서칭여부=내제.find(키워드서칭)
            if 키워드서칭여부!=-1:
                print(키워드서칭)
                키워드최종목록.append(키워드서칭)
        키워드=str(키워드최종목록).replace("[","").replace("]","").replace("'","")
        
        구분 = '보도자료'
        time.sleep(1)
        driver.back()
        wr.writerow([제목] + [URL] + [작성일] + [크롤링날짜] + [구분]+[키워드])
        print(제목, URL, 페이지)

print(time.time()-start)

