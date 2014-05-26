import stack
import random

	
def display(files, random=False, log=False, reverse=False, stack_random=False):

	stacks = stack.read_stack_files(files)

	stop = False

	while stop == False:
		for stack_id in stacks.keys(): #stack_id = defines stack order
			for stack_name in stacks[stack_id]: #stack_name is file name
				print 'Stack:', stack_name
				cards = stacks[stack_id][stack_name] # cards = {card_id:[side1,side2]}
				for card_id in cards: # card_id = defines card order
					print card_id

					if reverse == True:
						print cards[card_id][1]
						print cards[card_id][0]
					else:	
						print cards[card_id][0] # first side of card
						print cards[card_id][1] # second side of card
					raw_input('>')
