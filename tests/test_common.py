# -*- coding: utf-8 -*-

import unittest
import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from common import avg_list
from common import tokenize
from common import generate_matrices
from common import similarity_avg

class TestCommon(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual([''], tokenize(''))
        self.assertEqual(['alfa', 'beta'], tokenize('alfa beta?'))

    def test_avg_list(self):
        self.assertEqual(0, avg_list([0]))
        self.assertEqual(9, avg_list([9]))
        self.assertEqual(2, avg_list([0, 1, 2, 3, 4]))

    def test_generate_matrices(self):
        tokens1 = ["ako","si","starý"]
        tokens2 = ["koľko","máš","rokov"]
        matrices = [pd.DataFrame(columns=tokens1, index= tokens2).apply(pd.to_numeric, errors='coerce')]
        for e, a in zip(matrices, generate_matrices(tokens1, tokens2)):
            self.assertTrue(pd.DataFrame.equals(e, a))

    def test_similarity_avg(self):
        matrix1 = pd.DataFrame([[1]])
        matrix2 = pd.DataFrame([[1,0]])
        matrix3 = pd.DataFrame([[1,0],[1,0]])
        matrix4 = pd.DataFrame([[1,0,1],[1,0,0]])
        self.assertEqual(1, similarity_avg(matrix1))
        self.assertEqual(0.5, similarity_avg(matrix2))
        self.assertEqual(0.5, similarity_avg(matrix3))
        self.assertEqual(0.5, similarity_avg(matrix4))

if __name__ == '__main__':
    unittest.main()