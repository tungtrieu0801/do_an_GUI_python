import tkinter as tk
from tkinter import ttk
from styles import style_for_text
def create_home_page(main_fm):
    style_for_text()
    home_page_fm = ttk.Frame(main_fm)
    # home_page_fm.grid(row=0,column=0,padx=5,pady=5)
    # home_page_fm.place(x=400,y=400)
    home_page_fm.place(x=0, y=0, relwidth=1, relheight=1)  

    home_page_lb = ttk.Label(home_page_fm, text="Cuối cùng cũng fix xong dm mất hết buổi tối")
    # home_page_lb.grid(row=0,column=0,padx=5,pady=5)
    # home_page_lb.place(x=450,y=450)
    home_page_lb.place(relx=0.5, rely=0.5, anchor="center")  
 

