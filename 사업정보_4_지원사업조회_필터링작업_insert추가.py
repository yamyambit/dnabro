import pandas as pd
import datetime

current_time=datetime.datetime.now()
df_list=['지원사업조회_기업마당_최신화','지원사업조회_NTIS_최신화']
df2=pd.read_csv("C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/코드테이블2.csv", encoding='euc-kr')
for df_i in df_list:
    df=pd.read_excel('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/'+df_i+'.xls')
    print(df_i)
    if df_i == df_list[0]:

        df.columns = df.iloc[1, :]
        df = df.iloc[2:, :]
        df = df.sort_values(by=['번호'], axis=0)
        df = df.sort_values(by=['신청시작일'], axis=0)
        df['insert'] = ''
        df['부처코드'] = ''
        for a in range(0,df.shape[0]):
            for j in range(df2.shape[0]):
                if df.iloc[a,8]==df2.iloc[j,4]:
                    df.iloc[a,14]=df2.iloc[j,0]
            if df.iloc[a,14]!='':
                df.iloc[a,13]="('"+df.iloc[a,14]+"','"+df.iloc[a,9]+"','"+df.iloc[a,2]+"','"+\
                            str(df.iloc[a,5])[0:4]+"-"+str(df.iloc[a,5])[4:6]+"-"+str(df.iloc[a,5])[6:]+\
                            "','"+str(df.iloc[a,6])[0:4]+"-"+str(df.iloc[a,6])[4:6]+"-"+str(df.iloc[a,6])[6:]+"','"+df.iloc[a,4]+"','C','BP30050018'),"
            elif df.iloc[a,14]=='':
                df.iloc[a, 13] = "('" + df.iloc[a, 8] + "','" + df.iloc[a, 9] + "','" + \
                                 df.iloc[a, 2] + "','" + \
                                 str(df.iloc[a, 5])[0:4] + "-" + str(df.iloc[a, 5])[4:6] + "-" + str(df.iloc[a, 5])[
                                                                                                 6:] + \
                                 "','" + str(df.iloc[a, 6])[0:4] + "-" + str(df.iloc[a, 6])[4:6] + "-" + str(
                    df.iloc[a, 6])[6:] + "','" + df.iloc[a, 4] + "','C','BP30050018'),"

    elif df_i == df_list[1]:
        df = df.sort_values(by=['순번'], axis=0)
        df = df.sort_values(by=['접수일'], axis=0)
        df['insert'] = ''
        df['부처코드'] = ''
        for a in range(0,df.shape[0]):
            for j in range(df2.shape[0]):
                if df.iloc[a,3]==df2.iloc[j,4]:
                    df.iloc[a,16]=df2.iloc[j,0]
            df.iloc[a,15]="('"+str(df.iloc[a,16])+"','"+df.iloc[a,9]+"','"+df.iloc[a,4].replace("'","")+"','"+str(df.iloc[a,5])[0:4]+'-'+str(df.iloc[a,5])[5:7]+'-'+str(df.iloc[a,5])[8:]\
                          +"','"+str(df.iloc[a,6])[0:4]+'-'+str(df.iloc[a,6])[5:7]+'-'+str(df.iloc[a,6])[8:]+"','"+str(df.iloc[a,11])+"','C','BP30050005'),"
    org_li=['경찰청','국방부','농촌진흥청','문화재청','문화체육관광부','산림청','식품의약품안전처','외교부','원자력안전위원회','질병관리청']
    business_li=['용역','융자','마케팅','참가기업','참여기업','참가 기업','참여 기업']
    if df_i == df_list[0]:
        for org in org_li:
            for i in range(0,df.shape[0]):
                find_com_name1=df.iloc[i,8].find(org)
                if find_com_name1 != -1:
                    df.iloc[i, 2] = '사업공고 삭제'
        for business in business_li:
            for i in range(0,df.shape[0]):
                find_com_name2=df.iloc[i,2].find(business)
                if find_com_name2 != -1:
                    df.iloc[i, 2] = '사업공고 삭제'
        df = df[df['지원사업명'] != "사업공고 삭제"]

        print(df.shape)

    elif df_i == df_list[1]:
        for org in org_li:
            for i in range(0,df.shape[0]):
                if  type(df.iloc[i,3])!=float:
                    find_com_name1=df.iloc[i,3].find(org)
                if find_com_name1 != -1 or type(df.iloc[i,3])==float:
                    df.iloc[i, 4] = '사업공고 삭제'
        for business in business_li:
            for i in range(0,df.shape[0]):
                find_com_name2=df.iloc[i,4].find(business)
                if find_com_name2 != -1:
                    df.iloc[i, 4] = '사업공고 삭제'
        df = df[df['공고명'] != "사업공고 삭제"]
    df.to_csv('C:/Users/82106/PycharmProjects/selenium/venv/정보화 홈페이지DB/'+str(current_time.date())+'/'+df_i+'_insert.csv',encoding='UTF-8-sig', index=False)
