import tkinter as tk
from tkinter import ttk
import sv_ttk
from Page1 import App as ControlApp

def show_control_page():
    global control_page
    welcome_frame.pack_forget()  # Remove the welcome page
    control_page = ControlApp(root)  
    control_page.pack(fill='both', expand=True)

root = tk.Tk()
root.title("Hyperspectral Imaging Device")  
root.geometry("700x700")
sv_ttk.set_theme("dark")

welcome_frame = ttk.Frame(root)
welcome_frame.pack(expand=True, fill=tk.BOTH)
welcome_frame.columnconfigure(0, weight=1)

for i in range(1, 6):
    welcome_frame.rowconfigure(i, weight=1)

ttk.Label(welcome_frame, text="Welcome To Our Project!", font=("Arial", 16, "bold"), anchor='center').grid(row=1, column=0, sticky=tk.NSEW)
ttk.Label(welcome_frame, text="Hyperspectral Imaging Camera (HIC)", font=("Arial", 14), anchor='center').grid(row=2, column=0, sticky=tk.NSEW)
ttk.Label(welcome_frame, text="Click 'Start' to begin your journey.", font=("Arial", 10), justify="center", anchor='center', wraplength=500).grid(row=3, column=0, sticky=tk.NSEW)
ttk.Button(welcome_frame, text="Start", command=show_control_page).grid(row=4, column=0, sticky=tk.EW)

welcome_frame.rowconfigure(0, weight=2)
welcome_frame.rowconfigure(5, weight=2)

root.mainloop()