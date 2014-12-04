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

	def check_contents(self): # checks if all cards been exhausted
		if all(not stack[2] for stack in self.contents): # checks if `cards` list is empty
			self.contents = deepcopy(self.original)
			self.stack_id = 0

	def request(self):
		if 'random' in self.mode:
			try:
				self.card_id = randrange(0,len(self.contents[self.stack_id][2]))
			except ValueError:
				self.stack_id += 1
			
		cards = self.contents[self.stack_id][2].pop(self.card_id)
		print 'popping: ',cards,'from stack no.: ',self.stack_id

		if 'reverse' in self.mode:
			self.side1 = cards[2]
			self.side2 = cards[1]
		else:
			self.side1 = cards[1]
			self.side2 = cards[2]

	def fetch(self):
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
				#self.flipped = True
				self.stack_id += 1
				self.request()
				self.flipped = True 
				return self.side1
				#return self.side1
			

