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
        self.bind_keys()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, font="Arial 20")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        buttons = [
            ["(", ")", "%", "//"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]

        for r, row in enumerate(buttons, start=1):
            for c, btn in enumerate(row):
                button = tk.Button(self.root, text=btn, font="Arial 15")
                button.grid(row=r, column=c, sticky="nsew")

                button.bind("<Button-1>", self.on_click)

        # Make grid expandable
        for i in range(6):  # rows
            self.root.grid_rowconfigure(i, weight=1)

        for i in range(4):  # columns
            self.root.grid_columnconfigure(i, weight=1)

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

    def bind_keys(self):
        self.root.bind("<BackSpace>", self.on_backspace)

    def on_backspace(self, event):
        current = self.entry.get()
        if current:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[:-1])