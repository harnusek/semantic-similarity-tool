# -*- coding: utf-8 -*-

import unittest
import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from common import preprocessing
from common import sentence_analysis

from common import avg_list
# from common import lemmatization
from common import generate_matrices
# from common import remove_stop_words

class TestCommon(unittest.TestCase):
# pre
    def test_preprocessing(self):
        return
        sent_1 = "Koľko je hodín?"
        sent_2 = "Aký je čas?"
        del_stop = False
        use_pos = False
        use_lem = False
        print(preprocessing(sent_1,sent_2, del_stop, use_pos, use_lem))

    def test_sentence_analysis(self):
        sent = "anotátor, napr. tento!"
        analyzed_sent = [{'word': 'anotátor', 'tag': 'SSms1'},
                         {'word': ',', 'tag': 'Z'},
                         {'word': 'napr', 'tag': 'W'},
                         {'word': '.', 'tag': 'Z'},
                         {'word': 'tento', 'tag': 'PFms1'},
                         {'word': '!', 'tag': 'Z'}]
        self.assertEqual(analyzed_sent, sentence_analysis(sent))

    def test_remove_stop_words(self):
        os.chdir('..')
        self.assertEqual(['1', '2'], remove_stop_words(['1', '2','a']))

    def test_lemmatization(self):
        self.assertEqual([''], lemmatization(''))
        self.assertEqual(['mama', 'alebo', 'nemať'], lemmatization('mám, alebo nemám!'))
        self.assertEqual(['alfa', 'beta'], lemmatization('alfa beta?'))

# post
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

if __name__ == '__main__':
    unittest.main()