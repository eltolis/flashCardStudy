import os
import glob
import pickle
from flashcardstudy import errors, card

class StackFile(object):

	def __init__(self, id, name, cards):
		self.id = id
		self.name = name
		self.cards = cards

class Helpers(object):

	def id(self):
		while True:
			try:
				prompt = int(raw_input("Stack ID? "))
				return prompt

			except ValueError:
				print "Use numbers only."

	def name(self):
		while True:
			prompt = raw_input("Stack name? ")

			if len(prompt) > 0:
				return prompt
			else:
				print "Cannot use blank name. Try again.\n"

	def create_cards(self):
		while True:
			prompt = raw_input("Add cards to stack? Y/N\n")

			if 'Y' in prompt or 'y' in prompt:
				cards = card.add_card()
			else:
				cards = {}

			return cards
		

request = Helpers()


def lookup_stack_files():
	stack_files = glob.glob('*.stk')
	return stack_files

def get_valid_files(file):
	stack_files = lookup_stack_files()
	if file in stack_files:
		return file

def read_stack_files(stack_files):

	contents = {}
	for stack_file in stack_files:
		file = open(stack_file, 'rb')
		processed = pickle.load(file)
		contents.update(processed)
		file.close()
		
	return contents 

def requests():
	id = request.id()
	name = request.name()
	cards = request.create_cards()

	return id, name, cards

def new_stack_file():
	data = requests()
	a_stack = StackFile(*data)
	f = open(a_stack.name + '.stk', 'wb')
	
	data = {a_stack.id: {a_stack.name: a_stack.cards}}
	pickle.dump(data, f)
	f.close()

def get_stack_files_order():
	pass

def read_cards(stack_ID):
	pass

