def gethelp():
	print """
	-help: See this screen

		python flashcard.py [stackname][-args]

	You need to pass stackname (*.stk) with these arguments:
	-r, --random: Will display cards in random order (stacks are always in order)
	-s, --stack: Stacks are random as well (only with multiple stacks)
	-e, --edit: Edit stack, add/modify cards and their order
	-v, --reverse: Shows side two of card(s) first.
	-w, --write: Record log file (log.txt) with time statistics

	No need to pass stackname for these options:
	-n, --new: Create new stack
	-l, --list: List stack(s) in current dir
	-o, --order: Only for changing order of stacks in current dir
	--author: Author info

	Usage:
		
		Example: `python flashcard.py mystack.stk -r`

		This will launch flashcard with only one stack file
		named `mystack.stk' and it will display cards
		in random order. 

	Stack contains cards. Cards have two sides, each contains strings. 
	Sides are flipped by keystroke. You can have multiple stacks 
	and you can display stacks and cards in order (ID) 
	or in random fashion.
"""
	
