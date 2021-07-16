import random
x = input('最小值: ')
y = input('最大值: ')
x = int(x)
y = int(y)
ans = random.randint(x, y)
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
		print('小一點')
	elif guess < ans:
		print('大一點')
	
	print('你猜了', count, '次')