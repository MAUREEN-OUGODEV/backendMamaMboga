import unittest
from mama import Mama
'''
    defines test cases for product class behavior
    unnitest.TestCase = test class that helps in creating test classes
    '''
class TestMama(unittest.TestCase):
    def setUp(self):
        self.new_mama = Mama("Maureen Akinyi","ougomaureenakinyi@gmail.com","1234567","1234567")
        """"
        set up method that runs before each testcase
        """
    def test_init (self):
        '''
        initiates the test cases
        '''
        self.assertEqual(self.new_mama.full_name,"Maureen Akinyi")
        self.assertEqual(self.new_mama.email,"ougomaureenakinyi@gmail.com")
        self.assertEqual(self.new_mama.password,"1234567")
        self.assertEqual(self.new_mama.confirm_password,"1234567")
    def test_save_mama(self):
        '''
        objects saved in the contact list
        '''
        self.new_mama.save_mama()
        self.assertEqual(len(Mama.mama_list),1)
    def tearDown(self):
        Mama.mama_list =[]
    def test_save_multiple_product(self):
        self.new_mama.save_mama()
        test_mama = Mama("jackie ougo","jackie@gmail.com","123456","1223456")
        test_mama.save_mama()
        self.assertEqual(len(Mama.mama_list),2)
if __name__ ==  '__main__':
    unittest.main()