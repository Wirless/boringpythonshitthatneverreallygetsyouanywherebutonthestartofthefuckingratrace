import random
import time
credits = 100
bet = 0
even = [2,4,6,8,10,12]


class rouledice():
	while True:
		print("Welcome to rouledice please enter a number from 1 to 9: ")
		print(f"{credits} credits")
		uinput = int(input(": "))
		if uinput < 10:
			number = uinput
			bet = int(input("How much would you like to bet: "))
			if bet < credits:
				dice6 = random.randrange(1, 7)
				print(f"Dice rolled: {dice6} your number was {uinput}")
				if dice6 == uinput:
					credits += bet*4
					print(f"You won {credits} credits!")
				elif uinput == 9 and dice6 in even:
					print("You bet on 9 but it rolled on even you get your money back!")
				else:
					credits -= bet
					print(f"You lost {bet} credits! remaining credits: {credits}")
			else:
				bet = credits
				ds = f"Your bet was too high matching the amount of {credits} credits you own"
				print(ds)
		else:
			print("Dice has only 9 sides!")
		#
		#x = f"And finally what is your bet? your total credits are {credits}"
		#print(x)
		#betinput = input(": ")
		