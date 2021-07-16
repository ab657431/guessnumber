import random
ans = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	guess = input('你猜的數字: ')
	guess = int(guess)
	if guess == ans:
		print('猜對了')
		print('你在第',count,'次猜中了')
		break
	elif guess > ans:
		print('比答案大')
	elif guess < ans:
		print('比答案小')
	
	print('你猜了', count, '次')