from cliparser import ARGS
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

	if len(arguments[0]) == 0:
		if ARGS[4] in operation or ARGS[5] in operation:
			new_stack_file()
		elif ARGS[19] in operation or ARGS[20] in operation:
			files = lookup_stack_files()
			display(files)
	else:
		if ARGS[8] in operation or ARGS[9] in operation:
			display(files,reverse=True)
		elif ARGS[17] in operation or ARGS[18] in operation:
			display(files)
