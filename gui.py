import tkinter as tk
from tkinter import messagebox
from engine import CalculatorEngine

class CalculatorGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("OOP Calculator (Modular)")
        self.root.geometry("300x400")

        self.engine = CalculatorEngine()
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, font="Arial 20")
        self.entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]

        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")

            for btn in row:
                button = tk.Button(frame, text=btn, font="Arial 15")
                button.pack(side="left", expand=True, fill="both")
                button.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        text = event.widget.cget("text")

        if text == "=":
            self.calculate()
        elif text == "C":
            self.clear()
        else:
            self.entry.insert(tk.END, text)

    def calculate(self):
        expression = self.entry.get()
        try:
            result = self.engine.evaluate(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))
            self.clear()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.clear()

    def clear(self):
        self.entry.delete(0, tk.END)