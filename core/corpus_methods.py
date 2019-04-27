#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Corpus semantic similarity methods
"""
import common
from gensim.models.keyedvectors import KeyedVectors
import os
from gensim.models import Word2Vec

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
    similarity = common.similarity_matrices(matrices)
    return similarity

def load_model():
    """
    :return: w2v model
    """
    fname = 'core/sources/w2v_model.bin'
    # fname = 'core/sources/[SK]prim-6.1-public-all.shuffled.080cbow.bin'
    # fname = 'core/sources/[SK]prim-6.1-public-all.shuffled.200cbow.bin'
    # fname = 'core/sources/[SK]prim-6.1-public-all.shuffled.300cbow.bin'
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

# def vector_averaging_matrix(matrix):
#     """
#     :param matrix:
#     :r: similarity based on averaging w2v vectors
#     """
#     if matrix is None:
#         return None
#     sent_1 = [word for word in matrix.columns.values if word in model.vocab]
#     sent_2 = [word for word in matrix.index.values if word in model.vocab]
#     if not sent_1 or not sent_2:
#         return 0.0
#     vect_1 =  np.mean(model[sent_1], axis=0)
#     vect_2 =  np.mean(model[sent_2], axis=0)
#     cosine_similarity = np.dot(vect_1, vect_2) / (
#             np.linalg.norm(vect_1) * np.linalg.norm(vect_2))
#     return float(cosine_similarity.item())

def generate_test_model():
    """
    :return: model for testing
    """
    texts = [['dom', 'byt']]
    model = Word2Vec(texts, size=2, window=1, min_count=1, workers=4)
    return model

if(os.getcwd().split(os.sep)[-1] == 'core'):
    model = load_model()
else:
    model = generate_test_model()
    # fname = '../core/sources/w2v_model.bin'
    # model = KeyedVectors.load_word2vec_format(fname, binary=True)