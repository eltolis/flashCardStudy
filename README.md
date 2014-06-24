# flashCardStudy

A command line script that is intended for anyone who needs to memorize stuff. You can create and display virtual flash cards organized into stacks. This script is written in Python 2.7.

# Changes

- You can now create stacks and add cards to them.
- You can display cards in random order and reversed.
- You can use the `--all` argument to pass all stack files in current dir to the script.
- You can jump between stacks by using `-s` argument.

## Current implementation

For now the package is not ready but it works in shell. Clone the repo and navigate to `/bin` directory:

`python flashstudy.py [arguments]`

I will add GUI in Tkinter later on so you can use the scipt graphically.

## Arguments

When you launch `python flashstudy.py --help` you will get the help screen.

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


