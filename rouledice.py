import random
import time
maincredits = 0
credits = 100
bet = 0
even = [2,4,6,8,10,12]
odd = [1,3,5,7,9,11]
high = [4,5,6]
low = [1,2,3]
blackjackfull = 21
class Games:
	while True:
		print("Which game would you like to play?")
		print("1. Chohan\n 2.HL \n 3. Numbers")
		uinput = input(": ")
		if uinput == "1" or uinput == "chohan":
			while True:
				print("Options:\n Type Odd to play odd\n Type Even to play even")
				time.sleep(0.5)
				print("Current Credits: " + str(credits))
				user_input = input(": ")
				if user_input == "quit":
					break
				elif user_input == "restart":
					credits = 100
				elif user_input == "odd":
					while True:
						try:
							bet = int(input("How much would you like to bet: "))
							bet = int(bet)
							break
						except ValueError:
							print("Invalid bet")
					if bet <= credits and bet > 0:
						dice1 = random.randrange(1, 7)
						dice2 = random.randrange(1, 7)
						dicesum = int(dice1) + int(dice2)
						print("dice 1 rolled: " + str(dice1))
						time.sleep(0.5)
						print("dice 2 rolled: " + str(dice2))
						time.sleep(0.5)
						if dicesum in odd:
							print(str(dicesum) + " is odd!")
							time.sleep(0.5)
							bet = bet*2
							credits += int(bet)
						else:
							print("You lost!")
							time.sleep(0.5)
							credits -= int(bet)
					else:
						print("Not enough credits!")
					print(credits)
				elif user_input == "even":
					while True:
						try:
							bet = int(input("How much would you like to bet: "))
							bet = int(bet)
							break
						except ValueError:
							print("Invalid bed")
					if bet <= credits and bet > 0:
						dice1 = random.randrange(1, 7)
						dice2 = random.randrange(1, 7)
						dicesum = int(dice1) + int(dice2)
						print("dice 1 rolled: " + str(dice1))
						time.sleep(0.5)
						print("dice 2 rolled: " + str(dice2))
						time.sleep(0.5)
						if dicesum in even:
							print(str(dicesum) + " is even!")
							time.sleep(0.5)
							bet = bet*2
							credits += int(bet)
						else:
							print("You lost!")
							time.sleep(0.5)
							credits -= int(bet)
					else:
						print("not enough credits!")
					print(credits)
				else:
					print("Unknown input")
		elif uinput == "2" or uinput == "highlow":
			while True:
				print("High Low Game Options:\n High = roll 4,5,6 \n Low = roll 1,2,3")
				usrinput = input(": ")
				if usrinput == "high" or usrinput == "High":
					while True:
						try:
							bet = int(input("How much would you like to bet: "))
							bet = int(bet)
							break
						except ValueError:
							print("Invalid Bet")
					if bet <= credits and bet > 0:
						print("Rolling Dices...")
						dice4 = random.randrange(1, 7)
						if dice4 in high:
							print(str(dice4) + " is high!")
							time.sleep(0.5)
							bet = bet
							credits = int(credits) + int(bet)
						else:
							print("dice rolled:" + str(dice4) + "You Lost!")
							time.sleep(0.5)
							credits = int(credits) - int(bet)
					else:
						print("Not enough credits")
					print(credits)
				if usrinput == "low" or usrinput == "Low":
					while True:
						try:
							bet = int(input("How much would you like to bet: "))
							bet = int(bet)
							break
						except ValueError:
							print("Invalid Bet")
					if bet <= credits and bet > 0:
						print("Rolling Dices...")
						dice4 = random.randrange(1, 7)
						if dice4 in low:
							print(str(dice4) + " is low!")
							time.sleep(0.5)
							bet = bet
							credits = int(credits) + int(bet)
						else:
							print("dice rolled:" + str(dice4) + "You Lost!")
							time.sleep(0.5)
							credits = int(credits) - int(bet)
					else:
						print("Not enough credits")
					print(credits)
		elif uinput == "3" or uinput == "numbers":
			print("Playing the number games guess the number!")
			while True:
				try:
					inpt = int(input("Please enter a number from 1 to 6: "))
					inpt = int(inpt)
					break
				except ValueError:
					print("Invalid number")
				if inpt < 7:
					try:
						bet = int(input("How much would you like to Bet: "))
						bet = int(bet)
						break
					except ValueError:
						print("Invalid bet")
					if bet <= credits and bet > 0:
						dice5 = random.randrange(1, 7)
						if dice5 == inpt:
							print("dice rolled: " + str(dice5) + "you chosen" + str(inpt) + "You win!")
							credits += int(bet)*6
						else:
							print("dice rolled: " + str(dice5) + "you chosen" + str(inpt) + "You lose")
							credits -= int(bet)
					else:
						print("bet error")
				else:
					print("input error")