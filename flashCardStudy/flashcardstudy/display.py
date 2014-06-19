import os
import random
import sys
import timeit
import itertools
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
	stacks.sort()

	cards = [a_stack[2] for a_stack in stacks] 
	cards.sort()

	print """
	Type 'Q' to stop anytime, RETURN to continue studying.
	"""
	print "Your arguments:"
	print "random cards: %s, random stacks: %s, reverse: %s, log: %s" % (card_random, stack_random, reverse, log)

	if card_random:
		for s in cards:
			random.shuffle(s)

	setup = [iter(s) for s in cards]
	key = 0


	while True:

		rand_key = random.randrange(0, len(setup))
		rand_stack = setup[rand_key]

		try:
			if stack_random:
				a_card = next(rand_stack)

			else:
				try:
					a_card = next(setup[key])
				except IndexError:
					key = 0
					setup = [iter(s) for s in cards]

		except StopIteration:

			if card_random:
				for s in cards:
					random.shuffle(s)
				setup = [iter(s) for s in cards]


			if not stack_random:
				key += 1
				continue

			else:
				setup = [iter(s) for s in cards]

		side1 = 1
		side2 = 2

		if reverse:
			side1 = 2
			side2 = 1

		print a_card[side1]
		prompt(log)
		print a_card[side2]
		prompt(log)
