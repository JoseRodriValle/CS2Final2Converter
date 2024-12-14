import tkinter as tk
from gui import ConverterGUI


def main():  # Main Window
    root = tk.Tk()
    app = ConverterGUI(master=root)
    app.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
