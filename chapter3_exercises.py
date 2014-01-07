# Exercises for chapter 3:
#Exercise 3.5

def plus_line(x):
	print '+ ---- ' * x, '+'
	
def bar_line():
	print '|      |      ' * 2, '|'
	print '|      |      ' * 2, '|'
	print '|      |      ' * 2, '|'
	print '|      |      ' * 2, '|'

	
def print_box():	
	plus_line(4)
	bar_line(), bar_line()
		

def do_twice(f):
	f()
	f()

def whole_box():
	do_twice(print_box)
	plus_line(4)

whole_box()


'''
#Exercise 3.4
def do_twice(f, value):
	f(value)
	f(value)
	
def print_twice(value):
	print value
	print value
	

def do_four(f,value):
	do_twice(f, value)
	do_twice(f, value)

do_four(print_twice, 'spam')	
	
#Exercise 3.3

def right_justify(allen):
	print allen.rjust(70)

right_justify('allen')	

#Exercise 3.1 - when function call is at the top, error message occurs
#name 'repeat_lyrics' is not defined

#E 3.2 When function definitions are reverse, the program still works!
#As long as the function call is after the definition, we're fine.
	
def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack and I'm okay."
	print "I sleep all night and I work all day."
	
repeat_lyrics()
'''

# Name: JJ Kazakoff-Eigen