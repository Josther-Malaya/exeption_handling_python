import tkinter as tk
from gui import CalculatorGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()