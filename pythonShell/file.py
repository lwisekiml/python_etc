'''
f = open("D:/python/pythonShell/test.txt", "w")
for i in range(1,11):
	data = "%d번째 줄입니다.\n" % i
	f.write(data)
f.close()
'''
print("=====while=====")
f = open("D:/python/pythonShell/test.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
f.close()
print("="*16)

print("===readlins===")
f = open("D:/python/pythonShell/test.txt", "r")
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()
print("="*15)

print("====read====")
f = open("D:/python/pythonShell/test.txt", "r")
data = f.read()
print(data, end='')
f.close()
print("="*15)


print("=new text insert=")
f = open("D:/python/pythonShell/test.txt", "a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
print("="*15)
