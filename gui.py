import tkinter as tk
from tkinter import ttk
from converter import CurrencyConverter


class ConverterGUI(tk.Frame):

    # GUI class for Converter.

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.converter = CurrencyConverter()
        self.master.title("Currency Converter")
        self.master.geometry("350x300")  # Adjusted the size of the window

        # List of available currencies (this should be updated as per your requirements)
        self.available_currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD"]

        # Input Currency Dropdown
        self.input_currency_label = tk.Label(self.master, text="Input Currency:")
        self.input_currency_label.pack()
        self.input_currency = ttk.Combobox(self.master, values=self.available_currencies)
        self.input_currency.pack()

        # Output Currency Dropdown
        self.output_currency_label = tk.Label(self.master, text="Output Currency:")
        self.output_currency_label.pack()
        self.output_currency = ttk.Combobox(self.master, values=self.available_currencies)
        self.output_currency.pack()

        # Input Amount with Error Checking
        self.amount_label = tk.Label(self.master, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack()

        # Convert Button
        self.convert_button = tk.Button(self.master, text="Convert", command=self.convert)
        self.convert_button.pack()

        # Read-Only Output Value Box
        self.output_label = tk.Label(self.master, text="Converted Amount:")
        self.output_label.pack()
        self.output_value = tk.Entry(self.master, state='readonly')
        self.output_value.pack()

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            input_currency = self.input_currency.get()
            output_currency = self.output_currency.get()
            print(f"Converting {amount} from {input_currency} to {output_currency}")  # Debug print

            converted_amount = self.converter.convert(amount, input_currency, output_currency)
            print(f"Converted amount: {converted_amount}")  # Debug print

            self.output_value.config(state='normal')
            self.output_value.delete(0, tk.END)
            self.output_value.insert(0, str(converted_amount))
            self.output_value.config(state='readonly')
        except ValueError:
            print("Invalid input")  # Debug print
            self.output_value.config(state='normal')
            self.output_value.delete(0, tk.END)
            self.output_value.insert(0, "Invalid input")
            self.output_value.config(state='readonly')


# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterGUI(master=root)
    app.mainloop()
