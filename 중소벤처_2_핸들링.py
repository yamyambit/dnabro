from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

import time
import bs4

import requests
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
import datetime

import clipboard

current_time=datetime.datetime.now()
등록입력=input("등록 시작일을 입력하세요 ex:2022-04-23\n")



df1=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+str(current_time.date())+"/정책뉴스.csv", encoding='UTF-8-sig')
df2=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+str(current_time.date())+"/중소벤처.csv", encoding='UTF-8-sig')

for i in range(df1.shape[0]):
    df1.iloc[i,2]=int(df1.iloc[i,2].replace("-",""))
df1=df1[df1['작성일']>=20220101]
for i in range(df1.shape[0]):
    df1.iloc[i,2]=str(df1.iloc[i,2])[0:4]+"-"+str(df1.iloc[i,2])[4:6]+"-"+str(df1.iloc[i,2])[6:8]
df3=pd.concat([df1,df2])

df3=df3.sort_values(by=['작성일','제목'])
df3['코드']=''
df3["select * from bio_pride_gyeongnam.tbl_mss_journal;\ndelete from bio_pride_gyeongnam.tbl_mss_journal where MSS_SEQ>=1;\ninsert into bio_pride_gyeongnam.tbl_mss_journal(TITLE, CATEGORY, URL, ORIGINAL_DT, CREATED_DT, RESOURCE_CODE,KEYWORDS)\nvalues"]=''
df3['유지여부']=''


for i in range(df3.shape[0]):
    if df3.iloc[i,4]=='정책동향':
        df3.iloc[i, 6]='BP30050007'
    elif df3.iloc[i,4]=='보도자료':
        df3.iloc[i,6]='BP30050008'
for i in range(df3.shape[0]):
    df3.iloc[i,0]=df3.iloc[i,0].replace("'","")

for i in range(df3.shape[0]):
    if i==df3.shape[0]-1:
        df3.iloc[i, 7] = "('"+ str(df3.iloc[i, 0]) + "','" + str(df3.iloc[i, 4]) + "','" + str(
            df3.iloc[i, 1]) + "','" + str(df3.iloc[i, 2]) + "','" + str(df3.iloc[i, 3]) + "','" + str(df3.iloc[i, 6])+"','"+ str(df3.iloc[i, 5]) + "');"
    else:
        df3.iloc[i, 7] = "('"+ str(df3.iloc[i, 0]) + "','" + str(df3.iloc[i, 4]) + "','" + str(
            df3.iloc[i, 1]) + "','" + str(df3.iloc[i, 2]) + "','" + str(df3.iloc[i, 3]) + "','" + str(df3.iloc[i, 6])+"','"+ str(df3.iloc[i, 5]) + "'),"
    df3.iloc[i,7]=df3.iloc[i,7].replace("'nan'","NULL")
df3.to_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+str(current_time.date())+"/중소벤처정책뉴스_원본"+str(current_time.date())+".csv",encoding='UTF-8-sig', index=False)
df3=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+str(current_time.date())+"/중소벤처정책뉴스_원본"+str(current_time.date())+".csv")
df_before=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+등록입력+"/중소벤처정책뉴스_원본"+등록입력+".csv")

for i in range(df3.shape[0]):
    for j in range(df_before.shape[0]):
        if df3.iloc[i,0]==df_before.iloc[j,0]:
            df3.iloc[i,8]='제거'
    print(df3.iloc[i, 0], df3.iloc[i, 8])
print(df3[df3['유지여부']=='제거'])
df_f=df3.drop(df3[df3['유지여부']=='제거'].index)
print(df_f.iloc[-1,0])
df_f.to_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/뉴스데이터/"+str(current_time.date())+"/중소벤처정책뉴스"+str(current_time.date())+".csv",encoding='UTF-8-sig', index=False)

