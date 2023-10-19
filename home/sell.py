import tkinter as tk
from tkinter import ttk


def sell(root):
    sell_window = tk.Toplevel(root)
    sell_window.title("sell")
    sell_window.geometry("1140x820")

    def close_window_2():
        sell_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(sell_window, text="Back", command=close_window_2)
    back_button.pack()

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    label = tk.Label(sell_window, text="Đây là nơi bán hàng", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
    