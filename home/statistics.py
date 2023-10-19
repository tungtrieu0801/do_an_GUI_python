import tkinter as tk
from tkinter import ttk
def statistics(root):
    statistics_window = tk.Toplevel(root)
    statistics_window.title("statistics")
    statistics_window.geometry("1140x820")

    def close_window_2():
        statistics_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(statistics_window, text="Back", command=close_window_2)
    back_button.pack()

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    label = tk.Label(statistics_window, text="Đây là nơi báo cáo thống kê", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
    