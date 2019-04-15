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
