import timeit
from random import randrange
from copy import deepcopy

class ContentObject():


	def __init__(self,contents,*mode):
		self.contents = contents
		self.original = deepcopy(self.contents) # preserves original data
		self.mode = mode # random,reverse,random stack as string
		self.stack_id = 0
		self.card_id = 0
		self.side1 = ''
		self.side2 = ''
		self.flipped = False # determines whether to show side1 or side2
		self.switched_stack = False
		self.tic = timeit.default_timer() 

	def get_time(self):
		toc = timeit.default_timer()
		return toc - self.tic

	def check_contents(self): # checks if all cards been exhausted
		if 'randomstack' in self.mode or 'wildcard' in self.mode:
			if len(self.contents[self.stack_id][2]) == 0:
				self.contents.pop(self.stack_id)
				self.stack_id = 0
				self.card_id = 0
				self.switched_stack = False

		if all(not stack[2] for stack in self.contents): # checks if `cards` list is empty
			self.contents = deepcopy(self.original)
			self.stack_id = 0
			self.card_id = 0
			self.switched_stack = False
			
	def generate_stack_id(self):
		return randrange(0,len(self.contents))

	def generate_card_id(self):
		return randrange(0,len(self.contents[self.stack_id][2]))

	def request(self):

		if 'randomstack' in self.mode and not self.switched_stack:
			self.stack_id = self.generate_stack_id()
			self.switched_stack = True

		if 'random' in self.mode:
			try:
				self.card_id = self.generate_card_id() 
			except ValueError:
				self.stack_id += 1
				self.card_id = self.generate_card_id() 

		if 'wildcard' in self.mode:
			self.stack_id = self.generate_stack_id() 
			self.card_id = self.generate_card_id()
			self.check_contents()
			
		cards = self.contents[self.stack_id][2].pop(self.card_id)

		if 'reverse' in self.mode:
			self.side1 = cards[2]
			self.side2 = cards[1]
		else:
			self.side1 = cards[1]
			self.side2 = cards[2]

	def fetch(self):
		print self.contents
		self.check_contents()
		if self.flipped:
			self.flipped = False 
			return self.side2
		else:
			try:
				self.request()
				self.flipped = True 
				return self.side1
			except IndexError:
				self.stack_id += 1
				self.request()
				self.flipped = True 
				return self.side1
