import tkinter as tk
from tkinter import ttk
from styles import configure_styles

def home(root):
    #gọi hàm style căn chỉnh
    configure_styles()
    home_window = tk.Toplevel(root)
    home_window.title("Home")
    
    # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 1140  # Thay đổi kích thước theo nhu cầu
    window_height = 820  # Thay đổi kích thước theo nhu cầu
    # Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
    home_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    home_window.resizable(width=False, height=False)

    def close_window_2():
        home_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    frame_back = ttk.Frame(home_window)
    frame_back.place(x=20,y=20)
    back_button = ttk.Button(frame_back, text="Quay lại", command=close_window_2, style='Back_Bbutton.TButton')
    back_button.grid(column=0,row=0,padx=(0,400))

    label = ttk.Label(frame_back, text="Trang chủ", foreground="green",font=("Arial", 25,'bold'),)  # Đặt kích thước font là 16
    label.grid(row=0, column=1)
    

 