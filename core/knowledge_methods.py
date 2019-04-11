# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Knowledge semantic similarity methods
"""
import common
from lxml import html
import requests
import json
import io
import threading
import os
import numpy as np

def similarity_sentences(sent_1,sent_2, use_stop, use_pos, use_lem):
    """
    :param sent_1:
    :param sent_2:
    :param use_stop:
    :param use_pos:
    :param use_lem:
    :return: similarity between sent_1 and sent_2
    """
    matrices = common.preprocessing(sent_1,sent_2, use_stop, use_pos, use_lem)
    matrices = [fill_matrix(matrix, dictionary) for matrix in matrices]
    sim_list = [similarity_matrix(matrix) for matrix in matrices]
    return common.avg_list(sim_list)

def update_dictionary(dictionary, word):
    """
    :param dictionary:
    :param word:
    :return: dictionary updated with word
    """
    if(word not in dictionary):
        # print('Look up Azet!')
        url = 'https://slovnik.azet.sk/synonyma/?q=' + word
        page = requests.get(url)
        tree = html.fromstring(page.content)
        elems = tree.xpath('//em[@class="term"]')
        terms = [e.text_content() for e in elems]
        dictionary.update({word: terms})
    return dictionary

def fill_matrix(matrix, dictionary):
    """
    :param matrix:
    :param dictionary:
    :return: matrix filled with token similarities
    """
    if matrix is not None:
        for col in matrix.columns.values:
            for ind in matrix.index.values:
                dictionary = update_dictionary(dictionary, col)
                dictionary = update_dictionary(dictionary, ind)
                matrix.loc[ind, col] = similarity_tokens(col, ind, dictionary)
    return matrix

def similarity_tokens(token1, token2, dictionary):
    """
    :param token1:
    :param token2:
    :param dictionary:
    :return: similarity between token1 and token2
    """
    if token1 == token2 or token1 in dictionary[token2] or token2 in dictionary[token1]:
        return 1.0
    else:
        return 0.0

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

def jaccard_matrix(matrix):
    """
    :param matrix:
    :return: similarity based on synonyms and Jaccard index
    """
    if matrix is None:
        return None
    columns = [x for x in matrix.columns.values]
    index = [x for x in matrix.index.values]
    if not columns or not index:
        return 0.0

    for c, col in enumerate(matrix.columns.values):
        for i, ind in enumerate(matrix.index.values):
            isSynonym = float(matrix.iloc[i][col])
            # print(type(isSynonym),col,ind)
            # print((isSynonym))
            if(isSynonym):
                columns[c] = index[i]
    intersection = len(list(set(columns).intersection(index)))
    union = (len(columns) + len(index)) - intersection
    jaccard = float(intersection / union)
    return jaccard

def load_dictionary():
    """
    :return: cached dictionary of synonyms
    """
    try:
        with open('core/data/synonym_dictionary.json', 'r', encoding="utf8") as json_file:
            json_str = json_file.read()
            return json.loads(json_str)
    except FileNotFoundError:
        return dict()

def save_dictionary():
    """
    Save dictionary of synonyms to file
    """
    threading.Timer(300.0, save_dictionary).start()
    with io.open('core/data/synonym_dictionary.json', 'w', encoding='utf8') as json_file:
        json.dump(dictionary, json_file, ensure_ascii=False)

if(os.getcwd().split(os.sep)[-1] != 'tests'):
    dictionary = load_dictionary()
    save_dictionary()
else:
    dictionary = dict()
