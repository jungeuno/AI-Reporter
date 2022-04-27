import pandas as pd
import os

if not os.path.exists('../data'):   #상위 폴더안에 data 폴더가 없다면 새로 생성
    os.mkdir('../data')

titles = ['제목 1','제목 2','제목 3']

data = pd.DataFrame({'titles': titles})
data.to_csv('../data/titles.csv', encoding='utf-8') #괄호 앞: 파일 저장 경로/뒤:한글포함되어 있으면 인코딩 주의
