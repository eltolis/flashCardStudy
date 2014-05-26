from cliparser import ARGS, single_args
from stack import new_stack_file, lookup_stack_files
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
		elif ARGS[19] in operation or ARGS[20] in operation:

			card_random = False
			log = False
			reverse = False
			stack_random = False

			if ARGS[8] in operation or ARGS[9] in operation:
				reverse=True
			elif ARGS[0] in operation or ARGS[1] in operation:
				card_random = True
			elif ARGS[2] in operation or ARGS[3] in operation:
				stack_random = True
			elif ARGS[10] in operation or ARGS[11] in operation:
				log = True

			files = lookup_stack_files()
			display(files, card_random, log, reverse, stack_random)
	else: # for files plus args
		if ARGS[17] in operation or ARGS[18] in operation:

			card_random = False
			log = False
			reverse = False
			stack_random = False

			if ARGS[8] in operation or ARGS[9] in operation:
				reverse=True
			elif ARGS[0] in operation or ARGS[1] in operation:
				card_random = True
			elif ARGS[2] in operation or ARGS[3] in operation:
				stack_random = True
			elif ARGS[10] in operation or ARGS[11] in operation:
				log = True

			display(files, card_random, log, reverse, stack_random)
