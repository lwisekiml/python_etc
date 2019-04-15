# pickle.py
'''
with open('pickle_test.txt', 'r') as f:
    data = f.read()

print("data : ", data)

data1 = data.replace("\t", "    ").replace('>>> ', '')
print("data1 : ", data1)

with open('pickle.txt', 'w') as f:
    f.write(data1)
'''


import sys

src = sys.argv[1]
dst = sys.argv[2]

# try: 
with open(src) as f:
    data = f.read()
# except UnicodeDecodeError: # sublimetext3 은 utf8로 인코딩 되어있다.
    # print()
    # with open(src, 'r', encoding = 'utf8') as f:
    #     data = f.read()

try:
    rm_enter = sys.argv[3] # 한줄 공백 없앨경우 아무거나 입력
    data1 = data.replace("\t", "    ").replace('         \n', '').replace('\n\n', '\n')
except IndexError:
    data1 = data.replace("\t", "    ").replace('>>> ', '').replace('         ', '')

with open(dst, 'w', encoding = 'utf8') as f:
    f.write(data1)

