'''
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
'''

'''
with open("test.txt", 'w') as f:
    f.write("Life is too short")
'''

'''
ch = input("저장할 내용을 입력하세요 : ")
f = open("test.txt", 'a')
f.write(ch)
f.write("\n")
f.close()
'''
"""
f = open('abc.txt', 'r')
lines = f.readlines()  # 모든 라인을 읽음
f.close()

lines.reverse()  # 읽은 라인을 역순으로 정렬

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()  # 포함되어 있는 줄바꿈 문자 제거
    f.write(line)
    f.write('\n')  # 줄바꿈 문자 삽입
f.close()
"""


"""
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
"""

f = open('sample.txt', 'r')
data = f.read()
f.close()
data = data.split('\n')

sum = 0
for i in data:
    sum += int(i)

avg = sum/len(data)

f = open('result.txt', 'w')
f.write(str(sum))
f.write('\n')
f.write(str(avg))
f.close()
