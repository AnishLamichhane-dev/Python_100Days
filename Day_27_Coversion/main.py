import tkinter


def calc():
    """Coverts miles to km and displays the result"""
    ans_label["text"] = round(float(entry.get()) * 1.609344, 2)


# Creates window for conversion
window = tkinter.Tk()
window.title("Mile to KM converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# Entry for Mile conversion
entry = tkinter.Entry(width=15)
entry.grid(row=0, column=1)
entry.focus()

# Writes the text Miles
miles_label = tkinter.Label(text="Miles", font=("Arial", 18, "bold"))
miles_label.config(padx=20, pady=5)
miles_label.grid(row=0, column=2)

# Writes the text is equal to
is_equal_to_label = tkinter.Label(
    text="is equal to", font=("Arial", 18, "bold"))
is_equal_to_label.config(padx=20, pady=5)
is_equal_to_label.grid(row=1, column=0)

# Writes 0Km before conversion
ans_label = tkinter.Label(text="0", font=("Arial", 18, "bold"))
ans_label.config(padx=20, pady=5)
ans_label.grid(row=1, column=1)

# Button with Click me written to start calculation
button = tkinter.Button(text="Click me", command=calc)
button.grid(row=2, column=1)

# Writes the text Km
Km_label = tkinter.Label(text="Km", font=("Arial", 18, "bold"))
Km_label.config(padx=20, pady=5)
Km_label.grid(row=1, column=2)

window.mainloop()
