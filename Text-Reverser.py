# Import Gui Tools
import tkinter as tk
from tkinter import messagebox

# Reverse text and show popup
def reverse_text():
    user_input = entry.get()
    reversed_result = user_input[::-1]
    messagebox.showinfo("Reversed Text", f"🔁 {reversed_result}")

# Create main window
window = tk.Tk()
window.title("Text Reverser")
window.geometry("300x200")

# Add instructions
label = tk.Label(window, text= "Enter text to reverse")
label.pack(pady=10)

# Add input box
entry = tk.Entry(window, width= 30)
entry.pack()

# Add reverse button
button = tk.Button(window, text="Reverse", command=reverse_text)
button.pack(pady=10)

# Run the app
window.mainloop()