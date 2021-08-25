import unittest
import platform

class Tests(unittest.TestCase):
    def setup (self): 
        # setup is called * before * each test is run
        pass 
    
    def teardown (self): 
        # teardown is called * after * the each test 
        pass 

    def test_0(self):
        self.assertTrue(True)

    def test_1 (self): 
        # any method beginning with " test " is a test 
        results = "abcd"
        self.assertEqual(results , "abcde")     

    @unittest.skip('skipped test')
    def test_2(self):
        self.fail('should have failed!')

    @unittest.skipIf(platform.system() == 'Darwin', 'Mac specific test')
    def test_3(self):
        self.assertTrue(True)

    @unittest.skipUnless(platform.system() == 'Darwin', 'Mac specific test')
    def test_4(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_5(self):
        self.assertEqual(2+2, 5)

if __name__ == '__main__':
    unittest.main()
