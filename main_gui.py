#!/usr/bin/env python3
#
#  [Program]
#
#  Fake Name/Address Generator GUI Version
#
#  [Author]
#
#  Drew, https://github.com/Ahendrix9624/
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.

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