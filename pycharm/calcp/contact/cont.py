class Contact:
    def __init__(self, name, phone_number, e_mail, address):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.address = address

    def print_info(self):
        print("\nName : ", self.name)
        print("Phone number : ", self.phone_number)
        print("E-mail : ", self.e_mail)
        print("Address : ", self.address)
