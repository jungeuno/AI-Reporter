import tensorflow as tf

model = tf. keras.models.Sequential([
    tf.keras.layers.Embedding(3, 15)
])

model.summary()         # 모델의 정보를 출력
