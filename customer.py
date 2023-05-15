class Customer:
    def __init__(self,full_name,email,password,confirm_password):
        self.full_name=full_name
        self.email= email
        self.password = password
        self.confirm_password =  confirm_password
    customer_list=[]
    def save_customer(self):
        Customer.customer_list.append(self)