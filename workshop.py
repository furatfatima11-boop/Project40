from tkinter import *
from datetime import date
root = Tk()
root.title("Demo Window")
root.geometry('400x300')
lbl = Label(text="Sign up for the workshop here!",fg="white",bg="purple",height= 1,width= 300)
name_lbl = Label(text="Full Name:",bg="purple", fg="white")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message 
    message = "Thanks for signing up "+name+"!""\n The workshop will take place on December 5th.""\n Today's date is "
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height =5)
btn = Button(text = "Check In",command=display,height = 1,bg="purple",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
text_box.pack()
btn.pack()
root.mainloop()