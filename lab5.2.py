import unittest
import lab5 as tested_app



class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.status, '200 OK')
        self.assertEqual(r.data, b'Hello world!')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)