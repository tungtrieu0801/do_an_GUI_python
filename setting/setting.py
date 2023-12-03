import tkinter as tk
from tkinter import ttk
from styles import configure_styles
def setting(root):
    #gọi hàm style căn chỉnh
    configure_styles()
    setting_window = tk.Toplevel(root)
    setting_window.title("setting")
        # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 1140  # Thay đổi kích thước theo nhu cầu
    window_height = 820  # Thay đổi kích thước theo nhu cầu
    # Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
    setting_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    setting_window.resizable(width=False, height=False)

    def close_window_2():
        setting_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    frame_back = ttk.Frame(setting_window)
    frame_back.place(x=20,y=20)
    back_button = ttk.Button(frame_back, text="Quay lại", command=close_window_2, style='Back_Bbutton.TButton')
    back_button.grid(column=0,row=0,padx=(0,400))
    
    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    
    label = tk.Label(frame_back, text="Cài đặt ", foreground="green",font=("Arial", 25,'bold'),)  # Đặt kích thước font là 16
    label.grid(column=1, row=0)