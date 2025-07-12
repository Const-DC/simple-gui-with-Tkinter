import tkinter as tk
from tkinter import messagebox



class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Close", command = exit)
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="your message" , font=("Arial", 24))
        self.label.pack(padx = 10 , pady = 10)

        self.textbox = tk.Text(self.root , height = 10, font=("Roboto", 14))
        self.textbox.bind("<KeyPress>", self.status_key)
        self.textbox.pack()

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root , text = "Check Messages" , font=("Roboto", 14), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="show message", font=("roboto", 14), command=self.show_message)

        self.button.pack(padx=10, pady=10)


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else :
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))

    def status_key(self, event):
        if event.keysym == "Return" and event.state == 20:
            print("Hello, World!")

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


MyGUI()