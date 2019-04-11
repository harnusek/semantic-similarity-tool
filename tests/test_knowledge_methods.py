#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from knowledge_methods import update_dictionary
from knowledge_methods import fill_matrix
from knowledge_methods import similarity_tokens
from knowledge_methods import similarity_sentences

class TestKnowledgeMethods(unittest.TestCase):
    def test_update_dictionary(self):
        token1 = 'N0TD3FIN3D'
        dict1 = {'N0TD3FIN3D':[]}
        self.assertEqual(dict1, update_dictionary(dict(),token1))
        token2 = 'metóda'
        dict2 = {'metóda':['metóda', 'postup', 'spôsob', 'cesta']}
        self.assertEqual(dict2, update_dictionary(dict(), token2))

    def test_fill_matrix(self):
        matrix1 = pd.DataFrame(columns=["dom", "je"], index=["byt"]).apply(pd.to_numeric, errors='coerce')
        matrix2 = pd.DataFrame(columns=["dom", "je"], index=["byt"]).apply(pd.to_numeric, errors='coerce')
        matrix2["dom"]["byt"] = 1.0
        matrix2["je"]["byt"] = 0.0
        dictionary = {"dom":["byt"] , "je":[] , "byt":[] }
        self.assertTrue(pd.DataFrame.equals(matrix2, fill_matrix(matrix1, dictionary)))

    def test_similarity_tokens(self):
        dictionary = {'metóda': ['metóda', 'postup', 'spôsob', 'cesta'], 'N0TD3FIN3D': [] , 'postup': [] , 'N0N3X1ST': []}
        self.assertEqual(1, similarity_tokens('metóda', 'postup', dictionary))
        self.assertEqual(1, similarity_tokens('metóda', 'metóda', dictionary))
        self.assertEqual(0, similarity_tokens('N0TD3FIN3D', 'metóda', dictionary))
        self.assertEqual(0, similarity_tokens('N0TD3FIN3D', 'N0N3X1ST', dictionary))

    def test_similarity_sentences(self):
        self.assertEqual(1, similarity_sentences("metóda", "metóda",False,False,False))
        self.assertEqual(0.4, similarity_sentences("metóda metóda", "metóda metóda N0TD3FIN3D metóda metóda",False,False,False))
        self.assertEqual(0, similarity_sentences("metóda", "N0TD3FIN3D",False,False,False))
        self.assertEqual(0.1, similarity_sentences("My v tom máme jasno. A čo vy?", "Boli ste už voliť?",False,False,False))
        self.assertEqual(1.0, similarity_sentences("Compute similarity between two sentences.","Compute similarity between two sentences.",False,False,False))

if __name__ == '__main__':
    unittest.main()