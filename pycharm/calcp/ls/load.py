from ..contact.cont import Contact


def load_contact(contact_list):
    f = open("contact_db.txt", "r", encoding='utf-8')
    lines = f.readlines()
    num = len(lines)/4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip()
        phone_number = lines[4*i + 1].rstrip()
        e_mail = lines[4*i + 2].rstrip()
        address = lines[4*i + 3].rstrip()
        contact = Contact(name, phone_number, e_mail, address)
        contact_list.append(contact)
    f.close()
