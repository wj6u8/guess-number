import random
r = random.randint(1, 100)
times = 1

while times >= 1:
	guess = input('請猜一個數字1~100: ')
	guess = int(guess)
	times = times + 1
	if guess < r:
		print('比答案小')
	elif guess > r:
		print('比答案大')
	else:
		print('終於猜對了')
		break