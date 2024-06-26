#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from corpus_methods import similarity_sentences
from corpus_methods import fill_matrix
from corpus_methods import similarity_tokens
from corpus_methods import generate_test_model

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

if __name__ == '__main__':
    unittest.main()