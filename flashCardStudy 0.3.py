# -*- coding: utf-8 -*-

# flashCardStudy version 0.3
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
import tty
import os

def study(cards):
	
	while True:
		randompick = random.choice(cards.keys())
		print "\n", randompick
		print "-" * 15
		
		hit = ord(sys.stdin.read(1))

		if hit == 113 or hit == 81:
			quit("Press COMMAND-W to close this window.")
		else:
			reveal = cards [randompick]
			print "\n", randompick.upper(), "=", reveal
			hit = ord(sys.stdin.read(1))
			os.system('cls' if os.name=='nt' else 'clear')

tty.setcbreak(sys.stdin)

cardsfile = open('flashcards.txt','r')

cards = {key: value for line in cardsfile.readlines() for key, value in [line.split(': ')]}

print "\nflashCardStudy 0.3"
print "*" * 18
print "by Ondrej Synacek, 2014\n"
print "Press any key to start and to reveal definitions, press 'Q' anytime to quit."

prompt = ord(sys.stdin.read(1))

if prompt == 113 or prompt == 81:
	quit("Press COMMAND-W to close this window.")
else:
	study(cards)
