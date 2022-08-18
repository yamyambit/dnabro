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

등록입력=input("등록 시작일을 입력하세요 ex:2022-04-23\n")
등록일=datetime.date(int(등록입력[0:4]),int(등록입력[5:7]),int(등록입력[8:]))
오늘날짜=current_time.date()
print(type(등록일))
print(type(오늘날짜))

wibity=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/공모전데이터_경남울산_위비티/"+str(current_time.date())+"/위비티.csv")

wibity = wibity.drop_duplicates(['주최/주관','공모명','응모분야','응모대상','시상규모','등록일','마감일','바로가기'])
wibity_before=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/공모전데이터_경남울산_위비티/"+등록입력+"/최종/위비티_완료"+등록입력+".csv")


for i in range(wibity.shape[0]):
    if 등록일<=datetime.date(int("20"+wibity.iloc[i,5][2:4]),int(wibity.iloc[i,5][5:7]),int(wibity.iloc[i,5][8:]))<=오늘날짜:
        wibity.iloc[i,9]='유지'
wibity1 = wibity.drop(wibity[wibity['not'] != '유지'].index)
wibity1=wibity1.sort_values(by=['등록일','공모명'])
wibity1.to_csv("C:/Users/82106/PycharmProjects/selenium/venv/공모전데이터_경남울산_위비티/"+str(current_time.date())+"/최종/위비티_완료_원본"+str(current_time.date())+".csv",encoding='UTF-8-sig', index=False)

for i in range(wibity.shape[0]):
    for j in range(wibity_before.shape[0]):
        if wibity.iloc[i,0]==wibity_before.iloc[j,0] and wibity.iloc[i,1]==wibity_before.iloc[j,1]:
            wibity.iloc[i,9]='제거'

wibity = wibity.drop(wibity[wibity['not'] != '유지'].index)

for i in range(wibity.shape[0]):
    if wibity.iloc[i, -2][-1] == ";":
        wibity.iloc[i, -2] = wibity.iloc[i, -2][:-1] + ","

wibity=wibity.sort_values(by=['등록일','공모명'])

if wibity.iloc[-1,-2][-1]==",":
    wibity.iloc[-1,-2]=wibity.iloc[-1, -2][:-1]+";"

wibity.to_csv("C:/Users/82106/PycharmProjects/selenium/venv/공모전데이터_경남울산_위비티/"+str(current_time.date())+"/최종/위비티_완료"+str(current_time.date())+".csv",encoding='UTF-8-sig', index=False)