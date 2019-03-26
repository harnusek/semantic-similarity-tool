# coding=utf-8
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from tool_synonyms import synonym_list

class TestStringMethods(unittest.TestCase):
    def test_synonym_list(self):
        self.assertEqual(synonym_list('N0TD3FIN3D'), [])
        self.assertEqual(synonym_list('metóda'), ['metóda', 'postup', 'spôsob', 'cesta'])

if __name__ == '__main__':
    unittest.main()