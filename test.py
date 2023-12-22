import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ Tkinter
window = tk.Tk()
window.title("Thông tin đầu tư")

# Đặt kích thước chữ là 25
style = ttk.Style()
style.configure('TLabel', font=('Arial', 25), borderwidth=2, relief="solid", padding=(10, 10))

# Tính toán vị trí giữa màn hình
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - 1300) // 2
y_coordinate = (screen_height - 700) // 2

# Cấu hình vị trí của cửa sổ
window.geometry(f"1300x800+{x_coordinate}+{y_coordinate}")

label1 = ttk.Label(window, text="Vốn đầu tư")
label1.place(relx=0.36,rely=0.36) # Canh giữa theo chiều ngang

label2 = ttk.Label(window, text="Tổng thu")
label2.place(relx=0.56,rely=0.36) # Canh giữa theo chiều ngang

label3 = ttk.Label(window, text="123123")
label3.place(relx=0.36,rely=0.66)  # Canh giữa theo chiều ngang

label4 = ttk.Label(window, text="124123")
label4.place(relx=0.56,rely=0.66)  # Canh giữa theo chiều ngang

# Hiển thị cửa sổ
window.mainloop()
