# -*- coding: utf-8 -*-

import common
from gensim.models.keyedvectors import KeyedVectors
import os
from gensim.models import Word2Vec
import numpy as np

def similarity_sentences(sent_1,sent_2, use_stop, use_pos, use_lem):
    """
    Return similarity between two sentences
    """
    matrices = common.preprocessing(sent_1,sent_2, use_stop, use_pos, use_lem)
    matrices = [fill_matrix(matrix, model) for matrix in matrices]
    sim_list = [similarity_matrix_X(matrix) for matrix in matrices]
    return common.avg_list(sim_list)

def load_model():
    fname = 'core/data/[SK]prim-6.1-public-all.shuffled.080cbow.bin'
    # fname = 'core/data/[SK]prim-6.1-public-all.shuffled.200cbow.bin'
    # fname = 'core/data/[SK]prim-6.1-public-all.shuffled.300cbow.bin'
    model = KeyedVectors.load_word2vec_format(fname, binary=True)
    return model

def fill_matrix(matrix, model):
    if matrix is not None:
        for col in matrix.columns.values:
            for ind in matrix.index.values:
                matrix.loc[ind, col] = similarity_tokens(ind, col, model)
    return matrix

def similarity_tokens(token1, token2, model):
    if(token1 is token2):
        return 1
    try:
        sim = model.wv.similarity(token1, token2)
    except KeyError:
        sim = 0
    return sim

def similarity_matrix_avg(matrix):
    if matrix is None:
        return None
    array = matrix.values
    count = 0
    for line in array:
        for cell in line:
            count = count + cell
    return count/array.size

def similarity_matrix_X(matrix):
    if matrix is None:
        return 0
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

def generate_model():
    texts = [['dom', 'byt']]
    model = Word2Vec(texts, size=2, window=1, min_count=1, workers=4)
    return model

if(os.getcwd().split(os.sep)[-1] != 'tests'):
    model = load_model()
else:
    # model = generate_model()
    fname = '../core/data/[SK]prim-6.1-public-all.shuffled.080cbow.bin'
    model = KeyedVectors.load_word2vec_format(fname, binary=True)