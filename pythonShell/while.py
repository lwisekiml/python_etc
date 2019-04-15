'''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")
'''

'''
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈으 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어 졌습니다. 판매 중지")
        break
'''

num = 1
sum = 0
while num <= 1000:
    if num%3 == 0:
        sum = sum + num
    num = num + 1
        
print(sum)

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
while A:
    num = A.pop()
    if num >= 50:
        sum += num
print(sum)


num = int(input("별 : "))
i = 1
while i <= num:
    print("*"*i)
    i += 1




