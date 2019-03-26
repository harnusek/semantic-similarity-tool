import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
from tool_w2v import get_similarity

class TestToolW2V(unittest.TestCase):
    def test_get_similarity(self):
        self.assertEqual(1, get_similarity('',''))

if __name__ == '__main__':
    unittest.main()