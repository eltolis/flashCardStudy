import os
from nose.tools import *
from bin import newstack, newcard, checkstacks, errors, cliparser

# empties out lists in parser
def parser_cleanup():
	cliparser.passed_files = [] 
	cliparser.passed_args = []
	cliparser.output = []

# STORAGE OBJECT tests (newcard, newstack)
def test_stack_object():
	test_stack = newstack.Stack(1, 'Test Stack')
	assert_equal(test_stack.id, 1)
	assert_equal(test_stack.name, 'Test Stack')

def test_card_object():
	test_card = newcard.Card(1)
	assert_equal(test_card.id, 1)

# DATA TESTS (checkstacks)
def test_lookup_stack_files():
	#path = os.path.join('flashCardStudy', 'bin')
	path = os.path.join(os.getcwd(), 'bin')
	assert_equal(path, '/Volumes/DATA HD/Github/flashCardStudy/flashCardStudy/bin')
	os.chdir(path)
	assert_equal(checkstacks.lookup_stack_files(),['example.stk','stack.stk'])
	os.chdir('/Volumes/DATA HD/Github/flashCardStudy/flashCardStudy')

# PARSER TESTS (cliparser)
def test_parser_with_no_arg():
	parser_cleanup()
	assert_raises(SystemExit, cliparser.parse, '-r')
	assert_raises(SystemExit, cliparser.parse, ' ')

def test_parser_with_single_type_arg():
	parser_cleanup()
	assert_equal(cliparser.parse(['--list']), [[],['--list']])
	
def test_parser_with_single_type_arg_and_file():
	parser_cleanup()
	assert_raises(SystemExit, cliparser.parse, ['stack.stk', '-n'])

def test_parser_with_invalid_arg():
	assert_raises(SystemExit, cliparser.parse, ['stack.stk','-q'])

def test_parser_with_files_only():
	assert_raises(SystemExit, cliparser.parse, ['stack.stk'])
	assert_raises(SystemExit, cliparser.parse, ['stack.stk','notes.stk'])

def test_parser_with_invalid_file():
	assert_raises(SystemExit, cliparser.parse, ['notes.stk','-r'])

def test_parser_with_valid_file():
	parser_cleanup()
	path = os.path.join(os.getcwd(), 'bin')
	os.chdir(path)
	assert_equal(cliparser.parse(['stack.stk', '-r']), [['stack.stk'],['-r']])

def test_parser_with_valid_file_and_args():
	parser_cleanup()
	assert_equal(cliparser.parse(['stack.stk', '-r', '-s', '-v']),[['stack.stk'],['-r', '-s', '-v']])

def test_parser_with_valid_file_and_invalid_arg():
	parser_cleanup()
	assert_raises(SystemExit, cliparser.parse, ['stack.stk', '-r', '-s', '-fail'])

def test_parser_with_invalid_single_type_arg():
	parser_cleanup()
	assert_raises(SystemExit, cliparser.parse, ['stack.stk', '-r', '--author'])
	parser_cleanup()
	assert_raises(SystemExit, cliparser.parse, ['stack.stk', 'example.stk', '-r', '--author'])
	parser_cleanup()
	assert_raises(SystemExit, cliparser.parse, ['stack.stk', 'fail.stk', '-e', '--list'])
	os.chdir('/Volumes/DATA HD/Github/flashCardStudy/flashCardStudy')

# PROCESSOR TESTS
