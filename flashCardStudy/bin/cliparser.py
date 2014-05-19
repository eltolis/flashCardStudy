import re
import errors
from checkstacks import get_valid_files

ARGS = [
		'-r', '--random', # 0,1
		'-s', '--stack', # 2,3
		'-n', '--new', # 4,5
		'-e', '--edit', # 6,7
		'-v', '--reverse', # 8,9
		'-w', '--write', # 10,11
		'-l', '--list', # 12,13
		'-o', '--order', # 14, 15
		'--author'] # 16

single_args = [ARGS[4],ARGS[5],ARGS[6],ARGS[7],
				ARGS[12], ARGS[13], ARGS[14], ARGS[15],ARGS[16]]

#functions = {
		#ARGS[0]: random(stack=False),
		#ARGS[1]: random(stack=False),
		#ARGS[2]: stack(stack=True),
		#ARGS[3]: stack(stack=True),
		#ARGS[4]: newstack(),
		#ARGS[5]: newstack(),
		#ARGS[6]: editstack(),
		#ARGS[7]: editstack(),
		#ARGS[8]: process(reverse=True),
		#ARGS[9]: process(reverse=True),
		#ARGS[10]: log(),
		#ARGS[11]: log(),
		#ARGS[12]: list(),
		#ARGS[13]: list(),
		#ARGS[14]: orderstack(),
		#ARGS[15]: orderstack(),
		#ARGS[16]: author()}


passed_files = []
passed_args = []
output = []

def parse(args):

	if len(args) <= 1 :
		for arg in args:
			if arg in single_args:
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

	output.append(passed_files)
	output.append(passed_args)
	return output 

def process(args, reverse=False):
	pass
