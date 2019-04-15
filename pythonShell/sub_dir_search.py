# sub_dir_search.py

import os
import sys

def search(dirname):
    try:
        filenames = os.listdir(dirname) # 해당 디렉토리에 있는 파일 리스트
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1] # 파일명을 확장자 기준으로 나눔
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass    

search("D:/python/pythonShell")

'''
# 파이썬 shell
rout = input("디렉토리 경로 : ")
search(rout)
'''
# cmd (해당 위치에서 이 코드 실행 ex> pyrthon sub_dir_search.py)
target = os.getcwd()
print(target)
search(target)
