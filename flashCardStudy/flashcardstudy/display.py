import os
import random
import sys
import timeit
import stack

def prompt(log):
	action = raw_input("> ")
	
	try:
		if action.lower() == 'q':
			
			if log:
				print '-' * 10

			exit(0)

	except ValueError:
		pass


def display(files, card_random, log, reverse, stack_random):

	stacks = stack.read_stack_files(files)
	print """
	Type 'Q' to stop anytime, RETURN to continue studying.
	"""
	print "Your arguments:"
	print "random cards: %s, random stacks: %s, reverse: %s, log: %s" % (card_random, stack_random, reverse, log)
	prompt(log)

	if stack_random:
		random.shuffle(stacks)
		state = 0
		while True:
			for a_stack in stacks:
				ran_stack = random.choice(stacks)
				print 'Stack name:', ran_stack[1]
				print 'Stack id:', ran_stack[0]
		
				for card_list in ran_stack[2]:

					for single_card in card_list:
						state_of_card_list = card_list[state]
						print 'Card ID', state_of_card_list[0], '/', len(card_list)
						print 'Side1', state_of_card_list[1]
						prompt(log)
						print 'Side2', state_of_card_list[2]
						if state >= len(card_list):
							state = 0
						else:
							state += 1 
						prompt(log)
						break

	while True:
		for a_stack in stacks:
			print 'Stack name:', a_stack[1]
			print 'Stack id:', a_stack[0]

			for card_list in a_stack[2]:

				for single_card in card_list:
					if card_random:
						random.shuffle(card_list)

					if reverse:
						print 'Card ID', single_card[0]
						print 'Side2', single_card[2]
						prompt(log)
						print 'Side1', single_card[1]
						prompt(log)

					print 'Card ID', single_card[0]
					print 'Side1', single_card[1]
					prompt(log)
					print 'Side2', single_card[2]
					prompt(log)
