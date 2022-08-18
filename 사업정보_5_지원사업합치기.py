from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

import numpy as np
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
등록입력2=input("등록 시작일의 전단계 날짜를 입력하세요 ex:2022-04-20\n")
등록일=datetime.date(int(등록입력[0:4]),int(등록입력[5:7]),int(등록입력[8:]))
오늘날짜=current_time.date()


df0=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/경남테크노파크_insert.csv')
df0=df0.sort_values(by=['접수일'])
for i in range(0,df0.shape[0]):
    df0.iloc[i,7]="('"+df0.iloc[i,8].replace(" ","")+"','"+df0.iloc[i,2]+"','"+df0.iloc[i,3]+"','"+df0.iloc[i,4]+"','"+df0.iloc[i,5]+"','"+df0.iloc[i,6]+"',"+"'C','BP30050017'),"


df0.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/경남테크노파크_insert_최신화.csv',encoding='UTF-8-sig',index=False)
df1=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/경남테크노파크_insert_최신화.csv")

df_list=['지원사업조회_기업마당_최신화','지원사업조회_NTIS_최신화']
i=1
for dfn in df_list:
    i=i+1
    globals()["df"+str(i)]=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/'+dfn+'_insert.csv')
li=[]
li=li+list(df3.iloc[:,-2])+list(df2.iloc[:,-2])+list(df1.iloc[:,-2])
df=pd.DataFrame({'insert문':li,
                 "select * from bio_pride_gyeongnam.tbl_business_info;\ndelete from bio_pride_gyeongnam.tbl_business_info where INPUT_TYPE='C';\ninsert into bio_pride_gyeongnam.tbl_business_info (GOV_CODE, NOTICE_ORGAN, TASK_NAME, ST_DT, END_DT, URL ,INPUT_TYPE,RESOURCE_CODE)\nvalues":'',
                 "등록일":'',
                 "마감일":'',
                 "공고명":''})
for i in range(0,df.shape[0]):
    df.iloc[i,1]=df.iloc[i,0]

df.iloc[-1,1]=df.iloc[-1,1].replace('),',');')
print(df.iloc[-1,1])

print(df)
for i in range(0,df.shape[0]):

    if df.iloc[i,0][2]!='B':
        print(i,df.iloc[i,0])
        df.iloc[i,0]=np.nan
df=df.dropna()
print(df)
for i in range(df.shape[0]):
    df.iloc[i,1]=df.iloc[i,1].replace('바로가기- 참-조','바로가기 참조')
    df.iloc[i,1]=df.iloc[i,1].replace("'바로가기 참조'","Null")
for i in range(df.shape[0]):
    if str(df.iloc[i, 1].split(",'")[4][0])=='2':
        df.iloc[i, 3] = df.iloc[i, 1].split(",'")[4]
    elif str(df.iloc[i, 1].split(",'")[4][0]) != '2':
        df.iloc[i, 3] = 'Null'
    if str(df.iloc[i, 1].split(",'")[3][0])=='2':
        df.iloc[i, 2] = df.iloc[i, 1].split(",'")[3]
    elif str(df.iloc[i, 1].split(",'")[3][0])!='2':
        df.iloc[i, 2] = 'Null'
    df.iloc[i, 4] = df.iloc[i, 1].split("',")[2].replace("'","").replace("Null", "").replace(",", "")
try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/최종")
except:
    pass

df=df.sort_values(by=['등록일','공고명'])

df['not']=''
df.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/최종/기업공고최종_원본'+str(current_time.date())+'.csv',
          encoding='UTF-8-sig', index=False)

for i in range(df.shape[0]):
    df_std=df.iloc[i,1].split("',")[3].split("'")[1]
    if str(df_std[0])!='2':
        df.iloc[i, 5] = '유지'
    elif str(df_std[0])=='2' and 등록일<=datetime.date(int("20"+df_std[2:4]),int(df_std[5:7]),int(df_std[8:]))<=오늘날짜:
        df.iloc[i,5]='유지'


df_before0=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' +str(등록입력)+ '/최종/기업공고최종_누적~'+str(등록입력2)+'.csv')
df_before1=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' +str(등록입력)+ '/최종/기업공고최종_원본'+str(등록입력)+'.csv')

df_before=pd.concat([df_before0,df_before1]).drop_duplicates(['공고명','등록일'])

for i in range(df_before.shape[0]):
    df_before.iloc[i,4]= df_before.iloc[i,4].replace("'","").replace("Null", "").replace(",", "")

df_before=df_before.sort_values(by=['등록일','공고명'])

df_before.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/최종/기업공고최종_누적~'+str(등록입력)+'.csv',
          encoding='UTF-8-sig', index=False)

for i in range(df.shape[0]):
    for j in range(df_before.shape[0]):
        if df.iloc[i,4]==df_before.iloc[j,4]:
            df.iloc[i,5]='탈락'
df = df.drop(df[df['not'] != '유지'].index)

for i in range(df.shape[0]):
    df.iloc[i,4]=df.iloc[i,4].replace("'","")
    df.iloc[i, 4] = df.iloc[i, 4].replace("Null", "")
    df.iloc[i, 4] = df.iloc[i, 4].replace(",", "")
    if df.iloc[i,1][-1]==';':
        df.iloc[i, 1]=df.iloc[i,1][:-1]+","
    df.iloc[-1,1]=df.iloc[-1, 1][:-1]+";"

df.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/최종/기업공고최종'+str(current_time.date())+'.csv',
          encoding='UTF-8-sig', index=False)