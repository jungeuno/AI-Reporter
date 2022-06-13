import tensorflow as tf
import os

index_to_word = ['가', '나', '다', '라']

# 가나다/라, 다나가/가
x = [[0, 1, 2], [2, 1, 0]]
y = [[0, 0, 0, 1], [1, 0, 0, 0]]

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(4, 5),
    tf.keras.layers.SimpleRNN(3),
    tf.keras.layers.Dense(4),
    tf.keras.layers.Softmax()
])

loss = tf.keras.losses.CategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])

if not os.path.exists('../logs'):                                       #학습 로그를 저장하는 공간의 폴더 생성
    os.mkdir('../logs')

tensorboard = tf.keras.callbacks.TensorBoard(log_dir='../logs')         #학습 과정 저장 (fit 함수를 실행 후의 과정)

model.fit(x, y, epochs=100, callbacks=[tensorboard])                    #한 번 학습을 할 떄마다 콜백에 기능을 저장

if not os.path.exists('../models'):                                     #학습 완료된 모델 저장을 위한 공간의 폴더 생성
    os.mkdir('../models')

model.save('../models/test.h5')                                         #해당 파일명으로 저장