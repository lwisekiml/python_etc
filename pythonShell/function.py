'''
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박씨", 27)
say_myself("박씨", 27, False)
'''
'''
a = 2
def vartest(t):
    
    print(a)

vartest()

x = 10
def printx():
    print(x)
printx()
'''

'''
def ot(a):
    if a%2 == 0:
        print("짝")
    else:
        print("홀")
ot(3)
'''
oott = lambda a: print("짝") if a%2 == 0 else print("홀")
oott(3)


