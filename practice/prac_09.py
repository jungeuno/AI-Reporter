import tensorflow as tf
import pandas as pd
import os

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()     # 공백 기준으로 토큰화함
                                                        # fit_on_texts() 메서드는 문자 데이터를 입력받아서 리스트의 형태로 변환
tokenizer.fit_on_texts(titles)                          # 토큰화된 data가 중복없이 (단어에 고유번호를 부여)저장됨
word_count = len(tokenizer.word_index) + 1              # '+1' - 시작번호를 0부터가 아닌 1부터로

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

x = []              #prac_04.py
y = []

for i in range(len(titles)):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]
    for j in range(1, len(sequence)):
        x.append(sequence[:j])
        y.append(sequence[j])

max_len = 0        # 토큰의 갯수가 가장 많은 수
for i in range(len(titles)):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]
    max_len = max(max_len, len(sequence))

pad_sequences = tf.keras.preprocessing.sequence.pad_sequences(x, maxlen=max_len)
categorical_y = tf.keras.utils.to_categorical(y, num_classes=word_count)    # y에 들어있는 가장 큰 길이값 +1 을 num_classes(=>word_count의 값인 42로 할당)로 하는 것이 효율적
                                                                            # 정답의 결과 수를 num_classes와 맞추어줘야함 (word_count로 맞춤)

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(word_count, 5),           # 단어의 종류 갯수 -> '3'
    tf.keras.layers.SimpleRNN(4),
    tf.keras.layers.Dense(word_count),
    tf.keras.layers.Softmax()                           # Softmax - Dense 레이어 기능에서 출력 값들의 합만 '1'이 되도록 바꿔줌, 파라미터도 없다.
])

loss = tf.keras.losses.CategoricalCrossentropy()                        #학습 코드 / loss => Crossentropy() - 분류 문제에서의 대표적인 손실함수
optimizer = tf.keras.optimizers.Adam(learning_rate=0.04)                #optimizers 최소화/최적화 작업 수행 함수/ 경사 하강 속도 (=learning_rate)
                                                                        #learning_rate 높일 수록 하강 속도가 빨라짐
model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])     #함수와 주체 연동 (=compile) / 정확도 확인 (=accuracy)

if not os.path.exists('../logs'):                                       #학습 로그를 저장하는 공간의 폴더 생성
    os.mkdir('../logs')

tensorboard = tf.keras.callbacks.TensorBoard(log_dir='../logs')                  #학습 과정 저장 (fit 함수를 실행 후의 과정)

model.fit(pad_sequences, categorical_y, epochs=1900, callbacks=[tensorboard])     #한 번 학습을 할 떄마다 콜백에 기능을 저장

if not os.path.exists('../models'):                                              #학습 완료된 모델 저장을 위한 공간의 폴더 생성
    os.mkdir('../models')

model.save('../models/test_prac.h5')                                             #해당 파일명으로 저장