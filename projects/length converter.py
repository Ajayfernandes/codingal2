import tkinter as tk

def inches_to_cm():
    inches = ent_length.get()
    cm = inches * 2.54
    lbl_result["text"] = f"{round(cm, 2)} \N{CM INCHES}"

window = tk.Tk()
window.title('legth converter')
window.resizable(width=False, height = False )

frm_entry = tk.frame(master = window)
ent_temperature = tk.Entry(master = frm_entry, width = 10)
lbl_temp = tk.Lable(master = frm_entry, text = "\N{CM INCHES}" )

ent_temperature.grid(row = 0, column = 0, sticky = 'e')
lbl_temp.grid(row = 0, column = 1, sticky = 'w')


btn_convert = tk.Button(

master=window,

text="-->",

command=inches_to_cm
)
lbl_result = tk.Label(master=window, text="\N{CM INCHES}")

# Set-up the layout using the .grid() geometry manager

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()