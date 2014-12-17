import os
from Tkinter import *
import tkMessageBox

def settings_window():
	window = Toplevel()

home = os.path.expanduser("~")
conf_file_name = '.flashstudyrc'

def check_conf_file():
	path = os.path.join(home, conf_file_name)
	return os.path.exists(path)

def read_conf_file():
	readfile = open(conf_file_name, 'r')
	defaultdir = readfile.readline()
	return defaultdir[16:]
	readfile.close()

def check_defaultdir():
	path = 'flashcards/'
	if not os.path.exists(path):
		os.makedirs(path)

class ConfigFile():

	def __init__(self):
		self.name = conf_file_name 
		self.defaultdir = home + '/flashcards/' 

	def create_conf_files(self):
		os.chdir(home)
		conf_file = open(self.name, 'w')
		conf_file.write('DEFAULT_FOLDER='+self.defaultdir)
		conf_file.close()

