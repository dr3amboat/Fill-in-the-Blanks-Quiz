# Fill-in-the-blanks game for Udacity IPND Stage 2

BLANKS = ["___1___", "___2___", "___3___", "___4___"]

GREETINGS = """\t\t\t\t PYTHON FILL IN THE BLANKS QUIZ
\nTest your Python knowledge!
Choose your level of difficulty. Answer when prompted to fill in the blanks.
"""

easy_block = """\nIn Python, ___1___ are identified as a contiguous set of characters represented in quotation marks.
Python allows for either pairs of single or double quotes. Subsets of ___1___ can be taken using the slice
operator ([] and [:]).

A ___2___ contains items separated by commas and enclosed within square brackets ([]). Like ___1___, values stored
in a ___2___ can be accessed using the slice operator ([] and [:]).

A ___3___ is another sequence data type that is similar to the ___2___. A ___3___ consists of a number of values
separated by commas. Unlike ___2___s, however, ___3___s are enclosed within parentheses and are immutable.

With a ___4___, you don't store information in a sequence; instead, you store it in key-value pairs. Keys are unique
within a ___4___ while values may not be. The values of a ___4___ can be of any type, but the keys must be of an 
immutable date type.
"""
easy_answers = ["strings", "list", "tuple", "dictionary"]

medium_block = """\nA ___1___ is a user-defined prototype for an object that defines a set of attributes that
characterise any object of the ___1___. The attributes are data members and ___2___, accessed via dot notation.

A ___2___ is a special kind of function that is defined in a ___1___ definition.

A ___3___ a special ___2___ that is automatically invoked right after a new object is created. The ___3___ 
___2___, __init__() is usually used to set up the initial attribute values of an object.

One of the key elements of OOP is ___4___, which allows you to base a new class on an existing one. By 
doing so, the new class automatically gets (or inherits) all of the methods and attributes of the existing 
class.
"""
medium_answers = ["class", "method", "constructor", "inheritance"]

hard_block = """\nIn an object-oriented program like Python, you can restrict access to methods and variables.
This can prevent data from being modified by accident and is known as ___1___.

The process of using an operator or function in different ways for different data input is called ___2___.
In practical terms, ___2___ means that if class B inherits from class A, it doesn't have to inherit everything
about class A; it can do some of the things that class A does differently.

In object-oriented programming theory, ___3___ is a technique of managing complexity of computer systems.
It works by establishing a level of complexity in which a person interacts with the system, suppressing the 
more complex details below the current level.

It might sound that ___1___ is similar to ___3___. That's because they're closely related as ___1___ is a 
principal of ___3___. In simpler terms, ___3___ saves you from worrying about the details while ___1___ hides
the details from you.

The process of defining something in terms of itself is called ___4___. We know that in Python, a function 
can call other functions. It is even possible for the function to call itself. These type of construct are 
termed as recursive functions.
"""

hard_answers = ["encapsulation", "polymorphism", "abstraction", "recursion"]

def guess(score):
	'''Prompts the user for their answer'''
	guess = raw_input("\nEnter your answer for {} : ".format(score)).lower()
	return guess


def choose_level():
	'''Asks user for desired level then returns corresponding
	block and answer key'''
	level = ""
	print "LEVELS: \t EASY \tMEDIUM \tHARD"
	levels = ["EASY", "MEDIUM", "HARD"]
	while level not in levels:
		level = raw_input("Choose a level: ").upper()
		if level == "EASY":
			return easy_block, easy_answers
		elif level == "MEDIUM":
			return medium_block, medium_answers
		elif level == "HARD":
			return hard_block, hard_answers
		else:
			print "Invalid input."
	
	

def main():
	'''Main engine of the game. Starts up the game and ends
	game by congratulating successful players.'''
	score = 0
	print GREETINGS
	user_level, answer = choose_level()
	while score < len(BLANKS):
		print user_level
		user_guess = guess(BLANKS[score])
		if user_guess == answer[score]:
			print "\nCorrect! Well done.\n"
			user_level = user_level.replace(BLANKS[score], user_guess)
			score += 1
		else:
			print "\nSorry, try again.\n"
	print "Congratulations! You have filled in all the blanks correctly. \n"
	print user_level
	raw_input("Press the enter key to exit.")
			

main()
