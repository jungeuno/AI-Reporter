# tokenize를 활용해서 도전과제 1에서 수집한 뉴스 제목 문장을 구성하는 단어에 정수 인덱스 부여
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values
word_index = dict()

for title in titles:
    words = title.split()
    for word in words:
        if word not in word_index:
            word_index[word] = len(word_index) + 1

print(word_index)