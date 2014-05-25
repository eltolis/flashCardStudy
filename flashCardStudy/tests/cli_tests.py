import sys
import StringIO
import glob
import os
from nose.tools import *
import mock
import json
from flashcardstudy import stack, errors, cliparser, stack

	
def parser_cleanup():
	cliparser.passed_files = [] 
	cliparser.passed_args = []
	cliparser.output = []

def files_cleanup():
	files = stack.lookup_stack_files()
	for file in files:
		truncfile = open(file, 'w')
		truncfile.truncate()
		truncfile.close()

def delete_files():
	files = glob.glob('*.stk')
	for file in files:
		os.remove(file)

def create_test_files():
	f1 = open('example.stk','w')
	f2 = open('stack.stk','w')
	f1.close()
	f2.close()

# DATA TESTS (stack)

def test_lookup_stack_files():
	create_test_files()
	assert_equal(stack.lookup_stack_files(),['example.stk','stack.stk'])
	delete_files()


def test_request_file_info():
	sys.stdin = StringIO.StringIO('1\nexample\nno\n')
	assert_equal(stack.requests(), (1, 'example', {}))

def test_new_stack_file():
	sys.stdin = StringIO.StringIO('1\nexample\nno\n')
	stack.new_stack_file()
	assert_equal(stack.lookup_stack_files(), ['example.stk'])
	delete_files()

#def test_get_list_of_stack_files():
	#files_cleanup()
	#data = ['one', 'two', 3, 4]
	#f = open('example.stk','w')
	#json.dumps(data, f)
	#f.close()
	#data2 = ['one', 'two', 3, 4]
	#f2 = open('stack.stk','w')
	#json.dumps(data, f2)
	#f2.close()
	#assert_equal(stack.read_stack_files(), data)
	#assert_equal(stack.read_stack_files(), data2)


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
	assert_raises(SystemExit, cliparser.parse, ['stack.stk','notes.stk','-r'])
	assert_raises(SystemExit, cliparser.parse, ['fail.stk', '-v'])

def test_parser_with_valid_file():
	parser_cleanup()
	create_test_files()
	assert_equal(cliparser.parse(['stack.stk', '-r']), [['stack.stk'],['-r']])

def test_parser_with_valid_file_and_args():
	parser_cleanup()
	assert_equal(cliparser.parse(['stack.stk', '-r', '-s', '-v']),[['stack.stk'],['-r', '-s', '-v']])
	delete_files()

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

# PROCESSOR TESTS

