import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from preprocessing import tokenize

class TestPreprocessing(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual([''], tokenize(''))
        self.assertEqual(['alfa', 'beta', '?'], tokenize('alfa beta ?'))

if __name__ == '__main__':
    unittest.main()