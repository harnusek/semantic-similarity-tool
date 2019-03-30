# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from tool_synonyms import synonym_dictionary
from tool_synonyms import generate_matrices
from tool_synonyms import fill_matrix
from tool_synonyms import similarity_tokens
from tool_synonyms import similarity_matrix
from tool_synonyms import get_similarity

class TestToolSynonyms(unittest.TestCase):
    def test_synonym_dictionary(self):
        tokens1 = ['N0TD3FIN3D', 'N0N3X1ST']
        dict1 = {'N0TD3FIN3D':[], 'N0N3X1ST':[]}
        self.assertEqual(dict1, synonym_dictionary(tokens1))

        tokens2 = ['metóda']
        dict2 = {'metóda':['metóda', 'postup', 'spôsob', 'cesta']}
        self.assertEqual(dict2, synonym_dictionary(tokens2))

    def test_generate_matrices(self):
        tokens1 = ["ako","si","starý"]
        tokens2 = ["koľko","máš","rokov"]
        matrices = [pd.DataFrame(columns=tokens1, index= tokens2)]
        for e, a in zip(matrices, generate_matrices(tokens1, tokens2)):
            self.assertTrue(pd.DataFrame.equals(e, a))

    def test_fill_matrix(self):
        matrix1 = pd.DataFrame(columns=["dom", "je"], index=["byt"])
        matrix2 = pd.DataFrame(columns=["dom", "je"], index=["byt"])
        matrix2["dom"]["byt"] = 1
        matrix2["je"]["byt"] = 0
        dictionary = {"dom":["byt"] , "je":[] , "byt":[] }
        self.assertTrue(pd.DataFrame.equals(matrix2, fill_matrix(matrix1, dictionary)))

    def test_similarity_tokens(self):
        dictionary = {'metóda': ['metóda', 'postup', 'spôsob', 'cesta'], 'N0TD3FIN3D': [] , 'postup': [] , 'N0N3X1ST': []}
        self.assertEqual(1, similarity_tokens('metóda', 'postup', dictionary))
        self.assertEqual(1, similarity_tokens('metóda', 'metóda', dictionary))
        self.assertEqual(0, similarity_tokens('N0TD3FIN3D', 'metóda', dictionary))
        self.assertEqual(0, similarity_tokens('N0TD3FIN3D', 'N0N3X1ST', dictionary))

    def test_similarity_matrix(self):
        matrix1 = pd.DataFrame([[1]])
        matrix2 = pd.DataFrame([[1,0]])
        matrix3 = pd.DataFrame([[1,0],[1,0]])
        matrix4 = pd.DataFrame([[1,0,1],[1,0,0]])
        self.assertEqual(1, similarity_matrix(matrix1))
        self.assertEqual(0.5, similarity_matrix(matrix2))
        self.assertEqual(0.5, similarity_matrix(matrix3))
        self.assertEqual(0.5, similarity_matrix(matrix4))

    def test_get_similarity(self):
        self.assertEqual(1, get_similarity("metóda", "metóda"))
        # self.assertEqual(0, get_similarity("metóda metóda", "metóda metóda N0TD3FIN3D metóda metóda"))
        self.assertEqual(0, get_similarity("metóda", "N0TD3FIN3D"))

if __name__ == '__main__':
    unittest.main()