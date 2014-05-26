import stack

def display(files, random=False, log=False, reverse=False, stack=False, all=False):

	if not all:
		stacks = stack.read_stack_files(files)

	stop = False

	while stop == False:
		print stacks
		
