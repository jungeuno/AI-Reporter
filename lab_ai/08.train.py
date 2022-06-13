import tensorflow as tf
import numpy as np

index_word = ['가', '나', '다', '라']

# 가나다/라, 다나가/가
x = [[0, 1, 2], [2, 1, 0]]                  #학습데이터 예시로 설정
y = [[0, 0, 0, 1], [1, 0, 0, 0]]

model = tf.keras.models.Sequential([        #모델 생성
    tf.keras.layers.Embedding(4, 5),        #임베딩 첫번째 숫자는 단어의 갯수 (=4개) / word_count
    tf.keras.layers.SimpleRNN(6),
    tf.keras.layers.Dense(4),               #임베딩 레이어와 맞추어줌 / 나머지 모델의 숫자는 자유롭게 설정 가능
    tf.keras.layers.Softmax()
])
model.summary()

predict = model.predict([[0, 1, 2]])        #학습데이터를 바탕으로 결과 예측
print(predict)                              #예측 결과 확인

loss = tf.keras.losses.CategoricalCrossentropy()                        #학습 코드 / loss => Crossentropy() - 분류 문제에서의 대표적인 손실함수
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)                #optimizers 최소화/최적화 작업 수행 함수/ 경사 하강 속도 (=learning_rate)
                                                                        #learning_rate 높일 수록 하강 속도가 빨라짐
model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])     #함수와 주체 연동 (=compile) / 정확도 확인 (=accuracy)
model.fit(x, y, epochs=100)                                             #실제 학습 / 경사 하강 횟수 (=epoch)- x에 해당되는 전체 데이터를 모두 학습

predict = model.predict([[0, 1, 2]])
print(predict)

index = np.argmax(predict[0])
print(index)
print(index_word[index])

predict = model.predict([[2, 1, 0]])
print(predict)

index = np.argmax(predict[0])
print(index)
print(index_word[index])