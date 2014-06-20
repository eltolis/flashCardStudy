from cliparser import ARGS, single_args
from stack import new_stack_file, lookup_stack_files, list_stacks
from card import list_card_contents
from display import display

#ARGS = [
		#'-r', '--random', # 0,1
		#'-s', '--stack', # 2,3
		#'-n', '--new', # 4,5
		#'-e', '--edit', # 6,7
		#'-v', '--reverse', # 8,9
		#'-w', '--write', # 10,11
		#'-l', '--list', # 12,13
		#'-o', '--order', # 14,15
		#'--author', # 16
		#'-d', '--display', # 17,18
		#'-a', '--all' #19,20
		#] 

def processor(arguments):

	files = arguments[0]
	operation = arguments[1]

	if len(files) == 0: # for file-less args 
		if ARGS[4] in operation or ARGS[5] in operation:
			new_stack_file()
		elif ARGS[12] in operation or ARGS[13] in operation:
			list_stacks()
		elif ARGS[19] in operation or ARGS[20] in operation:

			card_random = False
			log = False
			reverse = False
			stack_random = False
			
			for item in operation:
				if ARGS[0] == item or ARGS[1] == item:
					card_random = True
				elif ARGS[10] == item or ARGS[11] == item:
					log = True
				elif ARGS[8] == item or ARGS[9] == item:
					reverse=True
				elif ARGS[2] == item or ARGS[3] == item:
					stack_random = True

			files = lookup_stack_files()
			display(files, card_random, log, reverse, stack_random)
	else: # for files plus args
		if ARGS[17] in operation or ARGS[18] in operation:

			card_random = False
			log = False
			reverse = False
			stack_random = False
			
			for item in operation:
				if ARGS[0] == item or ARGS[1] == item:
					card_random = True
				elif ARGS[10] == item or ARGS[11] == item:
					log = True
				elif ARGS[8] == item or ARGS[9] == item:
					reverse=True
				elif ARGS[2] == item or ARGS[3] == item:
					stack_random = True

			display(files, card_random, log, reverse, stack_random)
		elif ARGS[6] in operation or ARGS[7] in operation:
			list_card_contents(files)
