import tensorflow as tf

data = [0, 1, 2, 3]
                                                                           # 원-핫 인코딩
categorical_data = tf.keras.utils.to_categorical(data, num_classes=6)      # 0부터 6까지의 '0' 중에서 해당 되는 위치에만 '1'로 표현함
print(categorical_data)                                                    # 확률로 나타낸 것! / 확률이 가장 높은 것을 1로 표현
