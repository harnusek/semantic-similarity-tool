# -*- coding: utf-8 -*-

import requests
import pandas as pd
import json

POS_TAGSET = ['default','S','V','A']

def preprocessing(sent_1,sent_2, del_stop, use_pos, use_lem):
    analysed_sent_1 = sentence_analysis(sent_1, del_stop, use_lem)
    analysed_sent_2 = sentence_analysis(sent_2, del_stop, use_lem)
    if(use_pos):
        splited = split_pos(analysed_sent_1, analysed_sent_2, POS_TAGSET)
    else:
        splited = split_pos(analysed_sent_1, analysed_sent_2, ['default'])

def sentence_analysis(sent, del_stop=False, use_lem=False):
    analysed_sent = list()
    url = 'http://nlp.bednarik.top/lemmatizer/json'
    payload = {'input': sent, 'method': 'WITHPOS'}
    response = requests.post(url, data=payload)
    json_str = response.content.decode('utf-8')
    tree = json.loads(json_str)
    for part in tree['sentences']:
        for token in part['tokens']:
            # needs test stop words
            word = token['lemma'] if use_lem else token['text']
            tag = token['tag'] # needs simplify
            pair = {'word':word, 'tag':tag}
            analysed_sent.append(pair)
    return analysed_sent

# def lemmatization(sent):
#     response = requests.post(url='http://text.fiit.stuba.sk:8080/lematizer/services/lemmatizer/lemmatize/fast', data=sent.encode('utf-8'))
#     str = response.content.decode("utf-8")
#     tokens = str.split(' ')
#     return tokens

# def remove_stop_words(words):
#     with open('core/data/stop_words_SK.txt', 'r', encoding='utf-8') as file:
#         stop_words = [word.rstrip() for word in file]
#         filtered_words = [word for word in words if word not in stop_words]
#         return filtered_words

def split_pos(analysed_sent_1, analysed_sent_2, categories):
    splited = [[[],[]]] * size(categories)
    for pair in analysed_sent_1:
        index = categories.index(pair['tag'])
        splited[index][0] = pair['word']
    for pair in analysed_sent_2:
        index = categories.index(pair['tag'])
        splited[index][1] = pair['word'
    return splited

def generate_matrices(tokens1, tokens2): # TODO pos tags
    for tag in tag_list:
        df = pd.DataFrame(columns=tokens1, index=tokens2)
        df = df.apply(pd.to_numeric, errors='coerce')
        matrices.append(df)
    return matrices

# post
def avg_list(list):
    return sum(list)/len(list)