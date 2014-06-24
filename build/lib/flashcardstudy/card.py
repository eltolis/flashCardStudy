import sys
import os
import pickle
from itertools import count
from prettytable import PrettyTable
import errors
import sfile

class Card(object):

	def __init__(self, id):
		self.id = id
		content = []

class Helpers(object):

	def editing(self, files):
		while True:
			list_card_contents(files)
			read_file = sfile.read_stack_files(files)
			contents = read_file[0]
			action = raw_input("Do you want to (A)dd new card, (M)odify a card, (D)elete a card or (C)hange the order? 'Q' to quit > ")

			if action.lower() == 'a':
				old_cards = contents[2]
				new_cards = add_card(files)

				for a_card in new_cards:
					old_cards.append(a_card)

				data = [contents[0], contents[1], new_cards] 

			elif action.lower() == 'm':
				print "modify card"

			elif action.lower() == 'd':
				data = delete_card(contents)

			elif action.lower() == 'c':
				data = change_card_order(contents)
			elif action.lower() == 'q':
				break
			else:
				print "Error! Invalid command. Select only 'A', 'M', 'D', 'C' or 'Q'"
				continue

			f = open(files[0], 'wb')
			pickle.dump(data, f)
			f.close()

	def adding(self, files=None):

		finished = False
		card_count = count(1)

		if files:
			contents = sfile.read_stack_files(files)
			cards = contents[0][2]
			ids = [i[0] for i in cards]
		else:
			cards = [] 

		while finished == False:
			new_card = []
			card_id = next(card_count)
			if files:
				if card_id in ids: 
					continue

			print "Card: %d" % card_id 
			side1 = raw_input("Side one: ")
			side2 = raw_input("Side two: ")
			new_card = [card_id, side1, side2]
			cards.append(new_card)

			finished_prompt = raw_input("Press RETURN to add another card, type F to finish.")

			if finished_prompt.lower() == 'f':
				finished == True
				return cards 
			else:
				continue

requests = Helpers()

def add_card(files=None):
	cards = requests.adding(files)
	return cards

def change_card_order(contents):
	while True:
		try:
			select = int(raw_input("Please select card (ID) you want to move > "))
			moved_card = contents[2].pop(select - 1)
			print "You selected: ", moved_card
			new_position = int(raw_input("Please select new position (ID) > "))
			contents[2].insert(new_position - 1, moved_card)
		except IndexError, ValueError:
			errors.id(5,no_quit=True)

		renumber_card_order(contents)
		return contents

def delete_card(contents):
	while True:
		try:
			select = int(raw_input("Please select card (ID) you want to delete > "))
			deleted_card = contents[2].remove(contents[2][select - 1])
		except IndexError, ValueError:
			errors.id(5,no_quit=True)

		renumber_card_order(contents)
		return contents

def renumber_card_order(contents):
	for a_card in contents[2]:
		a_card[0] = contents[2].index(a_card) + 1

def list_card_contents(files):
	contents = sfile.read_stack_files(files)

	table = PrettyTable(["Card ID", "Side 1", "Side 2"])
	table.align["Side1"] = 'l'
	table.align["Side2"] = 'l'

	cards = [stack[2] for stack in contents]

	for card in cards[0]:
		side1 = (card[1][:40] + '...') if len(card[1]) > 40 else card[1]
		side2 = (card[2][:40] + '...') if len(card[2]) > 40 else card[2]
		table.add_row([card[0],side1, side2])

	print "\nStack name: %s" % stack[1]
	print table.get_string(sortby="Card ID")
