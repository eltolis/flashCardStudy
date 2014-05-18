import errors

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
		#ARGS[0]: random(),
		#ARGS[1]: random(),
		#ARGS[2]: stack(),
		#ARGS[3]: stack(),
		#ARGS[4]: newstack(),
		#ARGS[5]: newstack(),
		#ARGS[6]: editstack(),
		#ARGS[7]: editstack(),
		#ARGS[8]: reverse(),
		#ARGS[9]: reverse(),
		#ARGS[10]: log(),
		#ARGS[11]: log(),
		#ARGS[12]: list(),
		#ARGS[13]: list(),
		#ARGS[14]: order(),
		#ARGS[15]: order(),
		#ARGS[16]: author()}

passed_args = []

def parse(args):
	for arg in args:
		if arg not in ARGS:
			errors.id(1)
		elif arg in single_args and len(args) >= 2:
			errors.id(2)
		else:
			passed_args.append(arg)

	return passed_args
	#process(passed_args)

def process(args):
	pass
