from Tkinter import *

def session(contents, randomize_cards, randomize_stacks, flip_cards):
	print contents
	print randomize_cards, randomize_stacks, flip_cards
	window = Toplevel()
	window.grab_set()
	window.title("Session")

	card_frame = Frame(window)
	card_frame.grid(row=0, column=0)

	button_frame = Frame(window)
	button_frame.grid(row=1, column=0)

	side1 = Label(card_frame)
	side1.grid(row=0, column=0)

	side2 = Label(card_frame)
	side2.grid(row=1, column=0)

	nextbutton = Button(button_frame, text="Next")
	nextbutton.grid(row=0, column=2)

	prevbutton = Button(button_frame, text="Previous")
	prevbutton.grid(row=0,column=1)

	finishbutton = Button(button_frame, text="Finish")
	finishbutton.grid(row=0,column=0, sticky=E)
