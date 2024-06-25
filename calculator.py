import tkinter as tk
from math import sin, cos, tan, log, log10, sqrt, pi, e, exp

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        
        self.display = tk.Entry(self, width=28, font=("Arial", 24), borderwidth=5, relief="sunken", bg="#e6e6e6")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        buttons = [
            ('C', 1, 0, 'clear', 1, "#ff6666"), ('MR', 1, 1, 'memory_recall', 1, "#ffcc66"), ('MC', 1, 2, 'memory_clear', 1, "#ffcc66"), ('M+', 1, 3, 'memory_add', 1, "#ffcc66"), ('M-', 1, 4, 'memory_subtract', 1, "#ffcc66"),
            ('(', 2, 0, None, 1, "#cce6ff"), (')', 2, 1, None, 1, "#cce6ff"), ('^', 2, 2, None, 1, "#cce6ff"), ('/', 2, 3, None, 1, "#cce6ff"), ('*', 2, 4, None, 1, "#cce6ff"),
            ('7', 3, 0, None, 1, "#ffffff"), ('8', 3, 1, None, 1, "#ffffff"), ('9', 3, 2, None, 1, "#ffffff"), ('-', 3, 3, None, 1, "#cce6ff"), ('+', 3, 4, None, 1, "#cce6ff"),
            ('4', 4, 0, None, 1, "#ffffff"), ('5', 4, 1, None, 1, "#ffffff"), ('6', 4, 2, None, 1, "#ffffff"), ('=', 4, 3, 'calculate', 2, "#66ff66"),
            ('1', 5, 0, None, 1, "#ffffff"), ('2', 5, 1, None, 1, "#ffffff"), ('3', 5, 2, None, 1, "#ffffff"), ('0', 5, 3, None, 2, "#ffffff"), ('.', 5, 4, None, 1, "#ffffff"),
            ('sin', 6, 0, None, 1, "#cce6ff"), ('cos', 6, 1, None, 1, "#cce6ff"), ('tan', 6, 2, None, 1, "#cce6ff"), ('log', 6, 3, None, 1, "#cce6ff"), ('ln', 6, 4, None, 1, "#cce6ff"),
            ('√', 7, 0, None, 1, "#cce6ff"), ('π', 7, 1, None, 1, "#cce6ff"), ('e', 7, 2, None, 1, "#cce6ff"), ('c', 7, 3, None, 1, "#cce6ff"), ('h', 7, 4, None, 1, "#cce6ff"),
            ('G', 8, 0, None, 1, "#cce6ff"), ('e', 8, 1, None, 1, "#cce6ff"), ('N_A', 8, 2, None, 1, "#cce6ff"), ('k', 8, 3, None, 1, "#cce6ff"), ('R', 8, 4, None, 1, "#cce6ff"),
            ('F', 9, 0, None, 1, "#cce6ff"), ('σ', 9, 1, None, 1, "#cce6ff"), ('ε₀', 9, 2, None, 1, "#cce6ff")
        ]

        self.memory = 0

        for button in buttons:
            text, row, col, cmd, colspan, color = button if len(button) == 6 else button + (1, "#ffffff")
            if cmd is None:
                cmd = lambda x=text: self.append_to_display(x)
            else:
                cmd = getattr(self, cmd)
            tk.Button(self, text=text, width=5, height=2, command=cmd, font=("Arial", 14), bg=color).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

        # Configure row and column weights
        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.grid_columnconfigure(j, weight=1)
    
    def clear(self):
        self.display.delete(0, tk.END)

    def append_to_display(self, text):
        self.display.insert(tk.END, text)

    def calculate(self):
        expression = self.display.get()
        try:
            expression = expression.replace('√', 'sqrt').replace('π', 'pi').replace('e', 'exp(1)').replace('^', '**').replace('ln', 'log').replace('log', 'log10')
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def memory_recall(self):
        self.display.insert(tk.END, str(self.memory))

    def memory_clear(self):
        self.memory = 0

    def memory_add(self):
        try:
            self.memory += eval(self.display.get())
        except:
            pass

    def memory_subtract(self):
        try:
            self.memory -= eval(self.display.get())
        except:
            pass

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
