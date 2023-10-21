import tkinter as tk
from tkinter import ttk


def contact(root):
    style = ttk.Style()
    style.configure("Bbutton.TButton",
                foreground="green",   # Màu chữ
                font=("Arial", 12),    # Phông chữ và kích thước
                padding=(10, 10),      # Khoảng cách giữa nội dung và biên (điều chỉnh chiều rộng và chiều cao ở đây)
                width=8,               # Chiều rộng của nút (giảm giá trị ở đây)
                borderwidth=5,         # Độ dày viền
                relief="flat"          # Kiểu viền
                )

    contact_window = tk.Toplevel(root)
    contact_window.title("contact")
        # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 1440  # Thay đổi kích thước theo nhu cầu
    window_height = 850  # Thay đổi kích thước theo nhu cầu
    # Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
    contact_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def close_window_2():
        contact_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    frame_back = ttk.Frame(contact_window)
    frame_back.place(x=20,y=20)
    
    back_button = ttk.Button(frame_back, text="Quay lại", command=close_window_2, style='Bbutton.TButton')
    back_button.pack()

    
    label = tk.Label(contact_window, text="Liên hệ với chúng tôi", font=("Arial", 26))  # Đặt kích thước font là 16
    label.place(x=350, y=100)

    frame_information = ttk.Frame(contact_window)
    frame_information.place(x=350, y=160, width=730, height=300)

    # Tạo một ttk.Style và cấu hình nó
    style = ttk.Style()
    style.configure("Custom.TFrame", background="green")  # Thay đổi màu nền ở đây

    # Sử dụng style đã cấu hình cho frame
    frame_information["style"] = "Custom.TFrame"
    label = ttk.Label(frame_information, text="Thông tin", font=("Arial", 26), background='green')

    # Tạo một ttk.Style và cấu hình nó
    style = ttk.Style()
    style.configure("White.TLabel", foreground="white")  # Thay đổi màu chữ thành màu trắng

    # Sử dụng style đã cấu hình cho label
    label["style"] = "White.TLabel"
    label.pack()

    