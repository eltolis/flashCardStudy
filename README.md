# flashCardStudy

This is simple command line utility aimed at anyone who wants to use memorizing technique for studying. This utility creates virtual stacks of cards, you flip the cards just as the paper flash cards. It works best for stuff like definitions or memorizing foreign words.
flashCardStudy does not use database for saving its data but instead relies on files.

## Version 0.8

* fixed parser problems
* you can know edit existing stacks (adding cards, deleting, reordering)
* modifying the cards and reordering the stacks will be possible in next version
* time logging does not work yet

## Installation

This is a standard package written in Python 2.7. Simply clone the repo, navigate to folder where `setup.py` is and simply type:

	python setup.py install

You might need to run this as _sudo_. This package will be available on PyPi shortly. Installation to `virtualenv` is simple too. If you do not want to install the package and just plainly use the utility, you will find the executable script in `bin/flashstudy.py`.

## Usage

You must feed parameters as CLI arguments for flashCardStudy to work. Bash command for this utility is `flashstudy`. For help do: 

	flashstudy -h

Every stack has an ID, name and contains the cards. Cards must always be in stack. Stack ID defines its order, stack name defines the filename. Each stack file has `.stk` extension and is simple binary file created by `Pickle` module.

Cards have their order as well which can be changed by using `-e` or `--edit` argument. You can have as many stacks containing as many cards as you want. You pass stacks (`.stk` files) as arguments plus modifier arguments. You can avoid passing filenames to utility by using `-a` or `--all` argument and combine it with modifier arguments.

## Examples

#### Create new stack

	flashstudy -n

#### Start session

	flashstudy [filename1.stk] [filename2.stk] -d -r -s

This will display cards from stacks _filename1_ and _filename2_. Utility will jump between the stacks randomly (`-s` argument) and it will also display individual cards randomly (`-r` argument).

	flashstudy --all -v

All stacks in current directory will be used, sides of the cards will be flipped because of the `-v` (also `--reverse`) argument.
You must always use either `-d` or `-a` for session to start. You can optionally add arguments (see below).

#### Edit a stack

	flashstudy [filename1.stk] --edit

This will launch interface for editing _filename1_ stack. You can add another cards here, as well as delete them. You can also reorder the cards if you want to have cards displayed in certain way.

## Arguments

`-n`  `--new`: Creates new stack file.
`-e`  `--edit`: Edit stack file.
`-l`  `--list`: List stacks and info in current directory.
`-o`  `--order`: Reorder stacks in current directory.

`-d`  `--display`: Will display/start session for given stack(s).
`-a`  `--all`: Will display/start session for all stacks in current directory.
`-r`  `--random`: Cards from stack are displayed randomly.
`-s`  `--stack`: Jumps between stacks randomly.
`-v`  `--reverse`: Flips the sides of cards.
`-w`  `--write`: Logs the duration of the session.

You must provide stack file(s) for these arguments:
`-d`  `--display`
`-r`  `--random`
`-s`  `--stack`
`-v`  `--reverse`
`-w`  `--write`

You don't provide stack file for these arguments:
`-n`  `--new`
`-e`  `--edit`
`-l`  `--list`
`-o`  `--order`
`-a`  `--all`

When using `-e` or `--edit` argument, you can only pass single stack file.

You can substitute stack files plus `-d` or `--display` with `-a` or `--all` argument.

## To be added

flashCardStudy will also probably include GUI in the future built in Tkinter so it will work on all platforms.
