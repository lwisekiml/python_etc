class Contact:
    def __init__(self, name):
        self.name = name

def set_contact(contact_list):
    name = "choi"
    contact = Contact(name)
    contact_list.append(contact)

    name = "park"
    contact = Contact(name)
    contact_list.append(contact)

def run():
    contact_list = []
    set_contact(contact_list)

    for c_name in contact_list:
        print(c_name.name)

if __name__ == "__main__":
    run()
