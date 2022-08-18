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

일주일=input("일주일 이내로 검색합니까? yes시 1을 입력\n")

try:
    os.mkdir("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date()))
except:
    pass
start = time.time()

driver=webdriver.Chrome('C:\selenium\chromedriver')


worknet = open("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/채용정보_경남울산_고용형태_최신화.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr = csv.writer(worknet)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr.writerow(['회사명'] + ['채용공고명'] + ['담당업무'] + ['지원자격'] + ["주소"] + ["근무조건"] + ["등록일"]+ ["마감일"]+["채용공고URL"]+['고용형태']+['정보제공처'])  # csv파일의 컬럼을 지정

url_intern='https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=02&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword=%EC%9D%B8%ED%84%B4&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=region&actServExcYn=&maxPay=&keywordStaAreaNm=&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=31000%2C48000&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=DESC&currntPageNo=1&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&srcKeyword=%EC%9D%B8%ED%84%B4&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=&stationNm=&benefitGbn=&keywordFlag=&notSrcKeyword=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=1b36643a-705e-403f-b7c5-edbc957c45b1&keywordBusiNm=&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=1&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL'
url_normal='https://www.work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?careerTo=&keywordJobCd=&occupation=02&templateInfo=&shsyWorkSecd=&rot2WorkYn=&payGbn=&resultCnt=50&keywordJobCont=N&cert=&cloDateStdt=&moreCon=&minPay=&codeDepth2Info=11000&isChkLocCall=&sortFieldInfo=DATE&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=ASC&keyword=&termSearchGbn=all&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&webIsOut=region&actServExcYn=&maxPay=&keywordStaAreaNm=N&emailApplyYn=&listCookieInfo=DTL&pageCode=&codeDepth1Info=11000&keywordEtcYn=&publDutyExcYn=&keywordJobCdSeqNo=&exJobsCd=&templateDepthNmInfo=&computerPreferential=&regDateStdt=&employGbn=&empTpGbcd=&region=31000%7C48000&infaYn=&resultCntInfo=50&siteClcd=all&cloDateEndt=&sortOrderByInfo=ASC&currntPageNo=1&indArea=&careerTypes=&searchOn=Y&tlmgYn=&subEmpHopeYn=&academicGbn=&templateDepthNoInfo=&foriegn=&mealOfferClcd=&station=&moerButtonYn=Y&holidayGbn=&enterPriseGbn=all&academicGbnoEdu=noEdu&cloTermSearchGbn=all&keywordWantedTitle=N&stationNm=&benefitGbn=&keywordFlag=&essCertChk=&isEmptyHeader=&depth2SelCode=&_csrf=bc40e0e7-0796-42c8-bc00-5a03edf34cc4&keywordBusiNm=N&preferentialGbn=&rot3WorkYn=&pfMatterPreferential=&regDateEndt=&staAreaLineInfo1=11000&staAreaLineInfo2=1&pageIndex=1&termContractMmcnt=&careerFrom=&laborHrShortYn=#viewSPL'
url_li=[url_intern,url_normal]

for url in url_li:
    driver.get(url)

    if url==url_normal:
        if 일주일 == '1':
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[1]/div[2]/table/tbody/tr[16]/td/div/span[4]/input').click()
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[3]/div[4]/button').click()
            time.sleep(3)
        for emp in range(1,5):
            if emp ==1:
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[1]/div[1]/table/tbody/tr[6]/td[2]/div[1]/span['+str(emp)+']/input').click()
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[3]/div[4]/button').click()
            elif emp!=1:
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[1]/div[1]/table/tbody/tr[6]/td[2]/div[1]/span[' + str(emp-1) + ']/input').click()
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[1]/div[1]/table/tbody/tr[6]/td[2]/div[1]/span[' + str(emp) + ']/input').click()
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[3]/div[4]/button').click()
            last_page = int(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[3]/div').text.split(" ")[1])
            print(last_page)
            for a in range(1,int(last_page)+1):
                driver.find_element_by_css_selector('#currentPageNo').clear()
                driver.find_element_by_css_selector('#currentPageNo').send_keys(a)
                driver.find_element_by_css_selector('#currentPageNo').send_keys(Keys.ENTER)

                if driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[3]/div[1]/p[2]/em').text[0] == "-":
                    driver.refresh()
                    time.sleep(3)
                elif driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[3]/div[1]/p[2]/em').text[0] == "0":
                    continue
                else:
                    for j in range(0, len(driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr'))):

                        회사명데이터= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[2]").text.split('\n')
                        회사명=회사명데이터[0].replace("㈜","(주)")
                        print(회사명데이터)
                        채용데이터 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]").text.split('\n')
                        채용공고명=채용데이터[0]
                        if len(채용데이터)==1:
                            담당업무=""
                            지원자격=""
                            주소=""
                        elif len(채용데이터)==3:
                            담당업무=채용데이터[1]
                            if len(driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr['+str(j+1)+']/td[3]/div/p[2]/em'))==3:
                                지원자격 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p[2]/em[1]").text+","+driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p[2]/em[2]").text
                                주소=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p[2]/em[3]").text
                            elif len(driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr['+str(j+1)+']/td[3]/div/p[2]/em'))==2:
                                지원자격 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p[2]/em[1]").text
                                주소=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p[2]/em[2]").text
                        elif len(채용데이터)==2:
                            담당업무=""
                            if len(driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr['+str(j+1)+']/td[3]/div/p/em'))==3:
                                지원자격 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p/em[1]").text+","+driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p/em[2]").text
                                주소=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p/em[3]").text
                            elif len(driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr['+str(j+1)+']/td[3]/div/p/em'))==2:
                                지원자격 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p/em[1]").text
                                주소=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/p/em[2]").text
                        print(채용데이터)

                        근무조건 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr['+str(j+1)+']/td[4]/div').text
                        등록마감 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr['+str(j+1)+']/td[5]/div/p[2]').text
                        등록일 = 등록마감[0:9]
                        마감일 = 등록마감[12:20]
                        채용공고URL = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr["+str(j+1)+"]/td[3]/div/div/a").get_attribute('href')
                        if emp ==1:
                            고용형태='정규'
                        elif emp ==2:
                            고용형태='시간(장기)'
                        elif emp ==3:
                            고용형태='비정규'
                        elif emp ==4:
                            고용형태='시간(단기)'
                        회사명=회사명.replace("'","")
                        채용공고명 = 채용공고명.replace("'", "")
                        담당업무 = 담당업무.replace("'", "")
                        지원자격 = 지원자격.replace("'", "")
                        근무조건 = 근무조건.replace("'", "")
                        try:
                            정보제공처 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]'
                                                         '/table/tbody/tr['+str(j+1)+']/td[2]/div[@class="cp-certification mt20"]/span[@class="txt-certi"]').text.replace(" ","").replace("\n","")
                        except:
                            정보제공처 = driver.find_element_by_xpath(
                                '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]'
                                '/table/tbody/tr[' + str(
                                    j + 1) + ']/td[2]/div[@class="cp-certification mt20"]/span').text.replace(
                                " ", "").replace("\n", "")
                        if 정보제공처!='워크넷':
                            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr['+str(j+1)+']/td[3]/div/div/a').click()
                            try:
                                result = driver.switch_to_alert()
                                result.accept()
                            except:
                                pass
                            try:
                                time.sleep(2)
                                driver.switch_to_window(driver.window_handles[1])
                            except:
                                time.sleep(10)
                                driver.switch_to_window(driver.window_handles[1])
                            채용공고URL=driver.current_url
                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])
                        wr.writerow(
                            [회사명] + [채용공고명] + [담당업무] + [지원자격] + [주소] + [근무조건] + [등록일] + [마감일] + [채용공고URL] + [고용형태] + [
                                정보제공처])
                        print(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[3]/nav/strong').text,"페이지",j + 1, '번째 채용정보 완료',정보제공처)

                    print(time.time()-start)
    if url == url_intern:
        last_page = int(driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[3]/div').text.split(" ")[1])
        if driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[1]/p/strong').text!='0':

            print(last_page)
            for a in range(1, int(last_page) + 1):
                driver.find_element_by_css_selector('#currentPageNo').clear()
                driver.find_element_by_css_selector('#currentPageNo').send_keys(a)
                driver.find_element_by_css_selector('#currentPageNo').send_keys(Keys.ENTER)

                if driver.find_element_by_xpath(
                        '/html/body/div[1]/div[2]/div[2]/div/section/form[1]/div[3]/div[1]/p[2]/em').text[0] == "-":
                    driver.refresh()
                    time.sleep(3)
                else:

                    for j in range(0, len(driver.find_elements_by_xpath(
                            '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr'))):
                        회사명데이터 = driver.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                j + 1) + "]/td[2]").text.split('\n')
                        회사명 = 회사명데이터[0]
                        print(회사명데이터)
                        채용데이터 = driver.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                j + 1) + "]/td[3]").text.split('\n')
                        채용공고명 = 채용데이터[0]
                        if len(채용데이터) == 1:
                            담당업무 = ""
                            지원자격 = ""
                            주소 = ""
                        elif len(채용데이터) == 3:
                            담당업무 = 채용데이터[1]
                            if len(driver.find_elements_by_xpath(
                                    '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[' + str(
                                            j + 1) + ']/td[3]/div/p[2]/em')) == 3:
                                지원자격 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p[2]/em[1]").text + "," + driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p[2]/em[2]").text
                                주소 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p[2]/em[3]").text
                            elif len(driver.find_elements_by_xpath(
                                    '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[' + str(
                                            j + 1) + ']/td[3]/div/p[2]/em')) == 2:
                                지원자격 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p[2]/em[1]").text
                                주소 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p[2]/em[2]").text
                        elif len(채용데이터) == 2:
                            담당업무 = ""
                            if len(driver.find_elements_by_xpath(
                                    '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[' + str(
                                            j + 1) + ']/td[3]/div/p/em')) == 3:
                                지원자격 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p/em[1]").text + "," + driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p/em[2]").text
                                주소 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p/em[3]").text
                            elif len(driver.find_elements_by_xpath(
                                    '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[' + str(
                                            j + 1) + ']/td[3]/div/p/em')) == 2:
                                지원자격 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p/em[1]").text
                                주소 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                        j + 1) + "]/td[3]/div/p/em[2]").text
                        print(채용데이터)

                        근무조건 = driver.find_element_by_xpath(
                            '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[' + str(
                                j + 1) + ']/td[4]/div').text
                        등록마감 = driver.find_element_by_xpath(
                            '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[' + str(
                                j + 1) + ']/td[5]/div/p[2]').text
                        등록일 = 등록마감[0:9]
                        마감일 = 등록마감[12:20]
                        채용공고URL = driver.find_element_by_xpath(
                            "/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[" + str(
                                j + 1) + "]/td[3]/div/div/a").get_attribute('href')

                        고용형태 ='인턴'
                        회사명 = 회사명.replace("'", "")
                        채용공고명 = 채용공고명.replace("'", "")
                        담당업무 = 담당업무.replace("'", "")
                        지원자격 = 지원자격.replace("'", "")
                        try:
                            정보제공처 = driver.find_element_by_xpath(
                                '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]'
                                '/table/tbody/tr[' + str(
                                    j + 1) + ']/td[2]/div[@class="cp-certification mt20"]/span[@class="txt-certi"]').text.replace(
                                " ", "").replace("\n", "")
                        except:
                            정보제공처 = driver.find_element_by_xpath(
                                '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]'
                                '/table/tbody/tr[' + str(
                                    j + 1) + ']/td[2]/div[@class="cp-certification mt20"]/span').text.replace(
                                " ", "").replace("\n", "")
                        if 정보제공처 != '워크넷':
                            driver.find_element_by_xpath(
                                '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[2]/table/tbody/tr[' + str(
                                    j + 1) + ']/td[3]/div/div/a').click()
                            try:
                                result = driver.switch_to_alert()
                                result.accept()
                            except:
                                pass
                            try:
                                time.sleep(2)
                                driver.switch_to_window(driver.window_handles[1])
                            except:
                                time.sleep(10)
                                driver.switch_to_window(driver.window_handles[1])
                            채용공고URL = driver.current_url
                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])
                        wr.writerow(
                            [회사명] + [채용공고명] + [담당업무] + [지원자격] + [주소] + [근무조건] + [등록일] + [마감일] + [채용공고URL] + [고용형태] + [
                                정보제공처])

                        print(driver.find_element_by_xpath(
                            '/html/body/div[1]/div[2]/div[2]/div/section/form[2]/div[3]/nav/strong').text, "페이지", j + 1,
                              '번째 채용정보 완료',정보제공처)

                    print(time.time() - start)
        else:
            print('체험형없음')
            continue
gnus0=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/채용정보_경남울산_고용형태_최신화.csv",  encoding='UTF-8-sig')
for i in range(gnus0.shape[0]):
    for j in range(1,3):
        if str(gnus0.iloc[i,j]).find('체험형')!=-1 or str(gnus0.iloc[i,j]).find('인턴')!=-1:
            gnus0.iloc[i,9]='인턴'
for i in range(0,gnus0.shape[0]):
    if gnus0.iloc[i, 9] != '인턴':
        if gnus0.iloc[i,3][0:4]=='경력무관':
            gnus0.iloc[i, 3] = "경력무관삭제"
gnus0=gnus0[gnus0['지원자격']!="경력무관삭제"]

학력목록=['중졸','고졸','대졸(2~3년)']
for 학력 in 학력목록:
    for i in range(0,gnus0.shape[0]):
        if gnus0.iloc[i, 9] != '인턴':
            find_com_name = gnus0.iloc[i, 3].find(학력)
            if find_com_name != -1:
                gnus0.iloc[i, 3] = '학력미달삭제'
gnus0=gnus0[gnus0['지원자격']!="학력미달삭제"]

급여목록=['시급','월급','연봉']

for 급여 in 급여목록:
    for i in range(0,gnus0.shape[0]):
        if gnus0.iloc[i,9]!='인턴':
            if 급여==급여목록[0]:
                find_com_name = gnus0.iloc[i, 5].find(급여)
                if find_com_name != -1:
                    gnus0.iloc[i, 5] = '급여미달삭제'
            elif 급여==급여목록[1]:
                find_com_name = gnus0.iloc[i, 5].find(급여)
                if find_com_name != -1:
                    if int(gnus0.iloc[i, 5][3:6])<=200:
                        gnus0.iloc[i, 5] = '급여미달삭제'
            elif 급여==급여목록[2]:
                find_com_name = gnus0.iloc[i, 5].find(급여)
                if find_com_name != -1:
                    if int(gnus0.iloc[i, 5].split("만원")[0].replace(" ","").replace("연봉","").replace(",",""))<=3000:
                    # if int(gnus0.iloc[i, 5][3]+gnus0.iloc[i, 5][5:8])<=3000#253:
                        gnus0.iloc[i, 5] = '급여미달삭제'
gnus0=gnus0[gnus0['근무조건']!="급여미달삭제"]
d_company_li=['병원','의원','농장','학원','복지','사회','어린이집','요양보호사']
for d_company in d_company_li:
    for i in range(0,gnus0.shape[0]):
        if gnus0.iloc[i, 9] != '인턴':
            find_com_name=gnus0.iloc[i,0].find(d_company)
            if find_com_name!=-1:
                gnus0.iloc[i,0]='회사명 삭제'

d_employ_li=['조작원','작업자','기사모집','토목','건설','조선소','생산직','선원','농업','택시기사','정비원','경비원','인테리어','어린이집','사무원','보육교사','복지']
for d_employ in d_employ_li:
    for i in range(0,gnus0.shape[0]):
        if gnus0.iloc[i, 9] != '인턴':
            for j in range(1,3):
                try:
                    find_com_name=gnus0.iloc[i,j].find(d_employ)#1,2번째 열이 빈칸이 아닐경우
                except:
                    gnus0.iloc[i, j]=d_employ
                    find_com_name=gnus0.iloc[i,j].find(d_employ)#1,2번째 열이 빈칸일 경우
                if find_com_name!=-1:
                    print(gnus0.iloc[i,j])
                    gnus0.iloc[i,j]='채용공고 삭제'
gnus0=gnus0[gnus0['채용공고명']!="채용공고 삭제"]
gnus0=gnus0[gnus0['담당업무']!="채용공고 삭제"]
gnus0=gnus0[gnus0['회사명']!="회사명 삭제"]

gnus0.to_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/"+str(current_time.date())+"/채용정보_경남울산_고용형태_최신화_필터링완료.csv", encoding='UTF-8-sig',index=False)



df1=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/채용정보_경남울산_고용형태_최신화_필터링완료.csv')
for i in range(0,df1.shape[0]):
    if str(df1.iloc[i,7])=='nan':
        df1.iloc[i,7]='Null'

df1["select * from bio_pride_gyeongnam.tbl_job_info;\ndelete from bio_pride_gyeongnam.tbl_job_info where NUM>=1;\ninsert into bio_pride_gyeongnam.tbl_job_info (NUM, ZIP_NAME, COMP_NAME, APPLY_TITLE, JOB_POS, QUALIFY, CONDITIONS, ST_DT, END_DT, URL, EMPLOY_TYPE, INPUT_TYPE,RESOURCE_CODE)"]=''
df1['not']=''
for i in range(0,df1.shape[0]):
    df1.iloc[i, 4] = str(df1.iloc[i, 4]).replace('경남', '경상남도')
    df1.iloc[i, 4] = str(df1.iloc[i, 4]).replace('울산광역시 ', '울산 ')
    df1.iloc[i,4]  = str(df1.iloc[i, 4]).replace(' 등', '')
    df1.iloc[i, 4] = str(df1.iloc[i, 4]).replace('nan', '')
    for j in range(0,df1.shape[1]):
        if type(df1.iloc[i,j])=='str':
            df1.iloc[i,j]  = df1.iloc[i,j].replace('\n','')
    if df1.iloc[i,9]!='인턴':
        if (df1.iloc[i, 4][0:2] != '경상' and df1.iloc[i, 4][0:2] != '울산'):
            df1.iloc[i, 12] = '제거'
    elif df1.iloc[i,9]=='인턴':
        if (df1.iloc[i, 4][0:2] != '경상' and df1.iloc[i, 4][0:2] != '울산') and (str(df1.iloc[i,4])!='nan' and str(df1.iloc[i,4])!=''):
            df1.iloc[i, 12] = '제거'
df1 = df1.drop(df1[df1['not'] == '제거'].index)

code_table=pd.read_csv('C:/Users/82106/PycharmProjects/selenium/venv/코드테이블.csv',encoding = 'ISO-8859-1' )
code_list=['워크넷','잡코리아','사람인','잡알리오','인크루트','커리어']
print(code_table.shape)
for i in range(0,df1.shape[0]):

    if df1.iloc[i,10]=='워크넷':
        df1.iloc[i,10]='BP30050001'
    elif df1.iloc[i,10]=='잡코리아':
        df1.iloc[i,10]='BP30050003'
    elif df1.iloc[i,10]=='사람인':
        df1.iloc[i,10]='BP30050009'
    elif df1.iloc[i, 10] == '잡알리오':
        df1.iloc[i, 10] = 'BP30050013'
    elif df1.iloc[i, 10] == '인크루트':
        df1.iloc[i, 10] = 'BP30050014'
    elif df1.iloc[i, 10] == '커리어':
        df1.iloc[i, 10] = 'BP30050015'
    else:
        df1.iloc[i,10]='BP30050016'



for i in range(0,df1.shape[0]):
    if df1.iloc[i,4][0:4]=='경상남도':
        if df1.iloc[i,4][5:8]!='창원시':
            df1.iloc[i,11]=("("+str(df1.iloc[i,10])+",'"+df1.iloc[i,4][5:8]+"','"+df1.iloc[i,0]+"','"+df1.iloc[i,1]+"','"+str(df1.iloc[i,2])+
                    "','"+df1.iloc[i,3]+"','"+df1.iloc[i,5]+"','"+df1.iloc[i,6]+"','"+str(df1.iloc[i,7])+"','"+df1.iloc[i,8]+"','"+df1.iloc[i,9]+"','C','"+df1.iloc[i,10]+"'),")
        elif df1.iloc[i,4][5:8] == '창원시':
            df1.iloc[i,11]=("("+str(df1.iloc[i,10])+",'"+df1.iloc[i,4][5:]+"','"+df1.iloc[i,0]+"','"+df1.iloc[i,1]+"','"+str(df1.iloc[i,2])+
                    "','"+df1.iloc[i,3]+"','"+df1.iloc[i,5]+"','"+df1.iloc[i,6]+"','"+str(df1.iloc[i,7])+"','"+df1.iloc[i,8]+"','"+df1.iloc[i,9]+"','C','"+df1.iloc[i,10]+"'),")
    elif df1.iloc[i,4][0:2]=='울산':
        df1.iloc[i, 11] = ("("+str(df1.iloc[i,10])+",'"+df1.iloc[i,4][0:2]+"','"+df1.iloc[i,0]+"','"+df1.iloc[i,1]+"','"+str(df1.iloc[i,2])+
                    "','"+df1.iloc[i,3]+"','"+df1.iloc[i,5]+"','"+df1.iloc[i,6]+"','"+str(df1.iloc[i,7])+"','"+df1.iloc[i,8]+"','"+df1.iloc[i,9]+"','C','"+df1.iloc[i,10]+"'),")
    elif df1.iloc[i,9]=='인턴':
        df1.iloc[i,11]=("("+str(df1.iloc[i,10])+",'"+str(df1.iloc[i,4]).replace("nan","")+"','"+df1.iloc[i,0]+"','"+df1.iloc[i,1]+"','"+str(df1.iloc[i,2]).replace("nan","")+
                    "','"+str(df1.iloc[i,3]).replace("nan","")+"','"+df1.iloc[i,5]+"','"+df1.iloc[i,6]+"','"+str(df1.iloc[i,7])+"','"+df1.iloc[i,8]+"','"+df1.iloc[i,9]+"','C','"+df1.iloc[i,10]+"'),")
df1.iloc[0,11]='values'+df1.iloc[0,11]
df1.iloc[-1,11]=df1.iloc[-1,11][:-1]+";"

df1.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/채용정보_경남울산_고용형태_최신화_필터링완료_insert.csv',encoding='UTF-8-sig', index=False)

인턴 = open("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/" + str(current_time.date()) + "/채용정보_경남울산_인턴.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr1 = csv.writer(인턴)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr1.writerow(['회사명'] + ['채용공고명'] + ['담당업무'] + ['지원자격'] + ["주소"] + ["근무조건"] + ["등록일"] + ["마감일"] + ["채용공고URL"] + ['고용형태']+ ['정보제공처']+ ['"select * from bio_pride_gyeongnam.tbl_internship_info;\ndelete from bio_pride_gyeongnam.tbl_internship_info where NUM>=1;\ninsert into bio_pride_gyeongnam.tbl_internship_info (ZIP_NAME, COMP_NAME, APPLY_TITLE, JOB_POS, QUALIFY, CONDITIONS, ST_DT, END_DT, URL, EMPLOY_TYPE, INPUT_TYPE,RESOURCE_CODE)\nvalues"']+['not'])  # csv파일의 컬럼을 지정
정규등 = open("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/" + str(current_time.date()) + "/채용정보_경남울산_정규등.csv", 'w', newline='', encoding='UTF-8-sig')  # csv파일을 쓰기모드로 오픈
wr2 = csv.writer(정규등)  # 이것까지 해야 제대로된 csv파일로써 핸들링할수있음
wr2.writerow(['회사명'] + ['채용공고명'] + ['담당업무'] + ['지원자격'] + ["주소"] + ["근무조건"] + ["등록일"] + ["마감일"] + ["채용공고URL"] + ['고용형태']+ ['정보제공처']+ ['"select * from bio_pride_gyeongnam.tbl_job_info;\ndelete from bio_pride_gyeongnam.tbl_job_info where NUM>=1;\ninsert into bio_pride_gyeongnam.tbl_job_info (ZIP_NAME, COMP_NAME, APPLY_TITLE, JOB_POS, QUALIFY, CONDITIONS, ST_DT, END_DT, URL, EMPLOY_TYPE, INPUT_TYPE,RESOURCE_CODE)\nvalues"']+['not'])  # csv파일의 컬럼을 지정

for i in range(df1.shape[0]):
    if df1.iloc[i,9]=='인턴':
        wr1.writerow([df1.iloc[i,0]] + [df1.iloc[i,1]] + [df1.iloc[i,2]] + [df1.iloc[i,3]] + [df1.iloc[i,4]] + [df1.iloc[i,5]] + [df1.iloc[i,6]] +[df1.iloc[i,7]] + [df1.iloc[i,8]] + [df1.iloc[i,9]]+ [df1.iloc[i,10]]+ ["("+",".join(df1.iloc[i,11].split(",")[1:])]+ [df1.iloc[i,12]])
    elif df1.iloc[i,9]!='인턴':
        wr2.writerow([df1.iloc[i,0]] + [df1.iloc[i,1]] + [df1.iloc[i,2]] + [df1.iloc[i,3]] + [df1.iloc[i,4]] + [df1.iloc[i,5]] + [df1.iloc[i,6]] +[df1.iloc[i,7]] + [df1.iloc[i,8]] + [df1.iloc[i,9]]+ [df1.iloc[i,10]]+ ["("+",".join(df1.iloc[i,11].split(",")[1:])]+ [df1.iloc[i,12]])

time.sleep(10)
# df_i = pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/" + str(current_time.date()) + "/채용정보_경남울산_인턴.csv")
# df_j = pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/" + str(current_time.date()) + "/채용정보_경남울산_정규등.csv")
# if df_i.iloc[-1, 11][-1] == ',':
#     df_i.iloc[-1, 11] = df_i.iloc[df_i.shape[0]-1, 11][:-1]+";"
#
# if df_j.iloc[df_j.shape[0]-1, 11][-1] == ',':
#     df_j.iloc[df_j.shape[0]-1, 11] = df_j.iloc[df_j.shape[0]-1, 11][:-1]+";"
#
# df_i.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/채용정보_경남울산_인턴1.csv',encoding='UTF-8-sig', index=False)
# df_j.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/' + str(current_time.date()) + '/채용정보_경남울산_정규등1.csv',encoding='UTF-8-sig', index=False)