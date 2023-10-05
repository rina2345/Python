import random 
import string #when we import stirng we have access to ascii uppercase and lowercase and functions and digits instead of typing it
import PySimpleGUI as sg





sg.theme("DarkTeal9")
sg.set_options(font="Arial 15")
layout = [
    [sg.Text("Uppercase: "), sg.Push(), sg.Input(size=15, key="-UP-")],
    [sg.Text("Lowercase: "), sg.Push(), sg.Input(size=15, key="-LOW-")],
    [sg.Text("Digits: "), sg.Push(), sg.Input(size=15, key="-DIG-")],
    [sg.Text("Symbols: "), sg.Push(), sg.Input(size=15, key="-SYM-")],
    [sg.Button('OK'), sg.Button("Cancel")],
    [sg.Text("Password: "), sg.Multiline(size=15, no_scrollbar=True,  disabled=True, key="-PASS-")] # to remove the scrollbar
]

Window = sg.Window("Password Generator", layout)

while True:
    event, values = Window.read() # accessiong the evets and values by reading the window
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break # to come out of the loop
    if event == "OK":
        try:
            u_upper = int(values["-UP-"])
            upper = random.sample(string.ascii_uppercase, u_upper) #to choose uppercase and lowercase letters randomly we are uasing random module(sample) we are going to sampple the upeercase letters
            u_lower = int(values["-LOW-"])
            lower = random.sample(string.ascii_lowercase, u_lower)
            u_digits = int(values["-DIG-"])
            digits = random.sample(string.digits, u_digits)
            u_symbols = int(values["-SYM-"])
            symbols = random.sample (string.punctuation, u_symbols)

            total = upper+lower+digits+symbols
            total = random.sample(total,  len(total)) # what ever the length is give it to me randomly
            total = "".join(total) # everything will be joined without anythin in b/w them 
            Window['-PASS-'].update(total)
        
        except ValueError:
            Window['-PASS-'].update("No Valid Number")

Window.close()