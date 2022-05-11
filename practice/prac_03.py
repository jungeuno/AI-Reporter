# sequence, slice를 활용해서 정수 인덱스로 변환한 뉴스 제목 sequence를 아래 예시처럼 x, y로 분리해서 저장
import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

x = []
y = []

for i in range(len(titles)):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]
    for j in range(1, len(sequence)):
        x.append(sequence[:j])
        y.append(sequence[j])

print(x)
print()
print(y)



