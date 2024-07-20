import tkinter as tk
import random

def randomize_text(event=None):
    try:
        # Get the current selection
        selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
    except tk.TclError:
        # If no text is selected, get all text
        selected_text = text_area.get("1.0", tk.END).strip()

    # Split the text into lines
    lines = selected_text.split("\n")
    # Randomize the lines
    random.shuffle(lines)

    # If no text was selected, replace all text
    if selected_text == text_area.get("1.0", tk.END).strip():
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "\n".join(lines))
    else:
        # Replace the selected text with the randomized lines
        text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
        text_area.insert(tk.INSERT, "\n".join(lines))

# Create the main window
root = tk.Tk()
root.title("Text Line Randomizer")

# Create a Text widget
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Create a Button widget
randomize_button = tk.Button(root, text="Randomize Selected Lines", command=randomize_text)
randomize_button.pack(side=tk.LEFT, pady=10, padx=5)

# Create a Labeil to indicate the hotkey
hotkey_label = tk.Label(root, text="(Ctrl+M)")
hotkey_label.pack(side=tk.LEFT)

# Bind the hotkey (Ctrl+C) to the randomize_text function
root.bind('<Control-m>', randomize_text)

# Run the Tkinter event loop
root.mainloop()

