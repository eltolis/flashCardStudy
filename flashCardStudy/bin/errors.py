import sys

def id(num):

	if num == 0:
		error = """
Error! No arguments passed. Use `-help` to see more."""
	elif num == 1:
		error = """
Error! Invalid arguments. Use `-help` to see more."""
	elif num == 2:
		error = """
Error! You cannot use this argument in this combination.
Use `help` to see more."""

	print error
	exit(0)
