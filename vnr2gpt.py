import pyperclip
import openai
import time
import tkinter as tk
from tkinter import scrolledtext

# Set up your OpenAI API key
openai.api_key = '############'

def translate_text(text):
    """Translate text from Japanese to Chinese using OpenAI's ChatGPT API."""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"With no other words, translate the following Japanese text to Chinese: {text}"}
        ]
    )
    return response['choices'][0]['message']['content']

def update_translation():
    """Check the clipboard for new text and update the translation."""
    global previous_text

    current_text = pyperclip.paste()

    if current_text != previous_text and current_text.strip():
        translated_text = translate_text(current_text)
        output_text.delete(1.0, tk.END)  # Clear previous text
        output_text.insert(tk.END, f"Detected Japanese Text:\n{current_text}\n\nTranslated Chinese Text:\n{translated_text}\n")

        # Update previous_text to current_text
        previous_text = current_text

    # Schedule the next check
    root.after(1000, update_translation)

# Create the main tkinter window
root = tk.Tk()
root.title("Japanese to Chinese Translator")

# Create a scrolled text area for output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10)
output_text.pack(padx=10, pady=10)
font_size = 16  # Change this value to make the font larger or smaller
output_text.configure(font=("MS_mincho", font_size))
# Initialize previous_text to an empty string
previous_text = ""

# Start checking the clipboard
update_translation()

# Run the GUI main loop
root.mainloop()
