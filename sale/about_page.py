import tkinter as tk

def create_about_page(main_fm):
    about_page_fm = tk.Frame(main_fm)
    about_page_lb = tk.Label(about_page_fm, text="About Page", fg="black")
    about_page_lb.pack(pady=80)
    about_page_fm.pack(fill=tk.BOTH, expand=True)
