import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
file_path = os.path.dirname(os.path.realpath(__file__))
from styles import *
def contact(root):
    #gọi hàm style căn chỉnh
    configure_styles()
    style_for_text()
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
    contact_window.resizable(width=False, height=False)
    def close_window_2():
        contact_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    

    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    frame_back = ttk.Frame(contact_window)
    frame_back.place(x=20,y=20)
    back_button = ttk.Button(frame_back, text="Quay lại", command=close_window_2, style='Back_Bbutton.TButton')
    back_button.pack(padx=(30,0))

    
    label = tk.Label(contact_window, text="Liên hệ với chúng tôi", foreground="green",font=("Arial", 25,'bold'),)  # Đặt kích thước font là 16
    label.place(x=350, y=100)

    frame_information = ttk.Frame(contact_window)
    frame_information.place(x=350, y=160, width=730, height=300)

    # Tạo một ttk.Style và cấu hình nó
    style = ttk.Style()
    style.configure("Custom.TFrame", background="#c8c3d9")  # Thay đổi màu nền ở đây

    # Sử dụng style đã cấu hình cho frame
    frame_information["style"] = "Custom.TFrame"


    # Tạo một ttk.Style và cấu hình nó
    style = ttk.Style()
    style.configure("White.TLabel", foreground="white")  # Thay đổi màu chữ thành màu trắng

    # Sử dụng style đã cấu hình cho label
    # label["style"] = "White.TLabel"
    def load_and_resize_image(image_path, width, height):
        image = Image.open(image_path)
        image.thumbnail((width, height))
        return ImageTk.PhotoImage(image)

    district = ttk.Label(frame_information, text="Địa chỉ: 108 Phố Nguyên Xá, Minh Khai, Bắc Từ Liêm, Hà Nội", style='Text.TButton')
    district.grid(row=0, column=0,padx=20,pady=(30, 0))

    phone_number =  ttk.Label(frame_information, text="Số điện thoại: 0987654321", style='Text.TButton')
    phone_number.grid(row=1, column=0)

    gmail = ttk.Label(frame_information, text="Gmail: trieutungvp@gmail.com", style='Text.TButton')
    gmail.grid(row=2, column=0) 

    location_image = load_and_resize_image(file_path + "/images/location.png", 70, 70)  # Đặt kích thước 70x70
    image_label = tk.Label(frame_information, image=location_image) 
    #do image nằm đơn lẻ k phụ thuộc vào gì cả, nên phải lưu vào 1 biến để duy trì ngăn bị thu hồi bởi  garbage collector
    #còn trong file main là do ảnh nằm trong button, nên khi render button nó sẽ render lại cả ảnh.
    image_label.image = location_image
    image_label.grid(row=0, column=1, rowspan=3, padx=(10, 0),pady=(40, 0))
    