import os

home = os.path.expanduser("~")

class ConfigFile():

	def __init__(self):
		self.name = '.flashstudyrc'
		self.path = '~'
		self.defaultdir = home + '/flashcards/' 

	def check_conf_file(self):
		pass

	def check_def_folder():
		pass
