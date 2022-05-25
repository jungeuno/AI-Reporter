import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('../models/softmax.h5')      #모델 불러오기

predict = model.predict([[0, 1, 2]])                            #예측
print(predict)

index_word = ['가', '나', '다', '라', '마', '바']

index = np.argmax(predict[0])                                   #해당 값의 인덱스를 출력 / argmax()

print(index)
print(index_word[index])