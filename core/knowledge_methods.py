#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Knowledge semantic similarity methods
"""
from common import preprocessing
from common import similarity_matrices
from lxml import html
import requests
import json
import io
import threading
import os

def similarity_sentences(sent_1,sent_2, use_stop, use_pos, use_lem):
    """
    :param sent_1:
    :param sent_2:
    :param use_stop:
    :param use_pos:
    :param use_lem:
    :return: similarity between sent_1 and sent_2
    """
    matrices = preprocessing(sent_1,sent_2, use_stop, use_pos, use_lem)
    matrices = [fill_matrix(matrix, dictionary) for matrix in matrices]
    similarity = similarity_matrices(matrices)
    return similarity

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

def load_dictionary():
    """
    :return: cached dictionary of synonyms
    """
    try:
        with open('core/sources/synonym_dictionary.json', 'r', encoding="utf8") as json_file:
            json_str = json_file.read()
            return json.loads(json_str)
    except FileNotFoundError:
        return dict()

def save_dictionary():
    """
    Save dictionary of synonyms to file
    """
    threading.Timer(300.0, save_dictionary).start()
    with io.open('core/sources/synonym_dictionary.json', 'w', encoding='utf8') as json_file:
        json.dump(dictionary, json_file, ensure_ascii=False)

if(os.getcwd().split(os.sep)[-1] != 'tests'):
    dictionary = load_dictionary()
    save_dictionary()
else:
    dictionary = dict()
