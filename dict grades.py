dict = {}
def gradings():
	'''
	Write a function that takes in nothing and returns
	a dict of student names with a single grade.
	The function loops, asking the user to enter a name,
	enter a grade, and stores them as a key-value pair.
	once the user enters an empty str for a username the function returns the dict
	( name + grade) - >
	 dict.(name,grade),-||-...
	'''
	while True:
		name = input("Please enter a student name: ")
		grade = input("Please enter a grade: ")
		if name == "" or grade == "":
			break
		else:
			dict[name] = grade
	print(dict, end=" ")

	
gradings()