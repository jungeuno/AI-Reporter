# prac_03에서 구한 x 데이터와 y 데이터에 각각 pad_sequence, to_categorical 적용
import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

x = []
y = []

for i in range(len(titles)):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]
    for j in range(1, len(sequence)):
        x.append(sequence[:j])
        y.append(sequence[j])

max_len = 0        # 토큰의 갯수가 가장 많은 수

for i in range(len(titles)):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]
    max_len = max(max_len, len(sequence))

pad_sequences = tf.keras.preprocessing.sequence.pad_sequences(x, maxlen=max_len)
print(pad_sequences)

categorical_y = tf.keras.utils.to_categorical(y, num_classes=50)    # y에 들어있는 가장 큰 길이값 +1 을 num_classes로 하는 것이 효율적
print(categorical_y)                                                # 임의로 50으로 할당
