import tkinter as tk

def fahrenheit_to_celcius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title('temperature converter')
window.resizable(width=False, height = False )

frm_entry = tk.frame(master = window)
ent_temperature = tk.Entry(master = frm_entry, width = 10)
lbl_temp = tk.Lable(master = frm_entry, text = "\N{DEGREE FAHRENHEIT }" )

ent_temperature.grid(row = 0, column = 0, sticky = 'e')
lbl_temp.grid(row = 0, column = 1, sticky = 'w')


btn_convert = tk.Button(

master=window,

text="-->",

command=fahrenheit_to_celcius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set-up the layout using the .grid() geometry manager

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()