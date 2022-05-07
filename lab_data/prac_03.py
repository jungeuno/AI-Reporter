import numpy as np
import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

sequence = tokenizer.texts_to_sequences([titles[0]])[0]      #텍스트 여러개를 복수형 반환/ 하나([0])만 리스트로 넘겨서 하나([[0])를 받아옴
print(titles[0])
print(sequence)
print(len(sequence))

s_length = len(sequence)

# for x in s_length:
#     print(sequence[:x])

