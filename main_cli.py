"""
USAGE - The code uses the Python Faker library to generate a fake name and address. 
        It then copies the name and address to the clipboard using the Pyperclip library 
        and prints it to the console. It prompts the user to generate another fake address 
        or exit the program. If the user chooses to generate another fake address, 
        the function is called recursively.
        
AUTHOR - https://github.com/Ahendrix9624/
"""

from faker import Faker 
import pyperclip

def fake_data_gen():
    fake = Faker()
    name = fake.name()
    address = fake.address()

    name_address = (f"{name}\n{address}")
    pyperclip.copy(name_address)
    print(name_address)
    
    again = input("Generate a Fake Address? Y or N?").lower()
    if again == "y":
        fake_data_gen()
    else:
        exit()

fake_data_gen()
