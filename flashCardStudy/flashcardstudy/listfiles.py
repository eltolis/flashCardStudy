import glob
import os

def list_stacks():
	os.chdir('../flashCardStudy/flashcards/')
	return glob.glob('*.dat')
