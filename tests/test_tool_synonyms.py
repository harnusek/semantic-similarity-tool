# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from tool_synonyms import synonym_dict
from tool_synonyms import generate_matrices
from tool_synonyms import fill_matrix

class TestToolSynonyms(unittest.TestCase):
    def test_synonym_dict(self):
        tokens1 = ['N0TD3FIN3D', 'N0N3X1ST']
        dict1 = {'N0TD3FIN3D':[], 'N0N3X1ST':[]}
        self.assertEqual(dict1, synonym_dict(tokens1))

        tokens2 = ['metóda']
        dict2 = {'metóda':['metóda', 'postup', 'spôsob', 'cesta']}
        self.assertEqual(dict2, synonym_dict(tokens2))

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
        dictionary = {"dom":["byt"]}
        self.assertTrue(pd.DataFrame.equals(matrix2, fill_matrix(matrix1, dictionary)))

    def test_sim_by_tokens(self):
        # sim_by_tokens(x, y)
        pass

if __name__ == '__main__':
    unittest.main()