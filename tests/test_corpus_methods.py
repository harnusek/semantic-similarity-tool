# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from corpus_methods import similarity_sentences
from corpus_methods import fill_matrix
from corpus_methods import similarity_tokens
from corpus_methods import generate_test_model
from corpus_methods import similarity_matrix

class TestCorpusMethods(unittest.TestCase):
    def test_fill_matrix(self):
        model = generate_test_model()
        matrix1 = pd.DataFrame(columns=["dom", "UND3FIN3D"], index=["dom"]).apply(pd.to_numeric, errors='coerce')
        matrix2 = pd.DataFrame(columns=["dom", "UND3FIN3D"], index=["dom"]).apply(pd.to_numeric, errors='coerce')
        matrix2["dom"]["dom"] = 1.0
        matrix2["UND3FIN3D"]["dom"] = 0.0
        self.assertTrue(pd.DataFrame.equals(matrix2, fill_matrix(matrix1, model)))

    def test_similarity_tokens(self):
        model = generate_test_model()
        self.assertEqual( 1.0 ,similarity_tokens("dom","dom", model))
        self.assertEqual( 0,similarity_tokens("UND3FIN3D","byt", model))

    def test_similarity_sentences(self):
        self.assertEqual(0.5, similarity_sentences('dom UND3FIN3D', 'dom', False, False, False))

    def test_similarity_matrix(self):
        matrix = pd.DataFrame([[0.3, 0.5],
                              [0.6 , 0.9],
                              [0.1, 0.7]])
        matrix0 = pd.DataFrame([[0.5,0.4,0.1],
                                [0.7,0.5,0.8],
                                [0.8,0.6,0.1]])
        matrix1 = pd.DataFrame([[1]])
        matrix2 = pd.DataFrame([[1,0]])
        matrix3 = pd.DataFrame([[1,0],
                                [1,0]])
        matrix4 = pd.DataFrame([[1,0,1],
                                [1,0,0]])
        self.assertAlmostEqual(0.4, similarity_matrix(matrix))
        self.assertAlmostEqual(0.6666666666666666, similarity_matrix(matrix0))
        self.assertEqual(1, similarity_matrix(matrix1))
        self.assertEqual(0.5, similarity_matrix(matrix2))
        self.assertEqual(0.5, similarity_matrix(matrix3))
        self.assertAlmostEqual(0.3333333333333333, similarity_matrix(matrix4))

if __name__ == '__main__':
    unittest.main()