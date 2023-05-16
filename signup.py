class Signup:
    def __init__(self, name, email, phone_number, password):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def show_name(self):
        return f"{self.name}"   

    def get_email(self):
        return f"{self.email}"