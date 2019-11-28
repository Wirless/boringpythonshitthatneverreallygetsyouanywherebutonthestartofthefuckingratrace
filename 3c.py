notnative = 'j,k,q,v,w,x,y,z,J,K,Q,V,W,X,Y,Z'
numbers = '1,2,3,4,5,6,7,8,9,0'

word = input("Please enter a word: ")

for char in word:   
	if char in notnative:    
		print (char, end=" is not Gaelic")
		print()
	elif char in numbers:
		print(char)
	else:
		print (char, end=" is valid native Irish")
		print()