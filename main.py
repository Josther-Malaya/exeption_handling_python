import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            # Evaluate the expression safely
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            entry.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Error", "Invalid input!")
            entry.delete(0, tk.END)

    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 15")
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", click)

# Run the application
root.mainloop()