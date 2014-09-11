from Tkinter import * 
from bin import flashstudy
from flashcardstudy import sfile
from flashcardstudy import stack 

# Data
files = sfile.read_stack_files(sfile.lookup_stack_files())
print files

# Main window
root = Tk()
root.title("flashCardStudy")


# Menus
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New stack")
filemenu.add_command(label="Edit stack")
filemenu.add_separator()
filemenu.add_command(label="Exit")

# Stack browser
stack_view = LabelFrame(root, text="Stacks")
stack_view.grid(row=0, column=0, padx=5)

stack_browser = Listbox(selectmode=EXTENDED, activestyle="dotbox", exportselection=0)

def refresh_files():
	files = sfile.read_stack_files(sfile.lookup_stack_files())
	files.sort()
	return files

def refresh_stacks(files):
	stack_browser.delete(0, END)
	for a_stack in files:
		stack_browser.insert(a_stack[0], a_stack[1])

refresh_stacks(refresh_files())

stack_browser.grid(row=0, column=0, in_=stack_view, padx=3, pady=2)

# Stack buttons
stack_buttons = Frame(stack_view)
stack_buttons.grid(row=1, column=0, pady=1, sticky=W)

stack_add_button = Button(text="+")
stack_add_button.grid(row=0, column=0, in_=stack_buttons)
stack_remove_button = Button(text="-")
stack_remove_button.grid(row=0, column=1, in_=stack_buttons)

# Card browser

card_view= LabelFrame(root, text="Cards")
card_view.grid(row=0, column=1, padx=5)

card_browser= Listbox(selectmode=EXTENDED, exportselection=0)
card_browser.insert(0, "<- Select stack")
card_browser.grid(row=0, column=0, in_=card_view, padx=3, pady=2)

def selectlistbox(evt, files):
	try:
		card_browser.delete(0, END)
		w = evt.widget
		index = w.curselection()[0]
		if len(w.curselection()) > 1:
			card_browser.delete(0, END)
		else:
			selected_stack = files[int(index)]
			for cards in selected_stack[2]:
				card_browser.insert(cards[0], (cards[1], cards[2]))
	except TypeError:
		card_browser.insert(0, "Click '+' to add cards")

card_buttons = Frame(card_view)
card_buttons.grid(row=1, column=0, pady=1, sticky=W)

card_add_button = Button(text="+")
card_add_button.grid(row=0, column=0, in_=card_buttons)
card_remove_button = Button(text="-")
card_remove_button.grid(row=0, column=1, in_=card_buttons)

# Options
options = LabelFrame(root, text="Options")
options.grid(row=1, column=0, padx=5, pady=5, sticky=W)

randomize_cards_checkbutton = Checkbutton(text="Randomize cards").grid(row=0, column=0, in_=options, sticky=W)
randomize_stacks_checkbutton = Checkbutton(text="Randomize stacks").grid(row=1, column=0,in_=options, sticky=W)
flip_cards_checkbutton = Checkbutton(text="Flip cards").grid(row=2, column=0, in_=options, sticky=W)

main_buttons = Frame(root)
main_buttons.grid(row=1, column=1, rowspan=3, padx=5, pady=5, sticky=SE)
help_button = Button(text="Help").grid(row=0, column=0, in_=main_buttons)
start_button = Button(text="Start").grid(row=0, column=1,in_=main_buttons)

def binds():
	stack_browser.bind('<<ListboxSelect>>', lambda evt, arg=refresh_files():selectlistbox(evt, arg))
	stack_browser.bind('<Double-1>', lambda evt, arg=refresh_files():edit_window(evt, arg))
	card_browser.bind('<Double-1>', lambda evt, arg=refresh_files():edit_card(evt, arg))
	stack_add_button.bind('<Button-1>', edit_window)

# Edit stacks window
def edit_window(evt, files=None):

	window = Toplevel()
	entry_name = Entry(window)
	entry_name.grid(row=0,column=0,in_=window, padx=10, pady=10)
	button_frame = Frame(window)
	button_frame.grid(row=1, column=0, sticky=E, pady=(7,0))
	cancel_button = Button(button_frame, text="Cancel")
	cancel_button.grid(row=1,column=0, in_=button_frame)
	ok_button = Button(button_frame,text="OK")
	ok_button.grid(row=1,column=1, in_=button_frame)

	def get_entry():
		new_stack_name = str(entry_name.get())
		stack.new_stack_file(gui=True, filename=new_stack_name)
		#files = sfile.read_stack_files(sfile.lookup_stack_files())
		refresh_stacks(refresh_files())
		binds()

	if files:
		w = evt.widget
		index = w.curselection()[0]
		stack_name = files[int(index)][1]
		window.title("Edit stack "+"\""+str(stack_name)+"\"")
		entry_name.insert(0,stack_name)
	else:
		window.title("Add new stack")
		new_stack_name = str(entry_name.get())
		ok_button.configure(command=get_entry)


# Edit cards window
def edit_card(evt, files):
	w = evt.widget
	stack_browser_select = stack_browser.curselection()[0]
	index = w.curselection()[0]
	window = Toplevel()
	window.title("Edit card")
	cards = files[int(stack_browser_select)][2][int(index)][1:3]
	entry_side1 = Entry(window)
	entry_side1.insert(0,cards[0])
	entry_side1.pack()
	entry_side2 = Entry(window)
	entry_side2.insert(0,cards[1])
	entry_side2.pack()

binds()
root.mainloop()
