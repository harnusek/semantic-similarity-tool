#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from common import preprocessing
from common import sentence_analysis
from common import categorize_sentences
from common import generate_matrices
from common import similarity_matrix
from common import similarity_matrices

class TestCommon(unittest.TestCase):
# pre
    def test_preprocessing(self):
        sent_1 = "Koľko dní?"
        sent_2 = "Aký je?"
        use_stop = False
        use_pos = True
        use_lem = True
        matrices = [None,
                    pd.DataFrame(columns=['koľko'], index= ['aký']).apply(pd.to_numeric, errors='coerce'),
                    None,
                    None,
                    pd.DataFrame(columns=['?'], index=['?']).apply(pd.to_numeric, errors='coerce')]
        for e, a in zip(matrices, preprocessing(sent_1,sent_2, use_stop, use_pos, use_lem)):
            if(e is not None and a is not None):
                self.assertTrue(pd.DataFrame.equals(e, a))

    def test_sentence_analysis(self):
        sent = "anotátor, napr. tento?"
        analyzed_sent1 = [{'word': 'anotátor', 'tag': 'S'},
                         {'word': ',', 'tag': 'Z'},
                         {'word': 'napr', 'tag': 'W'},
                         {'word': '.', 'tag': 'Z'},
                         {'word': 'tento', 'tag': 'P'},
                         {'word': '?', 'tag': 'Z'}]
        self.assertEqual(analyzed_sent1, sentence_analysis(sent, use_stop=True, use_lem=False))
        # test if stop-words stuff work
        analyzed_sent2 = [{'word': 'sa', 'tag': 'R'}]
        self.assertEqual(analyzed_sent2, sentence_analysis('a aby sa', use_stop=False, use_lem=False))

    def test_categorize_sentences(self):
        analyzed_sent1 = [{'word': '0', 'tag': 'A'},
                          {'word': '1', 'tag': 'B'},
                          {'word': '2', 'tag': 'B'}]
        analyzed_sent2 = [{'word': '3', 'tag': 'A'},
                          {'word': '4', 'tag': 'B'},
                          {'word': '5', 'tag': 'X'}]
        categories = ['A', 'B', 'C']
        categorized = [[['0'], ['3']], [['1', '2'], ['4']], [[], []]]
        self.assertEqual(categorized, categorize_sentences(analyzed_sent1, analyzed_sent2, categories))

    def test_generate_matrices(self):
        tokens1 = ["ako","si","starý"]
        tokens2 = ["koľko","máš","rokov"]
        categorized = [[tokens1, tokens2]]
        matrices = [pd.DataFrame(columns=tokens1, index= tokens2).apply(pd.to_numeric, errors='coerce')]
        for e, a in zip(matrices, generate_matrices(categorized)):
            self.assertTrue(pd.DataFrame.equals(e, a))
# post
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

    def test_similarity_matrices(self):
        self.skipTest('todo')

if __name__ == '__main__':
    unittest.main()