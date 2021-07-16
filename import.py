import random
ans = random.randint(1, 100)

while True:
	guess = input('你猜的數字: ')
	guess = int(guess)
	if guess == ans:
		print('猜對了')
		break
	elif guess > ans:
		print('比答案大')
	elif guess < ans:
		print('比答案小')
