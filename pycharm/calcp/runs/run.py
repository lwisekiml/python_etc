from ..printt.print_mn import *
from ..set.set_cont import *
from ..md.mod import *
from ..md.dels import *
from ..ls.load import *
from ..ls.store import *


def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name : ")
            delete_contact(contact_list, name)
        elif menu == 4:
            name = input("Name : ")
            mod_contact(contact_list, name)
        elif menu == 5:
            store_contact(contact_list)
            break
