import tkinter as tk
from tkinter import ttk
def warehouse(root):
    warehourse_window = tk.Toplevel(root)
    warehourse_window.title("warehourse")
        # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 1140  # Thay đổi kích thước theo nhu cầu
    window_height = 820  # Thay đổi kích thước theo nhu cầu
    # Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
    warehourse_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def close_window_2():
        warehourse_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(warehourse_window, text="Back", command=close_window_2)
    back_button.pack()

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    label = tk.Label(warehourse_window, text="Đây là kho hàng", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
     