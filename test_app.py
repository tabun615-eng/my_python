import unittest
import requests

class TestApp(unittest.TestCase):
    def test_requests_import(self):
        self.assertIsNotNone(requests)

if __name__ == '__main__':
    unittest.main()
