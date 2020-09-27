import tkinter

root = tkinter.Tk()
root.geometry('+400+200')
root.minsize(400,200)
root.title("test")

tnames = 'python','TCL','ruby'
cnames = StringVar()
cnames.set(tnames)
l = Listbox(root, listvariable = cnames,height = 10).grid()

ttk.Button(root,text = "submit",command = changeItems).grid()

root.mainloop()