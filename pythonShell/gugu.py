num = input("구구단을 출력할 숫자를 입력(1~9) : ")
num = int(num)
for i in range(1, 10):
    print(num * i, end=' ')
