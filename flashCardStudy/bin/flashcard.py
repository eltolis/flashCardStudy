import sys
from flashcardstudy import errors 
from flashcardstudy.help import gethelp
from flashcardstudy.cliparser import parse, ARGS
from flashcardstudy.processor import processor

if len(sys.argv) == 1:
	errors.id(0)

elif len(sys.argv) == 1 and sys.argv[1] == '-h' or sys.argv[1] == '--help':
	gethelp()

elif len(sys.argv) >= 1:
	arguments = parse(sys.argv[1:])
	processor(arguments)
