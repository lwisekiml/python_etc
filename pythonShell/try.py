'''
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print('indexing 할 수 없습니다.')



try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


try:
    f = open("나없는파일", "r")
except FileNotFoundError:
    print("파일이 없습니다.")
    pass

print('\n== 오류 일부러 발생시키기 ===')
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
'''

class MyError(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다.'
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError  as e:
    print(e)
    

print('=== 연습문제 ===')
result = 0
try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
