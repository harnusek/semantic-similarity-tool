# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from tool_synonyms import synonym_dictionary
from tool_synonyms import fill_matrix
from tool_synonyms import similarity_tokens
from tool_synonyms import get_similarity

class TestToolSynonyms(unittest.TestCase):
    def test_synonym_dictionary(self):
        tokens1 = ['N0TD3FIN3D', 'N0N3X1ST']
        dict1 = {'N0TD3FIN3D':[], 'N0N3X1ST':[]}
        self.assertEqual(dict1, synonym_dictionary(tokens1))

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

    def test_get_similarity(self):
        self.assertEqual(1, get_similarity("metóda", "metóda"))
        self.assertEqual(0.8, get_similarity("metóda metóda", "metóda metóda N0TD3FIN3D metóda metóda"))
        self.assertEqual(0, get_similarity("metóda", "N0TD3FIN3D"))
        self.assertEqual(0.0625, get_similarity("My v tom máme jasno. A čo vy?", "Boli ste už voliť?"))
        self.assertEqual(0.2, get_similarity("Compute similarity between two sentences.","Compute similarity between two sentences."))

if __name__ == '__main__':
    unittest.main()