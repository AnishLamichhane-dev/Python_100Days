from tkinter import *
import requests


def get_quote():
    kanye_quote_response = requests.get(url="https://api.kanye.rest")
    kanye_quote_response.raise_for_status()

    kanye_quotes_data = kanye_quote_response.json()["quote"]
    return (kanye_quotes_data)


def new_quote():
    canvas.itemconfig(quote_text, text=get_quote())


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=f"{get_quote()}", width=250, font=(
    "Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=new_quote)
kanye_button.grid(row=1, column=0)

mainloop()
