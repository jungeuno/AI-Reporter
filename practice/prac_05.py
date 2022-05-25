import tensorflow as tf
import os

model = tf.keras.models.Sequential([    #dense
    tf.keras.layers.Embedding(3, 5),
    tf.keras.layers.SimpleRNN(4),
    tf.keras.layers.Dense(6)
])
if not os.path.exists('../models'):     #'models' 디렉토리 경로가 존재하지 않는다면
    os.mkdir('../models')               #'models' 디렉토리 새로 생성
model.save('../models/dense.h5')        #디렉토리에 모델을 저장


model = tf.keras.models.Sequential([    #rnn
    tf.keras.layers.Embedding(3, 5),
    tf.keras.layers.SimpleRNN(4)
])
if not os.path.exists('../models'):
    os.mkdir('../models')
model.save('../models/rnn.h5')


model = tf.keras.models.Sequential([    #embedding
    tf.keras.layers.Embedding(3, 5)
])
if not os.path.exists('../models'):
    os.mkdir('../models')
model.save('../models/embedding.h5')
