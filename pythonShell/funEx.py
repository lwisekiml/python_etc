'''
import sys
# print(sys.argv)
l = sys.argv

sum = 0
for i in l:
    try:
        sum += int(i)
    except ValueError:
        continue
    
print(sum)
'''

'''
import os
os.chdir("D:\python\pythonShell")
f = os.popen("dir")
print(f.read())
'''

'''
import glob
print(glob.glob("D:/python/pythonShell/*.py"))
'''
# 2018/04/03 17:20:32
'''
import time
print(time.strftime('%Y/%m/%d %X', time.localtime(time.time())))
'''

# 다시보기!!!

import random
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = []
    for i in range(1, 47):
        data.append(i)
    for i in range(6):
        print(random_pop(data))
