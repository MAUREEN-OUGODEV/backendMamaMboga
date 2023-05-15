class Mama:
    def __init__(self,full_name,email,password,confirm_password):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
    mama_list=[]
    def save_mama(self):
        Mama.mama_list.append(self)