def store_contact(contact_list):
    f = open("contact_db.txt", "w", encoding="utf-8")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.address + '\n')
    f.close()
