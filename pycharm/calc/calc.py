# -*- coding: utf-8 -*-
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


def set_contact():
        name = input("Name : ")
        phone_number = input("Phone number : ")
        e_mail = input("E-mail : ")
        address = input("Address : ")
        contact = Contact(name, phone_number, e_mail, address)
        return contact


def print_menu():
    print("1.연락처 입력")
    print("2.연락처 출력")
    print("3.연락처 삭제")
    print("4.연락처 수정")
    print("5.종료")
    menu = input("메뉴선택:")
    return int(menu)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if name == contact.name:
            del contact_list[i]


def mod_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if name == contact.name:
            while 1:
                contact.print_info()
                num = int(input("수정 하고 싶은 항목의 번호\n(1.이름 2.폰 번호 3.이메일 4.주소 5.취소 : "))
                if num == 1:
                    contact.name = input('이름 : ')
                    break
                elif num == 2:
                    contact.phone_number = input('폰 번호 : ')
                    break
                elif num == 3:
                    contact.e_mail = input('이메일 : ')
                    break
                elif num == 4:
                    contact.address = input('주소 : ')
                    break
                elif num == 5:
                    break
                else:
                    print("잘못 입력 하셨습니다.")


def store_contact(contact_list):
    f = open("contact_db.txt", "w", encoding="utf-8")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.address + '\n')
    f.close()


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


if __name__ == "__main__":
    run()

