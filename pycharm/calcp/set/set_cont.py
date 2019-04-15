from ..contact.cont import Contact


def set_contact():
    name = input("Name : ")
    phone_number = input("Phone number : ")
    e_mail = input("E-mail : ")
    address = input("Address : ")
    contact = Contact(name, phone_number, e_mail, address)
    return contact
