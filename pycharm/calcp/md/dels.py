def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if name == contact.name:
            del contact_list[i]
