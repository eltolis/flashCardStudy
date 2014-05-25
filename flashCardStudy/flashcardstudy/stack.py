import os
import glob
import json
import errors

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
				card.add_card(a_stack)
			else:
				return {} 
		

request = Helpers()

stackfiles = []

def lookup_stack_files():
	stack_files = glob.glob('*.stk')
	return stack_files

def get_valid_files(file):
	stack_files = lookup_stack_files()
	if file in stack_files:
		return file

def read_stack_files():
	stack_files = lookup_stack_files()

	for stack_file in stack_files:
		file = open(stack_file, 'r')
		processed = json.load(file.read(), sort_keys=True)
		file.close()
	
	return processed 

def requests():
	id = request.id()
	name = request.name()
	cards = request.create_cards()

	return id, name, cards

def new_stack_file():
	data = requests()
	a_stack = StackFile(*data)
	f = open(a_stack.name + '.stk', 'w')
	
	data = {a_stack.id: {a_stack.name: a_stack.cards}}
	json.dump(data, f)
	f.flush()

def get_stack_files_order():
	pass

def read_cards(stack_ID):
	pass

