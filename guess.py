import random
r = random.randint(1, 100)
times = 0

while times >= 0:
	guess = input('請猜一個數字1~100: ')
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