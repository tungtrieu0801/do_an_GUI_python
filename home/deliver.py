import tkinter as tk
from tkinter import ttk


def deliver(root):
    deliver_window = tk.Toplevel(root)
    deliver_window.title("deliver")
    deliver_window.geometry("1140x820")

    def close_window_2():
        deliver_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(deliver_window, text="Back", command=close_window_2)
    back_button.pack()

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    label = tk.Label(deliver_window, text="Đây là nơi theo dõi vận chuyển", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
    