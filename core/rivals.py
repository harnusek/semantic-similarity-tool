# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import sys

def rival_similarity(sent_1, sent_2):
    vect_1 = np.mean(model[[word for word in sent_1 if word in model.vocab]], axis=0)
    vect_2 = np.mean(model[[word for word in sent_2 if word in model.vocab]], axis=0)
    cosine_similarity = np.dot(vect_1, vect_2) / (
            np.linalg.norm(vect_1) * np.linalg.norm(vect_2))
    return cosine_similarity.item()

def rival_matrix(matrix):
    vect_1 =  np.mean(model[[word for word in matrix.columns.values if word in model.vocab]], axis=0)
    vect_2 =  np.mean(model[[word for word in matrix.index.values if word in model.vocab]], axis=0)
    cosine_similarity = np.dot(vect_1, vect_2) / (
            np.linalg.norm(vect_1) * np.linalg.norm(vect_2))
    return cosine_similarity.item()

if(os.getcwd().split(os.sep)[-1] != 'tests'):
    model = load_model()
else:
    fname = '../core/data/[SK]prim-6.1-public-all.shuffled.080cbow.bin'
    model = KeyedVectors.load_word2vec_format(fname, binary=True)

