# -*- coding: utf-8 -*-

import common
from gensim.models.keyedvectors import KeyedVectors
import os
from gensim.models import Word2Vec

def similarity_sentences(sent_1,sent_2, del_stop=False, use_pos=False, use_lem=False):
    """
    Return similarity between two sentences
    """
    # all = common.preprocessing(sent_1,sent_2, del_stop, use_pos, use_lem)
    tokens1 = common.lemmatization(sent_1)
    tokens2 = common.lemmatization(sent_2)
    matrices = common.generate_matrices(tokens1, tokens2)
    matrices = [fill_matrix(matrix, model) for matrix in matrices]
    sim_list = [similarity_matrix_avg(matrix) for matrix in matrices]
    return common.avg_list(sim_list)

def load_model():
    fname = 'core/data/[SK]prim-6.1-public-all.shuffled.080cbow.bin'
    # fname = 'core/data/[SK]prim-6.1-public-all.shuffled.300cbow.bin'
    model = KeyedVectors.load_word2vec_format(fname, binary=True)
    return model

def fill_matrix(matrix, model):
    for col in matrix.columns.values:
        for ind in matrix.index.values:
            matrix.loc[ind, col] = similarity_tokens(ind, col, model)
    return matrix

def similarity_tokens(token1, token2, model):
    try:
        sim = model.wv.similarity(token1, token2)
    except KeyError:
        sim = 0
    return sim

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

def generate_model():
    texts = [['dom', 'byt']]
    model = Word2Vec(texts, size=2, window=1, min_count=1, workers=4)
    return model

if(os.getcwd().split(os.sep)[-1] != 'tests'):
    model = load_model()
else:
    model = generate_model()