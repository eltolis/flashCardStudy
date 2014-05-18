import os
from nose.tools import *
from bin import newstack, newcard, checkstacks, errors, cliparser

def test_stack_object():
	test_stack = newstack.Stack(1, 'Test Stack')
	assert_equal(test_stack.id, 1)
	assert_equal(test_stack.name, 'Test Stack')

def test_card_object():
	test_card = newcard.Card(1)
	assert_equal(test_card.id, 1)

def test_lookup_stack_files():
	#path = os.path.join('flashCardStudy', 'bin')
	path = os.path.join(os.getcwd(), 'bin')
	assert_equal(path, '/Volumes/DATA HD/Github/flashCardStudy/flashCardStudy/bin')
	os.chdir(path)
	assert_equal(checkstacks.lookup_stack_files(), ['stack.stk'])
	os.chdir('/Volumes/DATA HD/Github/flashCardStudy/flashCardStudy')

def test_parser_single_arg():
	assert_equal(cliparser.parse(['-n']), ['-n'])

def test_parser_multiple_args():
	cliparser.passed_args = []
	assert_equal(cliparser.parse(['-r', '-s']),['-r', '-s'])

def test_parser_fails():
	cliparser.passed_args = []
	assert_raises(SystemExit, cliparser.parse, ['-n', '-v'])
