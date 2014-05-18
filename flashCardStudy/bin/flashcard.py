#Command line interface for flashCardStudy

import sys
import errors
from help import gethelp
from cliparser import parse, ARGS, process

if len(sys.argv) == 1:
	errors.id(0)

elif len(sys.argv) == 1 and sys.argv[1] == 'help' or sys.argv[1] == '-help':
	gethelp()

elif len(sys.argv) => 1:
	arguments = parse(sys.argv[1:])
	process(arguments)
