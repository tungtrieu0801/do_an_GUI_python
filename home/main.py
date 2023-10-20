import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import homepage
import addProduct
import contact
import sell
import deliver
import history
import setting
import statistics
import warehouse
file_path = os.path.dirname(os.path.realpath(__file__))

app = tk.Tk()
# Lấy kích thước của màn hình
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Lấy kích thước của cửa sổ
window_width = 1140  # Thay đổi kích thước theo nhu cầu
window_height = 820  # Thay đổi kích thước theo nhu cầu

# Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Đặt vị trí cửa sổ
app.geometry(f"{window_width}x{window_height}+{x}+{y}")
app.title("Ứng dụng Tkinter")

frame = ttk.Frame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)
style = ttk.Style()

# Tùy chỉnh nút sử dụng Style
style.configure("TButton",
                foreground="green",  # Màu chữ
                font=("Arial", 12),  # Phông chữ và kích thước
                padding=(20, 50),     # Khoảng cách giữa nội dung và biên (thay đổi giá trị đầu tiên để điều chỉnh chiều rộng, thay đổi giá trị thứ hai để điều chỉnh chiều cao)
                width=10,             # Chiều rộng của nút (tăng giá trị ở đây)
                borderwidth=10,       # Độ dày viền
                relief="flat",       # Kiểu viền
                )
def open_new_window_from_main():
    app.withdraw()
    homepage.home(app)

def open_addProduct():
    app.withdraw()
    addProduct.addProduct(app)

def open_contact():
    app.withdraw()
    contact.contact(app)

def open_deliver():
    app.withdraw()
    deliver.deliver(app)

def open_history():
    app.withdraw()
    history.history(app)

def open_sell():
    app.withdraw()
    sell.sell(app)

def open_setting():
    app.withdraw()
    setting.setting(app)

def open_statistics():
    app.withdraw()
    statistics.statistics(app)
    
def open_warehouse():
    app.withdraw()
    warehouse.warehouse(app)

# Hàm để load và co nhỏ ảnh
def load_and_resize_image(image_path, width, height):
    image = Image.open(image_path)
    image.thumbnail((width, height))
    return ImageTk.PhotoImage(image)

image_home = load_and_resize_image(file_path + "/images/house.png", 65, 65)
button = ttk.Button(frame, image=image_home, text="Trang chủ   ",
                    compound='right', command=open_new_window_from_main, style="TButton")
button.grid(row=0, column=0, pady=40, padx=40)

image_sell = load_and_resize_image(file_path + "/images/selling.png", 65, 65)
button = ttk.Button(frame, image=image_sell, text="Bán hàng   ",
                    compound='right', style="TButton", command=open_sell)
button.grid(row=0, column=1, pady=40, padx=30)

image_statistics = load_and_resize_image(file_path + "/images/statistics.png", 65, 65)
button = ttk.Button(frame, image=image_statistics, text="Thống kê   ",
                    compound='right', style="TButton",command=open_statistics)
button.grid(row=0, column=2, pady=40, padx=30,)

image_warehouse = load_and_resize_image(file_path + "/images/warehouse.png", 65, 65)
button = ttk.Button(frame, image=image_warehouse, text="Kho hàng   ",
                    compound='right', style="TButton",command=open_warehouse)
button.grid(row=1, column=0, pady=40, padx=30)

image_history = load_and_resize_image(file_path + "/images/time-management.png", 65, 65)
button = ttk.Button(frame, image=image_history, text="Lịch sử     ",
                    compound='right', style="TButton",command=open_history)
button.grid(row=1, column=1, pady=40, padx=30)

image_shipped = load_and_resize_image(file_path + "/images/shipped.png", 65, 65)
button = ttk.Button(frame, image=image_shipped, text="Giao hàng",
                    compound='right', style="TButton",command=open_deliver)
button.grid(row=1, column=2, pady=40, padx=30)

image_forklift = load_and_resize_image(file_path + "/images/forklift.png", 65, 65)
button = ttk.Button(frame, image=image_forklift, text="Nhập hàng  ",
                    compound='right', style="TButton",command=open_addProduct)
button.grid(row=2, column=0, pady=40, padx=30)

image_gear = load_and_resize_image(file_path + "/images/gear.png", 65, 65)
button = ttk.Button(frame, image=image_gear, text="Cài đặt     ",
                    compound='right', style="TButton",command=open_setting)
button.grid(row=2, column=1, pady=40, padx=30)

image_contact = load_and_resize_image(file_path + "/images/contact.png", 65, 65)
button = ttk.Button(frame, image=image_contact, text="Báo lỗi     ",
                    compound='right', style="TButton",command=open_contact)
button.grid(row=2, column=2, pady=40, padx=30)

style = ttk.Style()
style.configure("TButton", font=("Arial", 25, "bold"), borderwidth=2, foreground="green")

app.mainloop()
if __name__ == "__main__":
    app.mainloop()