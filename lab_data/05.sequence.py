import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)
print(tokenizer.word_index)

print(titles)                                                #실행 전 test
print([titles[0],titles[3]])
print(tokenizer.texts_to_sequences([titles[0],titles[3]]))

sequence = tokenizer.texts_to_sequences([titles[0]])[0]      #텍스트 여러개를 복수형 반환/ 하나([0])만 리스트로 넘겨서 하나([[0])를 받아옴
print(titles[0])                                             #문장들을 숫자(행렬 또는 벡터) 형태로 변환/ 컴퓨터가 계산하기 편하도록 변환(인코딩)
print(sequence)