#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import numpy as np
import json
import os

EMPTY_POS_TAGSET = ['default']
SIMPLE_POS_TAGSET = ['V','S','A']               # slovesá, podstatné, prídavné
FANCY_POS_TAGSET = ['V','S','A','P','N','D']    # slovesá, podstatné, prídavné, zámená, číslovky, príslovky

def preprocessing(sent_1,sent_2, use_stop, use_pos, use_lem):
    """
    :param sent_1:
    :param sent_2:
    :param use_stop:
    :param use_pos:
    :param use_lem:
    :return: list of matrix (one sper each POS tag)
    """
    analysed_sent_1 = sentence_analysis(sent_1, use_stop, use_lem)
    analysed_sent_2 = sentence_analysis(sent_2, use_stop, use_lem)

    pos_tagset = SIMPLE_POS_TAGSET if use_pos else EMPTY_POS_TAGSET
    categorized = categorize_sentences(analysed_sent_1, analysed_sent_2, pos_tagset)

    matrices = generate_matrices(categorized)
    return matrices

def sentence_analysis(sent, use_stop, use_lem):
    """
    :param sent:
    :param use_stop:
    :param use_lem:
    :return: list of {word:pos_tag}
    """
    analysed_sent = list()
    url = 'http://nlp.bednarik.top/lemmatizer/json'
    payload = {'input': sent, 'method': 'WITHPOS'}
    response = requests.post(url, data=payload)
    json_str = response.content.decode('utf-8')
    tree = json.loads(json_str)
    for part in tree['sentences']:
        for token in part['tokens']:
            word = token['lemma'] if use_lem else token['text']
            tag = token['tag'][0]
            if(use_stop) or (not use_stop and word not in stop_words):
                pair = {'word':word, 'tag':tag}
                analysed_sent.append(pair)
    return analysed_sent

def load_stop_words():
    """
    :return: dictionary of stop words
    """
    with open('core/data/stop_words_SK.txt', 'r', encoding='utf-8') as file:
        stop_words = set(word.rstrip() for word in file)
    return stop_words

def categorize_sentences(analysed_sent_1, analysed_sent_2, pos_tagset):
    """
    :param analysed_sent_1:
    :param analysed_sent_2:
    :param pos_tagset:
    :return: list of [words from 1, words from 2](one per each pos_tags)
    """
    splited = [[list(),list()] for _ in pos_tagset]
    analysed_sentences = [analysed_sent_1,analysed_sent_2]
    for i, analysed_sent in enumerate(analysed_sentences):
        for pair in analysed_sent:
            if pair['tag'] in pos_tagset:
                index = pos_tagset.index(pair['tag'])
                splited[index][i].append(pair['word'])
            if(len(pos_tagset) == 1):
                splited[0][i].append(pair['word'])
    # print(splited)
    return splited

def generate_matrices(categorized):
    """
    :param categorized:
    :return: list of empty matrices
    """
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

def similarity_matrix(matrix):
    """
    :param matrix:
    :return: aggregated similarity from matrix
    """
    if matrix is None:
        return None
    array = matrix.values
    long_len = max(array.shape)
    short_len = min(array.shape)
    count = 0
    for _ in range(short_len):
        i, j = np.unravel_index(array.argmax(), array.shape)
        count = count + array[i, j]
        array = np.delete(array, i, 0)
        array = np.delete(array, j, 1)
    return count/long_len

def similarity_matrices(matrices):
    """
    :param matrices:
    :return: average similarity of matrices
    """
    sim_list = [similarity_matrix(matrix) for matrix in matrices]

    sim_list = [x for x in sim_list if x is not None]
    suma = sum(sim_list)
    lenth = len(sim_list)
    if lenth == 0:
        return 0
    average = round(suma/lenth, 4)
    return average

if(os.getcwd().split(os.sep)[-1] != 'tests'):
    stop_words = load_stop_words()
else:
    stop_words = set(['a','i','aby'])