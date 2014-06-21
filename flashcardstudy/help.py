def gethelp():
	print """
	-h, --help: See this screen

	Multiple-style arguments:
	-------------------------
	You need to pass stack filename (*.stk) with these arguments:
	-d, --display: Will display stack(s) normally.
	-r, --random: Will display cards in random order (stacks are always in order)
	-s, --stack: Stacks are random as well (only with multiple stacks)
	-e, --edit: Edit stack, add/modify cards and their order
	-v, --reverse: Shows side two of card(s) first.
	-w, --write: Will display time log when the session is over. 

		Example: `python flashcard.py mystack.stk -d -r`

		This will launch flashcard with only one stack file
		named `mystack.stk' and it will display cards
		in random order. 
	
	Single-style arguments:
	-----------------------
	No need to pass stack filename for these options:
	-n, --new: Create new stack
	-l, --list: List stack(s) in current dir
	-o, --order: Only for changing order of stacks in current dir
	--author: Author info

		Example: 'python flashcard.py -n`

		Launches flashcard in new mode that allows you to create
		new stack and add cards into that stack.

	'All' argument:
	--------------
	-a, --all: Displays all stack files in current directory. This arg can be 
	followed by these:
	[ -r, -s, -v, -w] (See above)

		Example: `python flashcard.py -a -r -s`

		Will display all stacks in current dir in random order
		and cards are also shuffled.

	Stack contains cards. Cards have two sides, each contains strings. 
	Sides are flipped by keystroke. You can have multiple stacks 
	and you can display stacks and cards in order (ID) 
	or in random fashion.
"""

def author():
	print"""
	2014 Ondrej Synacek
	web: comatory.github.io
	twitter: @ondrejsynacek
	"""
