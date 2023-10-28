import tkinter as tk
from tkinter import ttk
from styles import *
import mysql.connector
def addProduct(root):
    #gọi hàm style căn chỉnh
    configure_styles()
    addProduct_window = tk.Toplevel(root)
    addProduct_window.title("addProduct")
        # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1140  # Thay đổi kích thước theo nhu cầu
    window_height = 820  # Thay đổi kích thước theo nhu cầu
    # Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
    addProduct_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    addProduct_window.resizable(width=False, height=False)
    def close_window_2():
        addProduct_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    frame_back = ttk.Frame(addProduct_window)
    frame_back.place(x=20,y=20)
    back_button = ttk.Button(frame_back, text="Quay lại", command=close_window_2, style='Back_Bbutton.TButton')
    back_button.grid(column=0, row=0,padx=(0,250))
    
    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    def add_product():
        product_name = name_entry.get()
        product_type = type_entry.get()
        product_stock = stock_entry.get()
        product_price = price_entry.get()
        

        cursor.execute("INSERT INTO products (name, type, stock, price) VALUES (%s, %s, %s, %s)", (product_name, product_type, product_stock, product_price))
        connection.commit()
        
        # Hiển thị sản phẩm mới trong Treeview
    

        # Xóa nội dung đã nhập
        name_entry.delete(0, tk.END)
        type_entry.delete(0, tk.END)
        stock_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    # Kết nối với cơ sở dữ liệu MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='080102',
        database='mydb'
    )
    cursor = connection.cursor()
    
        # Tạo các label và entry để nhập thông tin sản phẩm
    frame_button = ttk.Frame(addProduct_window)
    frame_button.place(x=100, y=600)
    name_label = ttk.Label(frame_button, text="Tên sản phẩm")
    name_label.pack()
    name_entry = ttk.Entry(frame_button)
    name_entry.pack()


    type_label = ttk.Label(frame_button, text="Loại sản phẩm")
    type_label.pack()
    type_entry = ttk.Entry(frame_button)
    type_entry.pack()


    stock_label = ttk.Label(frame_button, text="Số lượng")
    stock_label.pack()
    stock_entry = ttk.Entry(frame_button)
    stock_entry.pack()

    price_label = ttk.Label(frame_button, text="Giá tiền")
    price_label.pack()
    price_entry = ttk.Entry(frame_button)
    price_entry.pack()

    # Tạo nút để thêm sản phẩm
    add_button = ttk.Button(frame_button, text="Thêm sản phẩm", command=add_product)
    add_button.pack()