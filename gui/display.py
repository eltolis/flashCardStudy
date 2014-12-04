from Tkinter import *
import itertools
from flashcardstudy.content import ContentObject 

def session(contents, randomize_cards, randomize_stacks, flip_cards):

	if randomize_cards == 1:
		randomize_cards = 'random'

	if randomize_stacks == 1:
		randomize_stacks = 'randomstack'
	
	if flip_cards == 1:
		flip_cards = 'reverse'

	def end():
		window.destroy()

	def start():
		side1cont.set(session.fetch())
		flipbutton.configure(command=flip)

	def flip():
		side2cont.set(session.fetch())
		flipbutton.configure(command=start)

	session = ContentObject(contents, randomize_cards, randomize_stacks, flip_cards)
		
	print "Starting session with these cards: ","\n", contents
	print "Random cards:",randomize_cards
	print "Random stacks:", randomize_stacks
	print "Flip cards:", flip_cards

	print contents

	window = Toplevel()
	window.grab_set()
	window.title("Session")

	card_frame = Frame(window)
	card_frame.grid(row=0, column=0, sticky=W, padx=2, pady=2)

	button_frame = Frame(window)
	button_frame.grid(row=1, column=0, pady=(5,0), padx=2)

	side1_frame = LabelFrame(card_frame, text="Side 1")
	side1_frame.grid(row=0, column=0)

	side1cont = StringVar()
	side2cont = StringVar()

	side1 = Label(side1_frame, textvariable=side1cont)
	side1.grid(row=0, column=0, sticky=W)

	side2_frame = LabelFrame(card_frame, text="Side 2")
	side2_frame.grid(row=1, column=0)

	side2 = Label(side2_frame, textvariable=side2cont)
	side2.grid(row=0, column=0, sticky=W)

	flipbutton = Button(button_frame, text="Flip", command=start)
	flipbutton.grid(row=0, column=2)

	finishbutton = Button(button_frame, text="End", command=end)
	finishbutton.grid(row=0,column=0, sticky=E)
	
