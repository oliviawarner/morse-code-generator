from tkinter import *
from datetime import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += "? "  # Unknown character in the input text
    return morse_code.strip()

def morse_to_text(morse):
    text = ""
    for code in morse.split(' '):
        if code in REVERSE_MORSE_CODE_DICT:
            text += REVERSE_MORSE_CODE_DICT[code]
        else:
            text += "?"  # Unknown Morse code
    return text

def convert_text():
    text = text_input.get()
    morse_code = text_to_morse(text)
    morse_output.delete(1.0, END)
    morse_output.insert(END, morse_code)

def convert_morse():
    morse = morse_input.get()
    text = morse_to_text(morse)
    text_output.delete(1.0, END)
    text_output.insert(END, text)

# GUI Setup
root = ttk.Window(themename="darkly")
root.title("Morse Code Generator")
root.geometry("800x600")

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label_style = ttk.Style()
label_style.configure("White.TLabel", foreground="white")

ttk.Label(mainframe, text="Enter Text:", style="White.TLabel").grid(row=0, column=0, sticky=W, pady=10)
text_input = ttk.Entry(mainframe, width=50)
text_input.grid(row=0, column=1, sticky=(W, E))

ttk.Label(mainframe, text="Morse Code:", style="White.TLabel").grid(row=1, column=0, sticky=NW, pady=10)
morse_output = Text(mainframe, height=5, width=50, wrap="word")
morse_output.grid(row=1, column=1, sticky=(W, E))

ttk.Button(mainframe, text="Convert to Morse", command=convert_text, bootstyle="success-outline").grid(row=2, column=0, sticky=W, pady=10)

# Adding a frame for the horizontal separator with padding
separator_frame = ttk.Frame(mainframe, padding=(20, 20))
separator_frame.grid(row=3, column=0, columnspan=2, sticky=(W, E))
separator = ttk.Separator(separator_frame, orient=HORIZONTAL)
separator.pack(fill='x')

ttk.Label(mainframe, text="Enter Morse Code:", style="White.TLabel").grid(row=4, column=0, sticky=W, pady=10)
morse_input = ttk.Entry(mainframe, width=50)
morse_input.grid(row=4, column=1, sticky=(W, E))

ttk.Label(mainframe, text="Text Output:", style="White.TLabel").grid(row=5, column=0, sticky=NW, pady=10)
text_output = Text(mainframe, height=5, width=50, wrap="word")
text_output.grid(row=5, column=1, sticky=(W, E))

ttk.Button(mainframe, text="Convert to Text", command=convert_morse, bootstyle="info-outline").grid(row=6, column=0, sticky=W, pady=10)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
