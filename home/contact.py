import tkinter as tk
from tkinter import ttk


def contact(root):
    contact_window = tk.Toplevel(root)
    contact_window.title("contact")
    contact_window.geometry("1140x820")

    def close_window_2():
        contact_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(contact_window, text="Back", command=close_window_2)
    back_button.pack()

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    label = tk.Label(contact_window, text="Đây là nơi liên hệ", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
    