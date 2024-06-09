import tkinter as tk
from tkinter import messagebox

class CoffeeMachine:
    def __init__(self):
        self.prices = {
            'espresso': 3.0,
            'latte': 4.0,
            'cappuccino': 4.5
        }

    def generate_receipt(self, orders):
        total = sum(self.prices[coffee_type] * quantity for coffee_type, quantity in orders.items())
        receipt = "Receipt\n"
        receipt += "-" * 20 + "\n"
        for coffee_type, quantity in orders.items():
            receipt += f"{quantity}x {coffee_type.capitalize()}: ${self.prices[coffee_type] * quantity:.2f}\n"
        receipt += "-" * 20 + "\n"
        receipt += f"Total: ${total:.2f}\n"
        return receipt

class CoffeeMachineGUI:
    def __init__(self, root, machine):
        self.machine = machine
        self.root = root
        self.root.title("Coffee Maker")
        self.orders = {}
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to the Coffee Maker", font=('Helvetica', 16))
        self.title_label.pack(pady=10)

        self.coffee_type_label = tk.Label(self.root, text="Select Coffee Type:")
        self.coffee_type_label.pack(pady=5)

        self.coffee_type_var = tk.StringVar(value='espresso')
        self.coffee_type_menu = tk.OptionMenu(self.root, self.coffee_type_var, 'espresso', 'latte', 'cappuccino')
        self.coffee_type_menu.pack(pady=5)

        self.quantity_label = tk.Label(self.root, text="Enter Quantity:")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack(pady=5)

        self.add_order_button = tk.Button(self.root, text="Add Order", command=self.add_order)
        self.add_order_button.pack(pady=10)

        self.orders_text = tk.Text(self.root, height=10, width=50)
        self.orders_text.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit Order", command=self.submit_order)
        self.submit_button.pack(pady=10)

    def add_order(self):
        coffee_type = self.coffee_type_var.get().strip().lower()
        try:
            quantity = int(self.quantity_entry.get().strip())
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")
            if coffee_type in self.machine.prices:
                self.orders[coffee_type] = self.orders.get(coffee_type, 0) + quantity
                self.orders_text.insert(tk.END, f"Added {quantity}x {coffee_type}\n")
                self.quantity_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Invalid Coffee Type", "Please enter a valid coffee type.")
        except ValueError as e:
            messagebox.showerror("Invalid Quantity", str(e))

    def submit_order(self):
        try:
            receipt = self.machine.generate_receipt(self.orders)
            messagebox.showinfo("Receipt", receipt)
            self.orders = {}
            self.orders_text.delete(1.0, tk.END)
            self.coffee_type_var.set('espresso')
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    machine = CoffeeMachine()
    app = CoffeeMachineGUI(root, machine)
    root.mainloop()
