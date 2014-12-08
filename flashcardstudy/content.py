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

	def check_contents(self): # checks if all cards been exhausted
		print 'total stacks left: ', len(self.contents)
		if 'randomstack' in self.mode or 'wildcard' in self.mode:
			print 'check'
			if len(self.contents[self.stack_id][2]) == 0:
				print 'deleting -> ',self.contents[self.stack_id][1]
				self.contents.pop(self.stack_id)
				self.stack_id = 0
				self.card_id = 0
				self.switched_stack = False

		if all(not stack[2] for stack in self.contents): # checks if `cards` list is empty
			self.contents = deepcopy(self.original)
			self.stack_id = 0
			self.card_id = 0
			self.switched_stack = False

	def request(self):

		if 'randomstack' in self.mode and not self.switched_stack:
			self.stack_id = randrange(0,len(self.contents))
			self.switched_stack = True

		if 'random' in self.mode:
			try:
				self.card_id = randrange(0,len(self.contents[self.stack_id][2]))
			except ValueError:
				self.stack_id += 1
				self.card_id = randrange(0,len(self.contents[self.stack_id][2]))

		if 'wildcard' in self.mode:
			self.card_id = randrange(0,len(self.contents[self.stack_id][2]))
			self.stack_id = randrange(0,len(self.contents))
			self.check_contents()
			print 'generated stack: ', self.stack_id, 'card: ', self.card_id
			
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
