import tkinter as tk

def create_contact_page(main_fm):
    contact_page_fm = tk.Frame(main_fm)
    contact_page_lb = tk.Label(contact_page_fm, text="Contact Page", fg="black")
    contact_page_lb.pack(pady=80)
    contact_page_fm.pack(fill=tk.BOTH, expand=True)
