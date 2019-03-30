# -*- coding: utf-8 -*-

import preprocessing
from lxml import html
import requests
import pandas as pd

def get_similarity(sent1,sent2):
    """
    Return similarity between two sentences
    """
    tokens1 = preprocessing.tokenize(sent1)
    tokens2 = preprocessing.tokenize(sent2)
    words = set(tokens1).union(set(tokens2))
    dictionary = synonym_dictionary(words)
    matrices = generate_matrices(tokens1, tokens2)
    for matrix in matrices:
        matrix = fill_matrix(matrix, dictionary)
        return similarity_matrix(matrix)

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

def generate_matrices(tokens1, tokens2):
    matrices = list()
    for _ in range(1):
        df = pd.DataFrame(columns=tokens1, index=tokens2)
        df = df.apply(pd.to_numeric, errors='coerce')
        matrices.append(df)
    return matrices

def fill_matrix(matrix, dictionary):
    for col in matrix.columns.values:
        for ind in matrix.index.values:
            matrix.loc[ind, col] = similarity_tokens(col, ind, dictionary)
            # matrix[col][ind] = similarity_tokens(col, ind, dictionary)
    return matrix

def similarity_matrix(matrix):
    array = matrix.values
    count = 0
    for line in array:
        for cell in line:
            count = count + cell
    return count/array.size

def similarity_tokens(token1, token2, dictionary):
    set1 = set(dictionary[token1])
    set2 = set(dictionary[token2])
    set1.add(token1)
    set2.add(token2)
    if bool(set1 & set2):
        return 1
    else:
        return 0