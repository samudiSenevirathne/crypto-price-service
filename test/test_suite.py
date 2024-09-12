import unittest
import requests

class TestCryptoPriceApp(unittest.TestCase):
    def test_home(self):
        response = requests.get('http://<your-loadbalancer-ip>')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the Coinbase Exchange!', response.json()['message'])

if __name__ == '__main__':
    unittest.main()
