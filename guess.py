import random
a = input('請輸入初始數字: ')
a = int(a)
b = input('請輸入最後數字: ')
b = int(b)
r = random.randint(a, b)
times = 0

while times >= 0:
	guess = input('請猜一個數字: ')
	guess = int(guess)
	times = times + 1
	print('你猜了', times, '次')
	if guess < r:
		print('比答案小')
	elif guess > r:
		print('比答案大')
	else:
		print('BINGO猜對了')
		break