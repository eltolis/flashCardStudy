import sys

def id(num,no_quit=None):
	
	print_help = "\nAdd `--help` or '-h' to see more."

	if num == 0:
		error = """
Error! No arguments passed."""
	elif num == 1:
		error = """
Error! Invalid arguments (filename or arg)."""
	elif num == 2:
		error = """
Error! You cannot use this argument in this combination."""
	elif num == 3:
		error = """
Error! You must append argument to launch the program."""
	elif num == 4:
		error = """
Error! Don't use this argument with file(s)."""
	elif num == 5:
		error = """
Error! Invalid card ID. Try again."""

	print error, print_help

	if no_quit:
		pass
	else:
		exit(0)
