# Generate a random number between 1~100
# Ask user to input a number
# If that is correct, print "Correct!"
# If that is wrong, tell user the number is greater or smaller

import random
start = input('Please input the range(Start): ')
end = input('Please input the range(End): ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('Please enter a number: ')
	num = int(num)
	if num == r:
		print('Correct!')
		print('You use total: ', count, 'guess')
		break
	elif num > r:
		print('Number should be smaller')
	else:
		print('Number should be greater')
	print('This is ', count, 'guess')