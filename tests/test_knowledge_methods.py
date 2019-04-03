# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from knowledge_methods import update_dictionary
from knowledge_methods import fill_matrix
from knowledge_methods import similarity_tokens
from knowledge_methods import similarity_sentences
from knowledge_methods import similarity_matrix_avg
from knowledge_methods import similarity_matrix_X

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
        self.assertAlmostEqual(1, similarity_sentences("metóda", "metóda"))
        self.assertAlmostEqual(0.8, similarity_sentences("metóda metóda", "metóda metóda N0TD3FIN3D metóda metóda"))
        self.assertAlmostEqual(0, similarity_sentences("metóda", "N0TD3FIN3D"))
        self.assertAlmostEqual(0.06, similarity_sentences("My v tom máme jasno. A čo vy?", "Boli ste už voliť?"))
        self.assertAlmostEqual(0.16666666666666666, similarity_sentences("Compute similarity between two sentences.","Compute similarity between two sentences."))


    def test_similarity_matrix_avg(self):
        matrix1 = pd.DataFrame([[1]])
        matrix2 = pd.DataFrame([[1,0]])
        matrix3 = pd.DataFrame([[1,0],[1,0]])
        matrix4 = pd.DataFrame([[1,0,1],[1,0,0]])
        self.assertEqual(1, similarity_matrix_avg(matrix1))
        self.assertEqual(0.5, similarity_matrix_avg(matrix2))
        self.assertEqual(0.5, similarity_matrix_avg(matrix3))
        self.assertEqual(0.5, similarity_matrix_avg(matrix4))

    def test_similarity_matrix_X(self):
        matrix0 = pd.DataFrame([[0.5,0.4,0.1],[0.7,0.5,0.8],[0.8,0.6,0.1]])
        matrix1 = pd.DataFrame([[1]])
        matrix2 = pd.DataFrame([[1,0]])
        matrix3 = pd.DataFrame([[1,0],[1,0]])
        matrix4 = pd.DataFrame([[1,0,1],[1,0,0]])
        self.assertAlmostEqual(0.7, similarity_matrix_X(matrix0))
        self.assertEqual(1, similarity_matrix_X(matrix1))
        self.assertEqual(1, similarity_matrix_X(matrix2))
        self.assertEqual(1, similarity_matrix_X(matrix3))
        self.assertEqual(1, similarity_matrix_X(matrix4))

if __name__ == '__main__':
    unittest.main()