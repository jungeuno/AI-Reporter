import tensorflow as tf
                                                                #04.softmax 파일에서 넣어준 인풋에 따라 결과가 출력
model = tf.keras.models.load_model('../models/embedding.h5')    #embedding 모델 불러오기
predict_em = model.predict([[0, 1, 2],[0, 1, 2]])               #예측
print(predict_em)

model = tf.keras.models.load_model('../models/rnn.h5')          #rnn 모델 불러오기
predict_rnn = model.predict([[0, 1, 2]])                        #예측
print(predict_rnn)

model = tf.keras.models.load_model('../models/dense.h5')        #dense 모델 불러오기
predict_den = model.predict([[0, 1, 2]])                        #예측
print(predict_den)

model = tf.keras.models.load_model('../models/softmax.h5')      #softmax 모델 불러오기
predict_soft = model.predict([[0, 1, 2]])                       #예측
print(predict_soft)                                             #확률의 총 합이 '1'

