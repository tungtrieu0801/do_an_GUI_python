import tkinter as tk
from tkinter import ttk


def history(root):
    history_window = tk.Toplevel(root)
    history_window.title("history")
    history_window.geometry("1140x820")

    def close_window_2():
        history_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(history_window, text="Back", command=close_window_2)
    back_button.pack()

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    label = tk.Label(history_window, text="Đây là lịch sử bán hàng", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
    