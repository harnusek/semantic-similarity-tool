# -*- coding: utf-8 -*-

import requests
import pandas as pd

def avg_list(list):
    return sum(list)/len(list)

def tokenize(sent):
    response = requests.post(url='http://text.fiit.stuba.sk:8080/lematizer/services/lemmatizer/lemmatize/fast', data=sent.encode('utf-8'))
    str = response.content.decode("utf-8")
    tokens = str.split(' ')
    return tokens

def remove_stop_words(words):
    with open('core/data/stop_words_SK.txt', 'r', encoding='utf-8') as file:
        stop_words = [word.rstrip() for word in file]
        filtered_words = [word for word in words if word not in stop_words]
        return filtered_words

def generate_matrices(tokens1, tokens2): # TODO pos tags
    matrices = list()
    for _ in range(1):
        df = pd.DataFrame(columns=tokens1, index=tokens2)
        df = df.apply(pd.to_numeric, errors='coerce')
        matrices.append(df)
    return matrices

def similarity_avg(matrix):
    array = matrix.values
    count = 0
    for line in array:
        for cell in line:
            count = count + cell
    return count/array.size

def similarity_X(matrix):
    array = matrix.values
    count = 0
    for line in array:
        count = count+max(line)
    return count/len(array)