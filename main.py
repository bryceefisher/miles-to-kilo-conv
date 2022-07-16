from tkinter import *

output = 0


def button_clicked():
    output_label["text"] = round(float(input.get()) * 1.60934, 2)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=120)
window.config(padx=20, pady=20)

# Entry
input = Entry()
input.config(width=10)
input.grid(column=1, row=0)
input.insert(0, "0")

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=3, row=0)

# Is equal to Label
equal_label = Label(text="Is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

# Output Label
output_label = Label(text=output, font=("Arial", 12, "bold"))
output_label.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

# Calculate Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
