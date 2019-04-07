import unittest
import requests
import json
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
import rivals

class TestApi(unittest.TestCase):
    """
    Requires running server
    """
    def test_knowledgeSim(self):
        url = 'http://localhost:5000/api/knowledgeSim'
        data = {
            "sent_1": "dom strom",
            "sent_2": "stromec budova"
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        sim = float(response.content)
        self.assertEqual(1, sim)

    def test_corpusSim(self):
        url = 'http://localhost:5000/api/corpusSim'
        data = {
            "sent_1": "dom strom",
            "sent_2": "stromec budova"
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        sim = float(response.content)
        self.assertAlmostEqual(0.2179, sim)

    def test_rivals(self):
        print(type(rivals.rival_similarity('koľko je'.split(),'koľko je hodín'.split())))

if __name__ == '__main__':
    unittest.main()
