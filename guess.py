# Generate a random number between 1~100
# Ask user to input a number
# If that is correct, print "Correct!"
# If that is wrong, tell user the number is greater or smaller

import random

r = random.randint(1, 100)
while True:
	num = input('Please enter a number: ')
	num = int(num)
	if num == r:
		print('Correct!')
		break
	elif num > r:
		print('Number should be smaller')
	else:
		print('Number should be greater')