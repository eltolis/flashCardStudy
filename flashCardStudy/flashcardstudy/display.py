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
	stacks.sort()

	cards = [a_stack[2] for a_stack in stacks] 
	cards.sort()

	print """
	Type 'Q' to stop anytime, RETURN to continue studying.
	"""
	print "Your arguments:"
	print "random cards: %s, random stacks: %s, reverse: %s, log: %s" % (card_random, stack_random, reverse, log)
	


	stack_setup = [iter(s[2]) for s in stacks]
	key = 0

	while True:

		if stack_random:
			key = random.randrange(0, len(stack_setup))
			random_iter = stack_setup[key]

		try:
			if stack_random:
				a_card = next(random_iter)
			else:
				try:
					a_card = next(stack_setup[key])
				except IndexError:
					key = 0
					stack_setup = [iter(s[2]) for s in stacks]
					continue

		except StopIteration:
			if not stack_random:
				key += 1
				continue
			else:
				del stack_setup[key]
				stack_setup = [iter(s[2]) for s in stacks]
				continue
		
		side1 = 1
		side2 = 2

		if reverse:
			side1 = 2
			side2 = 1

		print a_card[side1]
		prompt(log)
		print a_card[side2]
		prompt(log)





	#setup_stacks = [iter(s[2]) for s in stacks]

	#key = 0

	#while True:

		#if stack_random:
			#key = random.randrange(0,len(setup_stacks))
			#a_stack = setup_stacks[key]
		
		#try:	
			#a_stack = setup_stacks[key]
			#key += 1
		#except IndexError:
			#key = 0

		#try:
			#if card_random:
				#a_card = next(a_stack)
				#random.choice(a_card)
			#else:
				#a_card = next(a_stack)

		#except StopIteration:
			#del setup_stacks[key]
			#setup_stacks = [iter(s[2]) for s in stacks]
			#continue

		#if reverse:
			#print a_card[2]
			#prompt(log)
			#print a_card[1]
			#prompt(log)
		
		#else:
			#print a_card[1]
			#prompt(log)
			#print a_card[2]
			#prompt(log)
		
