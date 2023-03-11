"""
USAGE - This code generates fake name and address data using the Faker library and displays 
        it in a GUI window created using the tkinter library. 
        The "Generate Fake Data" button triggers the data generation and displays it in a text box. 
        The generated data is also copied to the clipboard using the pyperclip library. 
        If the text box is not empty, the data generation is repeated until an empty text box is generated.
        
AUTHOR - https://github.com/Ahendrix9624/
"""
from faker import Faker 
from tkinter import *
import pyperclip

BACKGROUND_COLOR = "red"

########################## DATA GEN #################################

def data_gen():
    entry = text_box.get("1.0",'end-1c')
    
    if len(entry) == 0:
        fake = Faker()
        name = fake.name()
        address = fake.address()
        text_box.insert(END, f"{name}\n{address}")
        entry = text_box.get("1.0",'end-1c')
        pyperclip.copy(entry)
    else:
        text_box.delete("1.0",'end-1c')
        data_gen()
        
########################## UI SETUP #################################
window = Tk()
window.title("Fake Name/Address Generator")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

generate_button = Button(text="Generate Fake Data", command=data_gen, width=23, height=5, highlightbackground=BACKGROUND_COLOR)
generate_button.pack()

text_box = Text(width=34, height=5)
text_box.pack()

window.mainloop()
