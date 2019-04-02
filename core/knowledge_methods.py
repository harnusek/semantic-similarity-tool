# -*- coding: utf-8 -*-

import common
from lxml import html
import requests
import json
import io
import threading
import os

def similarity_sentences(sent_1,sent_2, del_stop=False, use_pos=False, use_lem=False):
    """
    Return similarity between two sentences
    """
    tokens1 = common.lemmatization(sent_1)
    tokens2 = common.lemmatization(sent_2)
    matrices = common.generate_matrices(tokens1, tokens2)
    matrices = [fill_matrix(matrix, dictionary) for matrix in matrices]
    sim_list = [similarity_matrix_avg(matrix) for matrix in matrices]
    return common.avg_list(sim_list)

def update_dictionary(dictionary, word):
    """
    Return dictionary of token:synonyms
    """
    if(word not in dictionary):
        url = 'https://slovnik.azet.sk/synonyma/?q=' + word
        page = requests.get(url)
        tree = html.fromstring(page.content)
        elems = tree.xpath('//em[@class="term"]')
        terms = [e.text_content() for e in elems]
        dictionary.update({word: terms})
    return dictionary

def fill_matrix(matrix, dictionary):
    for col in matrix.columns.values:
        for ind in matrix.index.values:
            dictionary = update_dictionary(dictionary, col)
            dictionary = update_dictionary(dictionary, ind)
            matrix.loc[ind, col] = similarity_tokens(col, ind, dictionary)
    return matrix

def similarity_tokens(token1, token2, dictionary):
    set1 = set(dictionary[token1])
    set2 = set(dictionary[token2])
    set1.add(token1)
    set2.add(token2)
    if bool(set1 & set2):
        return 1.0
    else:
        return 0.0

def similarity_matrix_avg(matrix):
    array = matrix.values
    count = 0
    for line in array:
        for cell in line:
            count = count + cell
    return count/array.size

def similarity_matrix_X(matrix):
    array = matrix.values
    count = 0
    for line in array:
        count = count+max(line)
    return count/len(array)

def load_dictionary():
    try:
        with open('core/data/synonym_dictionary.json', 'r', encoding="utf8") as json_file:
            json_str = json_file.read()
            return json.loads(json_str)
    except FileNotFoundError:
        return dict()

def save_dictionary():
    threading.Timer(300.0, save_dictionary).start()
    with io.open('core/data/synonym_dictionary.json', 'w', encoding='utf8') as json_file:
        json.dump(dictionary, json_file, ensure_ascii=False)
        # print('[SAVE] synonym_dictionary.json')

dictionary = dict()
if(os.getcwd().split(os.sep)[-1] != 'tests'):
    dictionary = load_dictionary()
    save_dictionary()
