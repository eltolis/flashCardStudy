import os
from Tkinter import *
import tkMessageBox

def settings_window():
	window = Toplevel()

home = os.path.expanduser("~")
conf_file_name = '.flashstudyrc'
sys_separator = os.sep

def check_conf_file():
	path = os.path.join(home, conf_file_name)
	print """ check_conf_file
	""", path
	return os.path.exists(path)

def read_conf_file():
	readfile = open(os.path.join(home, conf_file_name), 'r')
	print "opening file", readfile
	defaultdir = readfile.readline()
	print "read def dir: ", defaultdir[15:]
	return defaultdir[15:]
	readfile.close()

def check_defaultdir(path):
	print "checking path -> PATH:",path, "IS?",  os.path.exists(path)
	# this is where the problem is
	# if conf file changed, creates blank dir
	# cant detect dir correctly when switched back
	# check escape chars
	if not os.path.exists(path):
		try:
			os.makedirs(path, 0777)
			print "creating dir at: ", path
		except OSError:
			print 'path exists'
			pass
	else:
		pass

class ConfigFile():

	def __init__(self):
		self.name = conf_file_name 
		self.defaultdir = os.path.join(home, 'flashcards' + sys_separator) 

	def create_conf_files(self):
		conf_file = open(os.path.join(home, self.name), 'w')
		print "created conf file: ", conf_file
		conf_file.write('DEFAULT_FOLDER='+self.defaultdir)
		conf_file.close()

