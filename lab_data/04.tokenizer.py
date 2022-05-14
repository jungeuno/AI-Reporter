import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

print(titles)

tokenizer = tf.keras.preprocessing.text.Tokenizer()     # 공백 기준으로 토큰화함
print(tokenizer.word_index)
                                                        # fit_on_texts() 메서드는 문자 데이터를 입력받아서 리스트의 형태로 변환
tokenizer.fit_on_texts(titles)                          # 토큰화된 data가 중복없이 (단어에 고유번호를 부여)저장됨
word_count = len(tokenizer.word_index) + 1              # '+1' - 시작번호를 0부터가 아닌 1부터로

print(tokenizer.word_index)                             # tokenizer의 word_index - 단어와 숫자의 키-값 쌍을 포함하는 딕셔너리를 반환
print(word_count)