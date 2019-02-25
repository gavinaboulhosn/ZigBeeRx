import tkinter as tk
from ZigBeeRx.ports import serial_ports
from tkinter import ttk
from tkinter import messagebox
import threading


class PortSelectGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")
        self.root.title("Serial Select")
        self.port_choices = serial_ports()
        self.port_var = tk.StringVar(self.root)
        self.port = None
        self.save_var = tk.IntVar()


    def display(self):
        try:
            self.port_var.set(self.port_choices[0])
            drop_menu = ttk.OptionMenu(self.root, self.port_var, *self.port_choices)
            drop_menu.pack()
            button = ttk.Button(self.root, text="Select Port", command=self.choose_port)
            button.pack()
            save_box = ttk.Checkbutton(self.root, text="Save selected port?", variable=self.save_var)
            save_box.pack(side=tk.LEFT)
            self.root.mainloop()

        except IndexError:
            messagebox.showerror("No serial connections discovered!",
                                 message="Please check USB connection and try again.")
            self.root.mainloop()
            self.root.quit()

    def choose_port(self):
        self.port = self.port_var.get()
        self.root.destroy()
        if self.save_var:
            self.save_port()
            print('here')

    def thread_close(self):
        self.thread = threading.Thread(target=self.choose_port())
        self.thread.start()
        return

    def save_port(self):
        import os
        with open(os.path.join(os.pardir, "port.ini"), "w") as file:
            file.write(self.port)
