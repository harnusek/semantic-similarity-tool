import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from tool_synonyms import synonym_list

class TestToolSynonyms(unittest.TestCase):
    def test_get_similarity(self):
        # get_similarity(sent1, sent2)
        pass

    def test_synonym_list(self):
        self.assertEqual(synonym_list('N0TD3FIN3D'), [])
        self.assertEqual(synonym_list('metóda'), ['metóda', 'postup', 'spôsob', 'cesta'])

    def test_sim_by_matrix(self):
        # sim_by_matrix(xList, yList)
        pass

    def test_sim_by_tokens(self):
        # sim_by_tokens(x, y)
        pass

if __name__ == '__main__':
    unittest.main()