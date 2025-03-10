from tkinter import *
from datetime import date
window = Tk()

window.title('demo window')
window.geometry('400x300')
window.mainloop()
lbl = Label(text = "Hey there!", fg = 'white',bg = '##32a862',height=1, width = '300')
name_lbl = Label(text = 'full name', bg = '#32a862')
name_entry = Entry()
def display():
    name = name_entry.get
    global message
    message = 'Welcome to the application /n todays date is :'
    greet = 'hello'+name+"/n"

    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END, date.today())

text_box = Text(height=3)
btn = Button(text = 'begin', command = display, height = 2,bg = '#32a862', fg = 'white' )
lbl.pack()

name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()