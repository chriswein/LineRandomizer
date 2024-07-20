import tkinter as tk
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

# Create the main window
root = tk.Tk()
root.title("Text Line Randomizer")

# Create a Text widget
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Create a Button widget
randomize_button = tk.Button(root, text="Randomize Selected Lines", command=randomize_text)
randomize_button.pack(side=tk.LEFT, pady=10, padx=5)

# Create a Label to indicate the hotkey
hotkey_label = tk.Label(root, text="(Ctrl+M)")
hotkey_label.pack(side=tk.LEFT)

# Bind the hotkey (Ctrl+M) to the randomize_text function
root.bind('<Control-m>', randomize_text)

# Run the Tkinter event loop
root.mainloop()
