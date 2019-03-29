# -*- coding: utf-8 -*-

import preprocessing
from lxml import html
import requests
import pandas as pd
from lxml.etree import tostring

def get_similarity(sent1,sent2):
    """
    Return similarity between two sentences
    """
    tokens1 = preprocessing.tokenize(sent1)
    tokens2 = preprocessing.tokenize(sent2)
    words = set(tokens1).union(set(tokens2))
    dictionary = synonym_dict(words)
    matrices = generate_matrices(tokens1, tokens2)
    for matrix in matrices:
        matrix = fill_matrix(matrix, dictionary)

    return sim_by_matrix(tokens1, tokens2)

def synonym_dict(words):
    """
    Return dictionary of token:synonyms
    """
    dictionary = dict()
    for word in words:
        url = 'https://slovnik.azet.sk/synonyma/?q=' + word
        page = requests.get(url)
        tree = html.fromstring(page.content)
        elems = tree.xpath('//em[@class="term"]')
        terms = [e.text_content() for e in elems]
        dictionary.update({word: terms})
    return dictionary

def generate_matrices(tokens1, tokens2):
    matrices = list()
    for _ in range(1):
        matrices.append(pd.DataFrame(columns=tokens1, index=tokens2))
    return matrices

def fill_matrix(matrix, dictionary):
    matrix = matrix.fillna(0)
    return matrix

def sim_by_matrix(matrix):
    points = 0
    for x in xList:
        for y in yList:
            points = points + sim_by_tokens(x,y)
    return points

def sim_by_tokens(token1, token2, dictionary):
    if any(elem in synonym_list(x) for elem in synonym_list(y)):
        return 1
    else:
        return 0