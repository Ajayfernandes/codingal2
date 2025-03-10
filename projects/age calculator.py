from tkinter import *

root = Tk()
root.title('Age calculator')
root.geometry('2400x400')

frame = Frame(master = root, height = 200, width = 360, bg = 'yellow')

lbl1 = Label(frame, text = 'year of birth', bg = "blue", fg = "white", width = 12)

year_entry = Entry(frame)



def display():
    age = 2025 - int(year_entry.get())
    message = "you are", age, "years old!"
    textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed

btn = Button(text=" calculate", command=display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
year_entry.place(x=150, y=20)
btn.place(x=130, y=210)
textbox.place(y=250)
root.mainloop()