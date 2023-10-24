import tkinter as tk
import tkinter.ttk as ttk
def create_product_page(main_fm):
    product_page_fm = tk.Frame(main_fm)
    product_page_fm.pack(fill=tk.BOTH, expand=True)

    product_page_lb = tk.Label(product_page_fm, text="Product Page", fg="black")
    product_page_lb.grid(column=0,row=0,padx=30,pady=30)

    product_page_lb1 = tk.Label(product_page_fm, text="Product Page", fg="black")
    product_page_lb1.grid(column=1,row=0,padx=30,pady=30)

    product_page_lb2 = tk.Label(product_page_fm, text="Product Page", fg="black")
    product_page_lb2.grid(column=0,row=1,padx=30,pady=30)

    product_page_lb3 = tk.Label(product_page_fm, text="Product Page", fg="black")
    product_page_lb3.grid(column=1,row=1,padx=30,pady=30)

    product_page_lb4 = tk.Label(product_page_fm, text="Product Page", fg="black")
    product_page_lb4.grid(column=0,row=2,padx=30,pady=30)
    
def your_function():
    # Xử lý sự kiện khi nút được nhấn
    print("Button clicked")