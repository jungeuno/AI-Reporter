import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['titles'].values
word_index = dict()

for title in titles:
    words = title.split()
    for word in words:
        if word not in word_index:
            word_index[word] = len(word_index) + 1

print(word_index)