import Tkinter

#functions
def show_all():
    pass


#GUI
root = Tkinter.Tk()
root.title("workout")

label1= Tkinter.Label(root, text="helloworld")
label1.pack()

txt_input=Tkinter.Entry(root)
txt_input.pack()

btn_showall=Tkinter.Button(root, text="Show All", command=show_all)
btn_showall.pack()

root.mainloop()
