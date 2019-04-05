# -*- coding: utf-8 -*-

import unittest
import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from common import preprocessing
from common import sentence_analysis
from common import categorize_sentences
from common import generate_matrices
from common import avg_list

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
        categories = ['default', 'A', 'B', 'C']
        categorized = [[[], ['5']], [['0'], ['3']], [['1', '2'], ['4']], [[], []]]
        self.assertEqual(categorized, categorize_sentences(analyzed_sent1, analyzed_sent2, categories))

    def test_generate_matrices(self):
        tokens1 = ["ako","si","starý"]
        tokens2 = ["koľko","máš","rokov"]
        categorized = [[tokens1, tokens2]]
        matrices = [pd.DataFrame(columns=tokens1, index= tokens2).apply(pd.to_numeric, errors='coerce')]
        for e, a in zip(matrices, generate_matrices(categorized)):
            self.assertTrue(pd.DataFrame.equals(e, a))
# post
    def test_avg_list(self):
        self.skipTest('in progress')
        self.assertEqual(0, avg_list([0]))
        self.assertEqual(9, avg_list([9]))
        self.assertEqual(1.3333, avg_list([3,0,1]))
        self.assertEqual(2, avg_list([0, 1, 2, 3, 4]))
if __name__ == '__main__':
    unittest.main()