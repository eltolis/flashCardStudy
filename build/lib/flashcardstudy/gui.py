from Tkinter import *
import sys
import main
import listfiles
import gui_newstack

# Quit app
def quit_command():
	exit(0)

# Main window

root = Tk()
root.geometry("450x450+300+300")
root.title('flashCardStudy')

# Menubar
menubar = Menu(root)

# File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New stack")
filemenu.add_command(label="Export stack")
filemenu.add_command(label="Import stack")
filemenu.add_command(label="Quit", command=quit_command)

# Help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help")
helpmenu.add_command(label="About")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Buttons
newbutton = Button(text="New stack").grid(column=2, row=2)
editbutton = Button(text="Edit stack").grid(column=2, row=3)
deletebutton = Button(text="Delete stack").grid(column=2, row=4)

# Filebox label
fileboxlabel = Label(text="Select stack(s):").grid(column=1, row=1, sticky=W)

# Filebox
files = Listbox(root)

for item in listfiles.list_stacks():
	files.insert(END, item)

files.grid(column=1, row=2, rowspan=10)


root.mainloop()

if __name__ == '__main__':
	main()
