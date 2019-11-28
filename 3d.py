
def num_chk(mylist):
	'''
	(num) -> bool
	Process list of numbers and return a list to indicate whether it is divisible by both 3 and 5.
	>>>num_chk([25, 15, 9])
	[False, True, False]
	'''
	listt = []
	for number in mylist:
		divideby3 = number%3
		divideby5 = number%5
		if (divideby3) == 0 and (divideby5) == 0:
			listt.append(True)
		else:
			listt.append(False)
	print(listt)


num_chk([25, 15, 9])