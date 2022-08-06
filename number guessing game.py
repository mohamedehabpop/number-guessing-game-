import random


def guess(x):
	random_number = random.randint(1,x)
	guess = 0 
	while guess != random_number:
		guess = int(input(f"please enter a guess between 1 and {x}: "))
		if random_number > guess:
			print("try again that's too low  ")
		elif random_number < guess:
			print("try again that's too high  ")
	print(f"yay, congrats. numbrer {random_number} is the correct number")


def computer_guess(y):
	low = 1 
	high = y
	feedback = ''
	while feedback != 'c':
		if low != high:
			gues = random.randint(low, high)
		else:
			gues = low 
		feedback = input(f'is {gues} high?(H), low(L) or correct(C)').lower()
		if feedback == 'h':
			high =gues -1 
		elif feedback == 'l':
			low = gues +1
	print(f'yay, congrats. the computer guessed or number:{gues}')

choice = int(input("choose computer guess(1) or human guess(2)"))

if choice == 1:
	computer_guess(1000)
elif choice==2:
	guess(100)