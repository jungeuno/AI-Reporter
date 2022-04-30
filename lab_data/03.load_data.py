import pandas as pd

data = pd.read_csv('../data/titles.csv')    #titles.csv 파일의 내용을 읽기
print(data)

titles = data['titles'].values              #data 배열에 저장된 기사 제목들을 .values 통해서 순수 제목만 추출해서 리스트 형식으로 출력
print(titles)