# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from corpus_methods import similarity_sentences
from corpus_methods import fill_matrix
from corpus_methods import similarity_tokens
from corpus_methods import load_model

class TestCorpusMethods(unittest.TestCase):
    def test_fill_matrix(self):
        matrix1 = pd.DataFrame(columns=["dom", "je"], index=["byt"]).apply(pd.to_numeric, errors='coerce')
        matrix2 = pd.DataFrame(columns=["dom", "je"], index=["byt"]).apply(pd.to_numeric, errors='coerce')
        matrix2["dom"]["byt"] = 1.0
        matrix2["je"]["byt"] = 0.0
        self.assertTrue(pd.DataFrame.equals(matrix2, fill_matrix(matrix1)))

    def test_similarity_tokens(self):
        self.assertEqual(1, similarity_tokens('metóda', 'postup'))
        self.assertEqual(1, similarity_tokens('metóda', 'metóda'))
        self.assertEqual(0, similarity_tokens('N0TD3FIN3D', 'metóda'))
        self.assertEqual(0, similarity_tokens('N0TD3FIN3D', 'N0N3X1ST'))

    def test_get_similarity(self):
        self.assertEqual(1, similarity_sentences('', ''))

    def test_load_model(self):
        model = load_model()
        print(model)

if __name__ == '__main__':
    unittest.main()