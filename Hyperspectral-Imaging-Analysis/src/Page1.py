import tkinter as tk
from tkinter import ttk
import sv_ttk
from StartPoint import MoveLeftOne, MoveLeftFive, MoveRightOne, MoveRightFive
from Scanning import start_scan
from Example.Run_example  import load_dispaly_Cube, Display_RGB 
class MovementControl(ttk.LabelFrame):
    def __init__(self, parent, title, move_one, move_five):
        super().__init__(parent, text=title, padding=15)
        self.add_widgets(move_one, move_five)

    def add_widgets(self, move_one, move_five):
        ttk.Button(self, text="1 mm", command=move_one).grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        ttk.Button(self, text="5 mm", command=move_five).grid(row=1, column=0, sticky="ew", padx=10, pady=5)


        
class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=15)
        self.setup_layout()

    def setup_layout(self):
        self.grid(sticky="nsew")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        MovementControl(self, "Move Left", MoveLeftOne, MoveLeftFive).grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        MovementControl(self, "Move Right", MoveRightOne, MoveRightFive).grid(row=0, column=1, sticky="nsew", padx=(0, 10))

        ttk.Button(self, text="Start Scanning", command=self.start_scanning).grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=10)
        ttk.Button(self, text="Display Cube", command=lambda: load_dispaly_Cube("C:\\Users\\suraf\\New folder (2)\\Hyperspectral-Imaging-Analysis\\src\\Example\\92AV3C (2).lan")).grid(row=2, column=1, columnspan=3, sticky="ew", padx=20, pady=10)
        ttk.Button(self, text="Display RGB ", command=lambda: Display_RGB()).grid(row=3, column=2, columnspan=4, sticky="ew", padx=20, pady=10)


    def start_scanning():
        print("starting scan....")
    
    def Display_Cube():
        print("displaying cube...")

def main():
    root = tk.Tk()
    root.title("Hyperspectral Imaging Device")
    root.geometry("800x400")
    sv_ttk.set_theme("dark")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    app = App(root)
    app.pack(expand=True, fill='both')

    root.mainloop()

if __name__ == "__main__":
    main()
