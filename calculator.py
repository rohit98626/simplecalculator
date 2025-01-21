from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):
        master.title("Enhanced Calculator")
        master.geometry('400x600')  # Increased height to fit all buttons
        master.config(bg='lightgrey')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        self.memory = 0  # For memory storage

        # Display
        Entry(
            master, width=16, bg='white', font=('Arial Bold', 28),
            textvariable=self.equation, bd=5, relief='sunken', justify='right'
        ).grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Buttons
        buttons = [
            ['C', 'M+', 'MR', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '('],
            [')', '%', 'x²', '√']
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                Button(
                    master, text=btn_text, width=9, height=3, font=('Arial', 16),
                    bg='yellow', relief='raised',
                    command=lambda text=btn_text: self.button_action(text)
                ).grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

        # Adjust row weights for even distribution
        for i in range(len(buttons) + 1):  # +1 to include the display row
            master.grid_rowconfigure(i, weight=1)

        # Adjust column weights for even button spacing
        for i in range(4):  # 4 columns in total
            master.grid_columnconfigure(i, weight=1)

    def button_action(self, btn_text):
        """Handle button actions."""
        if btn_text == 'C':
            self.clear()
        elif btn_text == '=':
            self.solve()
        elif btn_text == 'M+':
            self.memory_add()
        elif btn_text == 'MR':
            self.memory_recall()
        elif btn_text == 'x²':
            self.square()
        elif btn_text == '√':
            self.square_root()
        else:
            self.show(btn_text)

    def show(self, value):
        """Display input on the screen."""
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        """Clear the display."""
        self.entry_value = ''
        self.equation.set('')

    def solve(self):
        """Evaluate the expression."""
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")

    def memory_add(self):
        """Add current result to memory."""
        try:
            self.memory = eval(self.entry_value)
        except:
            self.equation.set("Error")

    def memory_recall(self):
        """Recall the memory value."""
        self.entry_value += str(self.memory)
        self.equation.set(self.entry_value)

    def square(self):
        """Square the current input."""
        try:
            result = eval(self.entry_value) ** 2
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")

    def square_root(self):
        """Square root of the current input."""
        try:
            result = eval(self.entry_value) ** 0.5
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")


# Run the application
root = Tk()
calculator = Calculator(root)
root.mainloop()
