class Product:
    
    def __init__(self,product_name,product_price):
        self.product_name = product_name
        self.product_price = product_price
    product_list=[]
# save product
    def save_product(self):
        Product.product_list.append(self)

        # delete product
    def delete_product(self):

        Product.product_list.remove(self)     

# find product by name
    @classmethod
    def find_by_name(cls,name):

        
        for product in cls.product_list:
            if product.product_name == name :
                return product   