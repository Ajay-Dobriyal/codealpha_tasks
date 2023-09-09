import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import requests
from bs4 import BeautifulSoup

# Create a Translator instance
translator = Translator()

# Function to perform translation
def translate_text():
    text_to_translate = input_text.get(1.0, "end-1c")
    source_lang = source_language.get()
    target_lang = target_language.get()
    
    try:
        translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        output_text.delete(1.0, "end")
        output_text.insert("end", translated_text.text)
    except Exception as e:
        output_text.delete(1.0, "end")
        output_text.insert("end", "Translation Error")

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Input text area
input_label = ttk.Label(root, text="Enter text to translate:")
input_label.pack()

input_text = tk.Text(root, height=5, width=40)
input_text.pack()

# Source language dropdown
source_language_label = ttk.Label(root, text="Select source language:")
source_language_label.pack()

source_language = ttk.Combobox(root, values=list(LANGUAGES.values()))
source_language.set("English")  # Set default source language to English
source_language.pack()

# Target language dropdown
target_language_label = ttk.Label(root, text="Select target language:")
target_language_label.pack()

target_language = ttk.Combobox(root, values=list(LANGUAGES.values()))
target_language.set("Spanish")  # Set default target language to Spanish
target_language.pack()

# Translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Output text area
output_text = tk.Text(root, height=5, width=40)
output_text.pack()

root.mainloop()
