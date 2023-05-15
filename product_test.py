import unittest
from product import Product

'''
    defines test cases for product class behavior
    unnitest.TestCase = test class that helps in creating test classes
    '''

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.new_product = Product("Mango",200)
        
        """"
        set up method that runs before each testcase
        """

    def test_init (self):
        '''
        initiates the test cases
        '''
        self.assertEqual(self.new_product.product_name,"Mango")
        self.assertEqual(self.new_product.product_price,200)    

    def test_save_contact(self):
        '''
        objects saved in the contact list
        '''
        self.new_product.save_product()
        self.assertEqual(len(Product.product_list),1)


    def tearDown(self):
        Product.product_list =[]



    def test_save_multiple_product(self):
        self.new_product.save_product()
        test_product = Product("orange",200)
        test_product.save_product()
        self.assertEqual(len(Product.product_list),2)

    def test_delete_product(self):
        self.new_product.save_product()

        test_product = Product("orange",200)
       
        test_product.save_product()
        self.new_product.delete_product() 
        self.assertEqual(len(Product.product_list),1
                         )

    def test_find_product_by_name(self):
        '''
        test to check if we can find a product by name and display information
        '''

        self.new_product.save_product()
        test_product = Product("orange",200) # new product
        test_product.save_product()

        found_product = Product.find_by_name("orange")

        self.assertEqual(found_product.product_price,test_product.product_price)

if __name__ ==  '__main__':
    unittest.main()    