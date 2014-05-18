class Card(object):

	def __init__(self, id):
		self.id = id
		content = []

def add_card_helper():
	print "\nType ++done to save cards in stack"
	side1 = raw_input("Side one > ")
	side2 = raw_input("Side two > ")

	return side1, side2

def add_card():
	a_card = Card(1)
	a_card.content.append(*add_card_helper())
