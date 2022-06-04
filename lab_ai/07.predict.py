import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('../models/softmax.h5')      #모델 불러오기

predict = model.predict([[0, 1, 2]])                            #예측
print(predict)                                                  #predict(input값) => y' (= 결과 예측값)
                                                                #최종 결과값과 예측값의 비교 후 파라미터 조정 => '학습'
index_word = ['가', '나', '다', '라', '마', '바']                 #index_word -> 인덱스를 단어로 변환

index = np.argmax(predict[0])                                   #해당 값의 인덱스를 출력 / argmax() - 배열의 확률 중에서 가장 큰 값

print(index)
print(index_word[index])
