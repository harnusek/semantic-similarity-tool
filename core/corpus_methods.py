# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Corpus semantic similarity methods
"""
import common
from gensim.models.keyedvectors import KeyedVectors
import os
from gensim.models import Word2Vec
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
    matrices = [fill_matrix(matrix, model) for matrix in matrices]
    sim_list = [similarity_matrix(matrix) for matrix in matrices]
    return common.avg_list(sim_list)

def load_model():
    """
    :return: w2v model
    """
    fname = 'core/data/[SK]prim-6.1-public-all.shuffled.080cbow.bin'
    # fname = 'core/data/[SK]prim-6.1-public-all.shuffled.200cbow.bin'
    # fname = 'core/data/[SK]prim-6.1-public-all.shuffled.300cbow.bin'
    model = KeyedVectors.load_word2vec_format(fname, binary=True)
    return model

def fill_matrix(matrix, model):
    """
    :param matrix:
    :param model:
    :return: matrix filled with token similarities
    """
    if matrix is not None:
        for col in matrix.columns.values:
            for ind in matrix.index.values:
                matrix.loc[ind, col] = similarity_tokens(ind, col, model)
    return matrix

def similarity_tokens(token1, token2, model):
    """
    :param token1:
    :param token2:
    :param model:
    :return: similarity between token1 and token2
    """
    if(token1 == token2):
        return 1
    try:
        sim = model.wv.similarity(token1, token2)
    except KeyError:
        sim = 0
    return sim

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

def generate_test_model():
    """
    :return: model for testing
    """
    texts = [['dom', 'byt']]
    model = Word2Vec(texts, size=2, window=1, min_count=1, workers=4)
    return model

if(os.getcwd().split(os.sep)[-1] != 'tests'):
    model = load_model()
else:
    model = generate_test_model()
    # fname = '../core/data/[SK]prim-6.1-public-all.shuffled.080cbow.bin'
    # model = KeyedVectors.load_word2vec_format(fname, binary=True)