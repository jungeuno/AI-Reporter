import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('../models/softmax.h5')      #모델 불러오기

predict = model.predict([[0, 1, 2]])                            #예측
print(predict)

index_word = ['가', '나', '다', '라', '마', '바']                 #index_word -> 인덱스를 단어로 변환

index = np.argmax(predict[0])                                   #해당 값의 인덱스를 출력 / argmax()

print(index)
print(index_word[index])

# predict 사용 이유? / 실데 output 결과와 예측을 비교해서 학습하기 위함?
# model.predict() 괄호 안의 배열 의미 / argmax() 안에 의미 / 결과 6개는 어떤 것? 아웃풋 개수?
