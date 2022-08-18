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
등록입력2=input("등록 시작일 이전일을 입력하세요 ex:2022-04-20\n")
등록일2=datetime.date(int(등록입력2[0:4]),int(등록입력2[5:7]),int(등록입력2[8:]))

오늘날짜=current_time.date()
df_i = pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/" + str(current_time.date()) + "/채용정보_경남울산_인턴.csv")
df_j = pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/" + str(current_time.date()) + "/채용정보_경남울산_정규등.csv")

if df_i.shape[0]==0:
    df_i = pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/2022-05-30/채용정보_경남울산_인턴.csv")
    for i in range(df_i.shape[0]):
        for j in range(df_i.shape[1]):
            df_i.iloc[i,j]='2022-05-30'
df_l=['df_i','df_j']


for i in range(df_i.shape[0]):
   df_i.iloc[i,-2]=df_i.iloc[i,-2].replace(";","")
for i in range(df_j.shape[0]):
    df_j.iloc[i, -2] = df_j.iloc[i, -2].replace(";","")

df_i=df_i.sort_values(by=['등록일','채용공고명'])
df_j=df_j.sort_values(by=['등록일','채용공고명'])

if df_i.shape[0]>=1:
    if df_i.iloc[-1, 11][-1] == ',':
        df_i.iloc[-1, 11] = df_i.iloc[df_i.shape[0]-1, 11][:-1]+";"
if df_j.shape[0]>=1:
    if df_j.iloc[-1, 11][-1] == ',':
        df_j.iloc[-1, 11] = df_j.iloc[df_j.shape[0]-1, 11][:-1]+";"
try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/최종")
except:
    pass

for i in range(df_i.shape[0]):
    df_i.iloc[i,11]=df_i.iloc[i,11].replace("'Null'","Null")
    df_i.iloc[i, 11] = df_i.iloc[i, 11].replace("''", "Null")
    df_i.iloc[i, 11] = df_i.iloc[i, 11].replace("'nan'", "Null")
for i in range(df_j.shape[0]):
    df_j.iloc[i,11]=df_j.iloc[i,11].replace("'Null'","Null")
    df_j.iloc[i, 11] = df_j.iloc[i, 11].replace("''", "Null")
    df_j.iloc[i, 11] = df_j.iloc[i, 11].replace("'nan'", "Null")


df0=pd.concat([df_i,df_j])

df0.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/채용정보_경남울산_필터링원본.csv',encoding='UTF-8-sig', index=False)

for df in df_l:
    print(len(globals()[df].iloc[0,6]))
    if len(globals()[df].iloc[0,6].replace(" ",''))!=8:
        for i in range(globals()[df].shape[0]):
            if 등록일<=datetime.date(int(globals()[df].iloc[i,6][0:4]),int(globals()[df].iloc[i,6][5:7]),int(globals()[df].iloc[i,6][8:]))<=오늘날짜:
                globals()[df].iloc[i,12]='유지'
        print(globals()[df].shape[0])
        globals()[df] = globals()[df].drop(globals()[df][globals()[df]['not'] != '유지'].index)
    elif len(globals()[df].iloc[0,6].replace(" ",''))==8:
        for i in range(globals()[df].shape[0]):
            if 등록일<=datetime.date(int("20"+globals()[df].iloc[i,6][0:2]),int(globals()[df].iloc[i,6][3:5]),int(globals()[df].iloc[i,6][6:]))<=오늘날짜:
                globals()[df].iloc[i,12]='유지'
        print(globals()[df].shape[0])
        globals()[df] = globals()[df].drop(globals()[df][globals()[df]['not'] != '유지'].index)

df_i.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/최종/채용정보_경남울산_인턴_원본_완료'+ str(current_time.date()) +'.csv',encoding='UTF-8-sig', index=False)
df_j.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/최종/채용정보_경남울산_정규등_원본_완료'+ str(current_time.date()) +'.csv',encoding='UTF-8-sig', index=False)

df_i_before1=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + 등록입력 + '/최종/채용정보_경남울산_인턴_완료'+ 등록입력 +'.csv')
df_j_before1=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + 등록입력 + '/최종/채용정보_경남울산_정규등_완료'+ 등록입력 +'.csv')

df_i_before2=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + 등록입력 + '/최종/채용정보_경남울산_인턴_누적~'+ 등록입력2 +'.csv')
df_j_before2=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + 등록입력 + '/최종/채용정보_경남울산_정규등_누적~'+ 등록입력2 +'.csv')

df_i_before=pd.concat([df_i_before1,df_i_before2]).drop_duplicates(['채용공고명','등록일'])
df_j_before=pd.concat([df_j_before1,df_j_before2]).drop_duplicates(['채용공고명','등록일'])

df_i_before=df_i_before.sort_values(by=['등록일','채용공고명'])
df_j_before=df_j_before.sort_values(by=['등록일','채용공고명'])

df_i_before.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/최종/채용정보_경남울산_인턴_누적~'+str(등록입력)+'.csv',
          encoding='UTF-8-sig', index=False)
df_j_before.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/최종/채용정보_경남울산_정규등_누적~'+str(등록입력)+'.csv',
          encoding='UTF-8-sig', index=False)

if df_i.shape[0]!=0 and df_i_before.shape[0]!=0:
    for i in range(df_i.shape[0]):
        for j in range(df_i_before.shape[0]):
            if df_i.iloc[i,0]==df_i_before.iloc[j,0] and df_i.iloc[i,1]==df_i_before.iloc[j,1] and df_i.iloc[i,2]==df_i_before.iloc[j,2]:
                df_i.iloc[i,12]='제거'
    df_i = df_i.drop(df_i[df_i['not'] != '유지'].index)

for i in range(df_j.shape[0]):
    for j in range(df_j_before.shape[0]):
        if df_j.iloc[i,0]==df_j_before.iloc[j,0] and df_j.iloc[i,1]==df_j_before.iloc[j,1] and df_j.iloc[i,2]==df_j_before.iloc[j,2]:
            df_j.iloc[i,12]='제거'
df_j = df_j.drop(df_j[df_j['not'] != '유지'].index)

for i in range(df_i.shape[0]):
    df_i.iloc[i,11]=df_i.iloc[i,11].replace("\n","")

for i in range(df_j.shape[0]):
    df_j.iloc[i,11]=df_j.iloc[i,11].replace("\n","")


for i in range(df_j.shape[0]):
    if df_j.iloc[i,-2][-1]!=",":
        df_j.iloc[i,-2]=df_j.iloc[i,-2].replace(";","")
        if i!=df_j.shape[0]-1:
            df_j.iloc[i, -2]=df_j.iloc[i,-2]+","
df_j.iloc[-1, -2]=df_j.iloc[i,-2][:-1]+");"


df_i.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/최종/채용정보_경남울산_인턴_완료'  + str(current_time.date()) +'.csv',encoding='UTF-8-sig', index=False)
df_j.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) +'/최종/채용정보_경남울산_정규등_완료'+ str(current_time.date()) +'.csv',encoding='UTF-8-sig', index=False)
