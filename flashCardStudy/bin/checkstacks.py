import os
import glob
import errors

def lookup_stack_files():
	stack_files = glob.glob('*.stk')
	return stack_files

def get_valid_files(file):
	stack_files = lookup_stack_files()
	if file in stack_files:
		return file

