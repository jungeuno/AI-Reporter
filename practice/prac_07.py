import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()     # 공백 기준으로 토큰화함
print(tokenizer.word_index)
                                                        # fit_on_texts() 메서드는 문자 데이터를 입력받아서 리스트의 형태로 변환
tokenizer.fit_on_texts(titles)                          # 토큰화된 data가 중복없이 (단어에 고유번호를 부여)저장됨
word_count = len(tokenizer.word_index) + 1              # '+1' - 시작번호를 0부터가 아닌 1부터로

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(word_count, 5),           # 단어의 종류 갯수 -> '3'
    tf.keras.layers.SimpleRNN(4),
    tf.keras.layers.Dense(word_count),
    tf.keras.layers.Softmax()                           # Dense 에서 합만 '1'로 바꿔줌, 파라미터도 없다.
])
model.summary()

predict = model.predict([[0, 1, 2]])                    # 예측
print(predict)                                          # 합이 '1'인 42개의 1차원 배열이 출력된다.
