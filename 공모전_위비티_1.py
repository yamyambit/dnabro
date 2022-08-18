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
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/공모전데이터_경남울산_위비티/"+str(current_time.date()))
except:
    pass
start = time.time()


위비티 = open("C:/Users/82106/PycharmProjects/selenium/venv/공모전데이터_경남울산_위비티/"+str(current_time.date())+"/위비티.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr = csv.writer(위비티)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr.writerow(['주최/주관'] + ['공모명'] + ['응모분야'] + ['응모대상'] + ['시상규모'] + ['등록일']+ ['마감일']+ ['바로가기']+['select * from bio_pride_gyeongnam.tbl_content_awards_info;\ninsert into bio_pride_gyeongnam.tbl_content_awards_info ( COMP_NAME, APPLY_TITLE, JOB_POS,QUALIFY, CONDITIONS,ST_DT, END_DT, URL ,INPUT_TYPE,RESOURCE_CODE)\nvalues']+['not'])  # csv파일의 컬럼을 지정

driver=webdriver.Chrome('C:\selenium\chromedriver')
url = 'https://www.wevity.com/?c=find&s=1&gub=1'
driver.get(url)
driver.maximize_window()

for 접수여부 in range(5,6):
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[2]/div/ul/li['+str(접수여부)+']/a').click()
    n = 0
    while n==0:
        리스트목록=len(driver.find_elements_by_xpath('//div[@class="ms-list"]/ul/li'))
        for 리스트 in range(2, 리스트목록+1):
        # for 리스트 in range(2,3):
            try:
                driver.find_element_by_xpath('//div[@class="ms-list"]/ul/li['+str(리스트)+']/div[1]/a').click()
                time.sleep(1)
                공모명=driver.find_element_by_xpath('//div[@class="contest-detail"]/div[1]/h6').text.replace("'",'')
                응모분야=driver.find_element_by_xpath( '//ul[@class="cd-info-list"]/li[1]').text.replace("분야\n",'').replace("'",'')
                응모대상=driver.find_element_by_xpath( '//ul[@class="cd-info-list"]/li[2]').text.replace("응모대상\n",'').replace("'",'')
                주최주관=driver.find_element_by_xpath( '//ul[@class="cd-info-list"]/li[3]').text.replace("주최/주관\n",'').replace("'",'')
                접수기간=driver.find_element_by_xpath( '//ul[@class="cd-info-list"]/li[5]').text.replace("접수기간\n",'').replace("'",'')
                등록일=접수기간.split(" ~ ")[0].replace("'",'')
                마감일=접수기간.split(" ~ ")[1].split(" ")[0].replace("'",'')
                시상규모=driver.find_element_by_xpath( '//ul[@class="cd-info-list"]/li[6]').text.replace("총 상금\n",'').replace("'",'')
                try:
                    바로가기=driver.find_element_by_xpath( '//ul[@class="cd-info-list"]/li[8]/a').get_attribute('href')
                except:
                    바로가기=''
                sql="('"+str(주최주관)+"','"+str(공모명)+"','"+str(응모분야)+"','"+str(응모대상)+"','"+str(시상규모)+"','"+str(등록일)+"','"+str(마감일)+"','"+str(바로가기)+"','C','BP30050012'),"
                sql=sql.replace("'nan'","''")
                wr.writerow([주최주관] + [공모명] + [응모분야] + [응모대상] + [시상규모] + [등록일] + [마감일] + [바로가기]+[sql])
                print(리스트 - 1, 공모명,등록일)
                driver.back()
            except:
                print('이거 에러임',리스트 - 1, 공모명,등록일)
                pass

            time.sleep(2)

        페이지개수 = len(driver.find_elements_by_xpath('//div[@class="list-navi"]/a'))
        print(페이지개수)
        print(str(driver.find_element_by_xpath('//div[@class="list-navi"]/a[' + str(페이지개수) + ']').get_attribute('href')))
        if driver.find_element_by_xpath('//div[@class="list-navi"]/a[' + str(페이지개수) + ']').get_attribute('href')!=None:
            driver.find_element_by_xpath('//div[@class="list-navi"]/a[' + str(페이지개수) + ']').click()
            n=0
        elif str(driver.find_element_by_xpath('//div[@class="list-navi"]/a[' + str(페이지개수) + ']').get_attribute('href'))=='None':
            n=1
        print(time.time()-start)
try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/공모전데이터_경남울산_위비티/"+str(current_time.date())+"/최종")
except:
    pass

