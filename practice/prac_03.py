# sequence, slice를 활용해서 정수 인덱스로 변환한 뉴스 제목 sequence를 x, y로 분리해서 저장
import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()              # 공백 기준으로 토큰화함
tokenizer.fit_on_texts(titles)

x = []
y = []

for i in range(len(titles)):
    sequence = tokenizer.texts_to_sequences([titles[i]])[0]      # 텍스트 여러 개를 복수형 반환/ 하나([0])만 리스트로 넘겨서 하나([[0])를 받아옴
    for j in range(1, len(sequence)):
        x.append(sequence[:j])
        y.append(sequence[j])

print(x)
print()
print(y)



