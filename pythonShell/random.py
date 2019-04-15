'''
import random
def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

def random_pop(data):
    number = random.choice(data)
    print("number : ", number)
    data.remove(number)
    return number

if __name__ == "__main__":
	data = [1,2,3,4,5]
	while data:
		print(random_pop(data))
'''

import random
def random_pop(data):
    pirnt(data)
	number = random.randint(0, len(data) - 1)
	return data.pop(number)

if __name__ == "__main__":
	data = [1,2,3,4,5]
	while data:
		print(random_pop(data))
