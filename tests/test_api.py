import unittest
import os
import requests

class TestApi(unittest.TestCase):
    def test_connectiom(self):
        url = 'http://localhost:5000/'
        # response = requests.post(url=url, data=sent.encode('utf-8'))

        page = requests.get(url)
        print(page.content)
        return
        print(os.getcwd())
        os.chdir("..")
        os.system("python -c \"print('666')\"")
        os.system("ls")
        return
        print(os.getcwd())
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
