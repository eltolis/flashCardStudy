from newcard import add_card

class Stack(object):

	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.cards = []

def add_stack_helper():
	stack_name = raw_input("Stack name > ")

	return stack_name

def add_stack():
	a_stack = Stack(1, *add_stack_helper)
	add_card()
