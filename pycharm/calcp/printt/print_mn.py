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
