from cliparser import ARGS
from stack import new_stack_file

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

def processor(arguments):

	files = arguments[0]
	operation = arguments[1]

	if len(arguments[0]) == 0:
		if ARGS[4] in operation or ARGS[5] in operation:
			new_stack_file()
		#elif ARGS[12:13] in operation:
			#checkstacks.list_stacks()
		#elif ARGS[14:15] in operation:
			#orderstack.manager()
		#elif ARGS[16] in operation:
			#gethelp.author()
	else:
		pass
