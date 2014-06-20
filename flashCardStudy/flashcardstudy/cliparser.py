import re
import errors
from stack import get_valid_files

ARGS = [
		'-r', '--random', # 0,1
		'-s', '--stack', # 2,3
		'-n', '--new', # 4,5
		'-e', '--edit', # 6,7
		'-v', '--reverse', # 8,9
		'-w', '--write', # 10,11
		'-l', '--list', # 12,13
		'-o', '--order', # 14,15
		'--author', # 16
		'-d', '--display', # 17,18
		'-a', '--all' #19,20
		] 

single_args = [ARGS[4],ARGS[5],ARGS[12], ARGS[13],
			ARGS[14],ARGS[15],ARGS[16]]


passed_files = []
passed_args = []
output = []

def parse(args):

	if len(args) <= 1 :
		for arg in args:
			if arg in single_args:
				break
			elif arg == ARGS[19] or arg == ARGS[20]:
				break
			elif arg not in ARGS:
				errors.id(1)
			elif arg != get_valid_files(arg):
				errors.id(1)

	for arg in args:
		if arg in ARGS:
			passed_args.append(arg)
		elif arg == get_valid_files(arg):
			passed_files.append(arg)
		elif arg != get_valid_files(arg) or arg not in ARGS:
			errors.id(1)

	check_single_arg = set(passed_args).intersection(single_args)

	if len(passed_args) > 1 and check_single_arg:
		errors.id(2)
	elif check_single_arg and len(passed_files) > 0:
		errors.id(4)

	output.append(passed_files)
	output.append(passed_args)

	if len(passed_args) > 1 and ARGS[6] in passed_args or ARGS[7] in passed_args:
		errors.id(1)
	elif len(passed_files) > 1:
		if ARGS[6] in passed_args or ARGS[7] in passed_args:
			errors.id(2)
		elif ARGS[19] in passed_args or ARGS[20] in passed_args:
			errors.id(4)
	elif len(passed_files) >= 1:
		if ARGS[19] in passed_args or ARGS[20] in passed_args:
			errors.id(4)

	return output 
