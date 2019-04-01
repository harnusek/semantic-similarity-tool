# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from knowledge_methods import synonym_dictionary
from knowledge_methods import fill_matrix
from knowledge_methods import similarity_tokens
from knowledge_methods import similarity_sentences
from knowledge_methods import load_dictionary
from knowledge_methods import save_dictionary
from knowledge_methods import delete_dictionary

class TestKnowledgeMethods(unittest.TestCase):
    def test_synonym_dictionary(self):
        delete_dictionary()
        tokens1 = ['N0TD3FIN3D', 'N0N3X1ST']
        dict1 = {'N0TD3FIN3D':[], 'N0N3X1ST':[]}
        self.assertEqual(dict1, synonym_dictionary(tokens1))
        delete_dictionary()
        tokens2 = ['metóda']
        dict2 = {'metóda':['metóda', 'postup', 'spôsob', 'cesta']}
        self.assertEqual(dict2, synonym_dictionary(tokens2))

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
        self.assertEqual(1, similarity_sentences("metóda", "metóda"))
        self.assertEqual(0.8, similarity_sentences("metóda metóda", "metóda metóda N0TD3FIN3D metóda metóda"))
        self.assertEqual(0, similarity_sentences("metóda", "N0TD3FIN3D"))
        self.assertEqual(0.0625, similarity_sentences("My v tom máme jasno. A čo vy?", "Boli ste už voliť?"))
        self.assertEqual(0.2, similarity_sentences("Compute similarity between two sentences.","Compute similarity between two sentences."))

    def test_load_dictionary(self):
        self.skipTest('Is not testable')
        os.chdir('..')
        # self.assertEqual(dict(), load_dictionary())
        print(load_dictionary())

    def test_save_dictionary(self):
        self.skipTest('Is not testable')
        os.chdir('..')
        save_dictionary()

if __name__ == '__main__':
    unittest.main()