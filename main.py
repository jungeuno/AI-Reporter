import pandas as pd

data = pd.read_csv('data/titles.csv')
titles = data['titles'].values          # 'titles' - titles.csv 파일의 제목!(맨상단)
word_index = dict()

for title in titles:
    words = title.split()
    for word in words:
        if word not in word_index:
            word_index[word] = len(word_index)

print(word_index)