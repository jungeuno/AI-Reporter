import tensorflow as tf

model = tf.keras.models.load_model('../models/embedding.h5')    #embedding 모델 불러오기
model.summary()

model = tf.keras.models.load_model('../models/rnn.h5')          #rnn 모델 불러오기
model.summary()

model = tf.keras.models.load_model('../models/dense.h5')        #dense 모델 불러오기
model.summary()

model = tf.keras.models.load_model('../models/softmax.h5')      #softmax 모델 불러오기
model.summary()