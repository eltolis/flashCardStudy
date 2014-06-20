import os
import glob
import pickle
from itertools import *
from prettytable import PrettyTable
from flashcardstudy import errors, card

class StackFile(object):

	def __init__(self, id, name, cards):
		self.id = id
		self.name = name
		self.cards = cards

class Helpers(object):

	def id(self):
		stacks = lookup_stack_files()
		contents = read_stack_files(stacks)
		an_id = count(1)
		
		if len(stacks) == 0:
			return 1
		else:
			intersection = [s for s in contents if s[0] != an_id]
			for s in contents:
				if next(an_id) in intersection:
					return next(an_id)

		return next(an_id)


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
				cards = [] 

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

	contents = [] 
	for stack_file in stack_files:
		file = open(stack_file, 'rb')
		processed = pickle.load(file)
		contents.append(processed)
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
	
	data = [a_stack.id, a_stack.name, a_stack.cards]
	pickle.dump(data, f)
	f.close()

def list_stacks():
	stacks = lookup_stack_files()
	contents = read_stack_files(stacks)
	
	table = PrettyTable(["Stack ID","Stack Name","Cards","Contents"])
	table.align["Contents"] = 'l'

	for stack in contents:
		stackname = (stack[1][:10] + '...') if len(stack[1]) > 10 else stack[1]
		stack_cards = [item[1:3] for item in stack[2]]
		display_cards = []
		for a_card in stack_cards:
			for card_cont in a_card:
				trunc_card = (card_cont[:15] + '...') if len(card_cont) > 15 else card_cont
				display_cards.append(trunc_card)

		table.add_row([stack[0],stackname, len(stack[2]), display_cards[0:4]])
	
	print '\n', table.get_string(sortby="Stack ID")
