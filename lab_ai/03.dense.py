import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(3, 5),
    tf.keras.layers.SimpleRNN(4),
    tf.keras.layers.Dense(6)
])

model.summary()