import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

sequences = []
max_len = 0        #토큰의 갯수가 가장 많은 수를 저장해둘 변수

for i in range(len(titles)):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]  # 텍스트 여러 개를 복수형 반환/ 하나([0])만 리스트로 넘겨서 하나([[0])를 받아옴
    sequences.append(sequence)
    max_len = max(max_len, len(sequence))
    print(titles[i])
    print(sequence)
    print(max_len)

pad_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_len)     #패딩 과정 / 연산이 가능하도록 함, 정확도 높임
print(pad_sequences)