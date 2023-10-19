import tkinter as tk
from tkinter import ttk

def addProduct(root):
    addProduct_window = tk.Toplevel(root)
    addProduct_window.title("addProduct")
    addProduct_window.geometry("1140x820")

    def close_window_2():
        addProduct_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(addProduct_window, text="Back", command=close_window_2)
    back_button.pack()

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    label = tk.Label(addProduct_window, text="Đây là nơi thêm hàng", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
    