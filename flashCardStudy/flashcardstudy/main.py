import random
import listfiles

class Card(object):
	"""
	Defines a single flash card (card). It has two sides,
	first side is content.key, other is content['value']."""

	def __init__(self):
		self.content = {}


class Stack(object):
	"""
	Stack is a superset of class 'Card'. It has name and single
	cards are stored in list 'stacks'."""
	def __init__(self, name):
		self.name = name
		self.stacks = []

def prompt():
	return raw_input()

def add_card_helper():
	print "Add card(s)?"
	while True:
		action = prompt().lower()

		if action == 'y':
			add_card()
		elif action == 'n':
			pass
		else:
			print "Select Yes or No"

def add_card(side1, side2):
	a_card = Card()
	a_card.content[side1] = side2
	return a_card

def new_stack(name_of_stack):
	"""
	Creates new stack of cards. Arg must be passed to it
	as a nem."""
	a_stack = Stack(name_of_stack)
	if flashcard.GUI == False:
		add_card_helper()
		side1 = prompt()
		side2 = prompt()
		add_card(side1, side2)

def edit_stack(self):
	pass

def delete_stack(self):
	pass

def export_stack(self):
	pass

def import_stack(self):
	pass
