'''
class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal3.sub(5))
print(cal3.sub(3))
'''


class FourCal:
    def __init__(self, first, second):
        self.num1 = first
        self.num2 = second
        
    def setdata(self, first, second):
        self.num1 = first
        self.num2 = second

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2

a = FourCal(1,2)
#a.setdata(4, 2)
print(a.num1)
print("a.add() :", a.add())
print("a.mul() :", a.mul())
print("a.sub() :", a.sub())
print("a.sub() :", a.div())

b = FourCal(2,5)
#b.setdata(3, 7)
print("b.num1 : ", b.num1)

print("="*15)

class MoreFourCal(FourCal):
    def pow(self):
        result = self.num1 ** self.num2
        return result

    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2

a = MoreFourCal(6, 8)
print("a.add() :", a.add())
b = MoreFourCal(4, 2)
print("b.pow() :", b.pow())


a = MoreFourCal(4, 0)
print("a.div() :", a.div())


print("\n=====클래스 변수=====")
class Family:
    lastname = "김"
        
print("Family.lastname : ", Family.lastname)

a = Family()
b = Family()

print("\n=== a.lastname 변경 전 ===")
print("id(Family.lastname) : ", id(Family.lastname))
print("id(a.lastname) : ", id(a.lastname))
print("id(b.lastname) : ", id(b.lastname))
print(a.lastname)
print(b.lastname)

print("\n=== a.lastname 변경 후 ===")
a.lastname = "한"
print(a.lastname)
print(b.lastname)

print('\n === Family.lastname = "박" ===')
Family.lastname = "박"
print("a.lastname : ", a.lastname)
print("b.lastname : ", b.lastname)

print("id(Family.lastname) : ", id(Family.lastname))
print("id(a.lastname) : ", id(a.lastname))
print("id(b.lastname) : ", id(b.lastname))



print("=" * 30)
class Data:
	def __init__(self, data):
		tmp = data.split("|")
		self.name = tmp[0]
		self.age = tmp[1]
		self.grade = tmp[2]
	def print_age(self):
		print(self.age)
	def print_grade(self):
		print("%s님 당신의 점수는 %s입니다." % (self.name, self.grade))

data = Data("홍길동|42|A")
data.print_age()
data.print_grade()
