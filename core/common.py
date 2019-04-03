# -*- coding: utf-8 -*-

import requests
import pandas as pd
import json

POS_TAGSET = ['default','P','V','S','Z']

def preprocessing(sent_1,sent_2, use_stop, use_pos, use_lem):
    analysed_sent_1 = sentence_analysis(sent_1, use_stop, use_lem)
    analysed_sent_2 = sentence_analysis(sent_2, use_stop, use_lem)
    if(use_pos):
        categorized = categorize_sentences(analysed_sent_1, analysed_sent_2, POS_TAGSET)
    else:
        categorized = categorize_sentences(analysed_sent_1, analysed_sent_2, ['default'])
    matrices = generate_matrices(categorized)
    return matrices

def sentence_analysis(sent, use_stop, use_lem):
    analysed_sent = list()
    url = 'http://nlp.bednarik.top/lemmatizer/json'
    payload = {'input': sent, 'method': 'WITHPOS'}
    response = requests.post(url, data=payload)
    json_str = response.content.decode('utf-8')
    # print(json_str)
    # return
    tree = json.loads(json_str)
    for part in tree['sentences']:
        for token in part['tokens']:
            # needs test stop words
            word = token['lemma'] if use_lem else token['text']
            tag = token['tag'][0] # needs simplify
            pair = {'word':word, 'tag':tag}
            analysed_sent.append(pair)
    return analysed_sent

# def is_stop_word(word):
#     with open('core/data/stop_words_SK.txt', 'r', encoding='utf-8') as file:
#         stop_words = [word.rstrip() for word in file]
#         filtered_words = [word for word in words if word not in stop_words]
#         return filtered_words

def categorize_sentences(analysed_sent_1, analysed_sent_2, categories):
    splited = [[list(),list()] for _ in categories]
    for pair in analysed_sent_1:
        index = 0
        if pair['tag'] in categories:
            index = categories.index(pair['tag'])
        # print(pair['word'], pair['tag'], index, splited[index])
        splited[index][0].append(pair['word'])
    for pair in analysed_sent_2:
        index = 0
        if pair['tag'] in categories:
            index = categories.index(pair['tag'])
        splited[index][1].append(pair['word'])
    return splited

def generate_matrices(categorized):
    matrices = list()
    for columns, index in categorized:
        if(len(columns)>0 and len(index)>0):
            df = pd.DataFrame(columns=columns, index=index)
            df = df.apply(pd.to_numeric, errors='coerce')
            matrices.append(df)
        else:
            matrices.append(None)
    return matrices

# post
def avg_list(list):
    suma = sum([i for i in list if i is not None])
    lenth = len([i for i in list if i is not None])
    average = round(suma/lenth, 4)
    return average