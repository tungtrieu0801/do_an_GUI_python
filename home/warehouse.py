import tkinter as tk
from tkinter import ttk
def warehouse(root):
    warehourse_window = tk.Toplevel(root)
    warehourse_window.title("warehourse")
    warehourse_window.geometry("1140x820")

    def close_window_2():
        warehourse_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(warehourse_window, text="Back", command=close_window_2)
    back_button.pack()

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    label = tk.Label(warehourse_window, text="Đây là kho hàng", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
     