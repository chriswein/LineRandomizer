import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
import random

def randomize_text(event=None):
    try:
        # Get the start and end indices of the current selection
        start_index = text_area.index(tk.SEL_FIRST)
        end_index = text_area.index(tk.SEL_LAST)

        # Modify the indices to select complete lines
        start_line = start_index.split('.')[0]
        end_line = end_index.split('.')[0]
        selected_text = text_area.get(f"{start_line}.0", f"{end_line}.end")
    except tk.TclError:
        # If no text is selected, get all text
        start_line = "1"
        end_line = str(int(text_area.index(tk.END).split('.')[0]) - 1)
        selected_text = text_area.get("1.0", tk.END).strip()

    # Split the text into lines
    lines = selected_text.split("\n")
    # Randomize the lines
    random.shuffle(lines)

    # Replace the selected text with the randomized lines
    text_area.delete(f"{start_line}.0", f"{end_line}.end")
    text_area.insert(f"{start_line}.0", "\n".join(lines))

    # Reselect the lines
    text_area.tag_add(tk.SEL, f"{start_line}.0", f"{end_line}.end")
    text_area.mark_set(tk.INSERT, f"{start_line}.0")
    text_area.see(tk.INSERT)

def drop(event):
    # Get the file path
    file_path = event.data.strip('{}')
    # Read the file content
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        # Insert the content into the text area
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)
    except Exception as e:
        print(f"Failed to read file: {e}")

def center_window(root, width=800, height=600):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

# Create the main window
root = TkinterDnD.Tk()
root.title("Text Line Randomizer")

# Center the window
center_window(root)

# Create a Text widget with a Scrollbar
frame = ttk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

text_area = tk.Text(frame, wrap=tk.WORD)
text_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

scrollbar = ttk.Scrollbar(frame, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)

# Create a Button widget
randomize_button = ttk.Button(root, text="Randomize Selected Lines", command=randomize_text)
randomize_button.pack(side=tk.LEFT, pady=10, padx=5)

# Create a Label to indicate the hotkey
hotkey_label = ttk.Label(root, text="(Ctrl+M)")
hotkey_label.pack(side=tk.LEFT)

# Bind the hotkey (Ctrl+M) to the randomize_text function
root.bind('<Control-m>', randomize_text)

# Enable drag and drop functionality
text_area.drop_target_register(DND_FILES)
text_area.dnd_bind('<<Drop>>', drop)

# Run the Tkinter event loop
root.mainloop()
