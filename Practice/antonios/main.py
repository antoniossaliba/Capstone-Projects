from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300, 150)
window.config(pady=20)

distance = 0

def conversion():
    calculation["text"] = f"is equal to\t{round(int(entry.get()) * 1.60934, 2)}\tKm"

entry = Entry(width=10)
entry.place(x=110, y=20)

miles_label = Label(text="Miles", font=("Arial", 10, "normal"))
miles_label.place(x=180, y=20)

calculation = Label(text=f"is equal to\t{distance}\tKm")
calculation.place(x=40, y=60)

calculate_button = Button(width=10, text="Calculate", command=conversion)
calculate_button.place(x=100, y=100)

window.mainloop()