# -*- coding: utf-8 -*-

import common
from gensim.models.keyedvectors import KeyedVectors
# import nltk
# import gensim
# from gensim import corpora, models, similarities

def similarity_sentences(sent1,sent2):
    """
    Return similarity between two sentences
    """
    tokens1 = common.tokenize(sent1)
    tokens2 = common.tokenize(sent2)
    model = load_model()
    matrices = common.generate_matrices(tokens1, tokens2)
    matrices = [fill_matrix(matrix) for matrix in matrices]
    sim_list = [common.similarity_avg(matrix) for matrix in matrices]
    return common.avg_list(sim_list)

def load_model():
    fname = '/data/[SK]prim-6.1-public-all.shuffled.080cbow.bin'
    # fname = '/data/[SK]prim-6.1-public-all.shuffled.300cbow.bin'
    model = KeyedVectors.load_word2vec_format(fname, binary=True)
    return model

def fill_matrix(matrix):
    for col in matrix.columns.values:
        for ind in matrix.index.values:
            matrix.loc[ind, col] = similarity_tokens(col, ind)
    return matrix

def similarity_tokens(token1, token2):
    return 4.2