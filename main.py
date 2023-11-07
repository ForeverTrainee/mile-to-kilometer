import tkinter


def button_cliced():
    miles = input.get()
    kilometers = float(miles) * 1.6
    label_kilometers.config(text=kilometers)



# Window
window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(width=20, height=200)
window.config(padx=20,pady=20)

# Label
label = tkinter.Label(text="is equal to")
label.grid(column=0,row=1)
label.config(padx=0,pady=0)


miles_kilometers = tkinter.Label(text="Miles")
miles_kilometers .grid(column=2,row=0)
miles_kilometers.config(padx=0)

label_kilometers = tkinter.Label(text="",anchor="center")
label_kilometers.grid(column=1,row=1)
label_kilometers.config(padx=10)

label_kilometers_text = tkinter.Label(text="Km")
label_kilometers_text .grid(column=3,row=1)
label_kilometers_text .config(padx=0)

# Button
button = tkinter.Button(text="Calculate", command=button_cliced)
button.grid(column=1,row=3)

# Entry
input = tkinter.Entry(width=5)
input.get()
input.grid(column=1,row=0)

window.mainloop()
