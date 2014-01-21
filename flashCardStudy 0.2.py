# -*- coding: utf-8 -*-

# flashCardStudy version 0.2
#
# flashCardStudy is intended to work as paper flash cards that you might know from
# school. 
# Your flash cards are located in "flashcards.txt" file.
# Open that file to add and modify flash cards by using this format:
# key: value
# Put every flash card on new line. Save the file and run the script.

import random
import sys
import string

def study(cards):
	
	while True:
		randompick = random.choice(cards.keys())
		print "\n", randompick
		print "-" * 15
		hit = raw_input("ENTER to continue ")

		if hit == "q" or hit == "Q":
			exit(0)
		else:
			reveal = cards [randompick]
			print randompick.upper(), "=", reveal

cardsfile = open('flashcards.txt','r')

cards = {key: value for line in cardsfile.readlines() for key, value in [line.split(': ')]}

print "\nflashCardStudy"
print "*" * 14
print "by Ondrej Synacek, 2014\n"

prompt = raw_input("Press ENTER to start, type 'Q' any time to quit.")

if prompt == "q" or prompt == "Q":
	exit(0)
else:
	study(cards)