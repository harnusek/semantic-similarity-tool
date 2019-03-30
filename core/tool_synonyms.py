# -*- coding: utf-8 -*-

import common
from lxml import html
import requests

def get_similarity(sent1,sent2):
    """
    Return similarity between two sentences
    """
    tokens1 = common.tokenize(sent1)
    tokens2 = common.tokenize(sent2)
    words = set(tokens1).union(set(tokens2))
    dictionary = synonym_dictionary(words)
    matrices = common.generate_matrices(tokens1, tokens2)
    for matrix in matrices:
        matrix = fill_matrix(matrix, dictionary)
        return common.similarity_avg(matrix)

def synonym_dictionary(words):
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

def fill_matrix(matrix, dictionary):
    for col in matrix.columns.values:
        for ind in matrix.index.values:
            matrix.loc[ind, col] = similarity_tokens(col, ind, dictionary)
            # matrix[col][ind] = similarity_tokens(col, ind, dictionary)
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