import os
import random
import sys
import stack

def prompt():
	action = raw_input("> ")
	
	try:
		if action.lower() == 'q':
			exit(0)

			if log == True:
				pass

	except ValueError:
		pass


def display(files, card_random, log, reverse, stack_random):

	stacks = stack.read_stack_files(files)

	print """
	Type 'Q' to stop anytime, RETURN to continue studying.
	"""
	print "Your arguments:"
	print "random cards: %s, random stacks: %s, reverse: %s, log: %s" % (card_random, stack_random, reverse, log)
	prompt()

	while True:
		for stack_id in stacks.keys(): #stack_id = defines stack order
			for stack_name in stacks[stack_id]: #stack_name is file name
				
				cards = stacks[stack_id][stack_name] # cards = {card_id:[side1,side2]}
				
				if card_random:
					card_tuple = cards.items()
					random.shuffle(card_tuple)

					for key, card_list in card_tuple:
						os.system('clear')
						print '-' * 40 
						print stack_id , stack_name.upper(), '  card:', str(key) + '/' + str(len(cards)) 
						print '-' * 40 

						if reverse:
							random.shuffle(card_tuple)
							print card_list[1]
							prompt()
							print card_list[0]
							prompt()
							os.system('clear')
						elif not reverse:
							print card_list[0]
							prompt()
							print card_list[1]
							prompt()
							os.system('clear')
				
				else:
					for card_id in cards: # card_id = defines card order

						os.system('clear')
						print '-' * 40 
						print stack_id , stack_name.upper(), '  card:', str(card_id) + '/' + str(len(cards)) 
						print '-' * 40 

						if reverse:
							print cards[card_id][1]
							prompt()
							print cards[card_id][0]
							prompt()
							os.system('clear')
						elif not reverse:	
							print cards[card_id][0] # first side of card
							prompt()
							print cards[card_id][1] # second side of card
							prompt()
							os.system('clear')
