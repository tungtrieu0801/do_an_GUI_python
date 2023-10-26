import tkinter as tk
from tkinter import ttk
import mysql.connector
from styles import configure_styles
def warehouse(root):
    #gọi hàm style căn chỉnh
    configure_styles()
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
    warehourse_window.resizable(width=False, height=False)

    def add_product():
        product_name = name_entry.get()
        product_type = type_entry.get()
        product_stock = stock_entry.get()
        product_price = price_entry.get()
        

        cursor.execute("INSERT INTO products (name, type, stock, price) VALUES (%s, %s, %s, %s)", (product_name, product_type, product_stock, product_price))
        connection.commit()
        
        # Hiển thị sản phẩm mới trong Treeview
        treeview.insert('', 'end', values=(product_name, product_type, product_stock, product_price))

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



    show_warehouse_frame = ttk.Frame(warehourse_window)
    show_warehouse_frame.place(x=40,y=100)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Helvetica", 10))
    style.configure("TButton", font=("Helvetica", 10))
    style.configure("TLabel", font=("Helvetica", 10))
    style.configure("TEntry", font=("Helvetica", 40))
    style.configure("Custom.Treeview.Row", font=("Helvetica", 12), height=70)
    # Tạo Treeview để hiển thị danh sách hàng hoá

    treeview = ttk.Treeview(show_warehouse_frame, columns=("Name", "Type", "Stock", "Price"), show="headings", style="Custom.Treeview")
    treeview.heading("Name", text="Tên sản phẩm")
    treeview.heading("Type", text="Loại sản phẩm")
    treeview.heading("Stock", text="Số lượng")
    treeview.heading("Price", text="Giá tiền")
    
    # Đặt kích thước của Treeview dọc theo chiều dài
    treeview['height'] = 10  # Thay đổi giá trị này để điều chỉnh số dòng hiển thị
    style.configure('Treeview', rowheight=40)
    # Đặt kiểu trình bày cho từng cột với anchor giữa (center)
    treeview.column("Name", width=300, anchor="center", stretch=tk.NO)
    treeview.column("Type", width=300, anchor="center", stretch=tk.NO)
    treeview.column("Stock", width=200, anchor="center", stretch=tk.NO)
    treeview.column("Price", width=200, anchor="center", stretch=tk.NO)


    # # Đặt kiểu trình bày cho từng dòng
    # style.layout("Treeview.Item", [('Treeitem.padding',
    #             {'sticky': 'nswe',
    #             'children': [('Treeitem.indicator', {'side': 'left', 'sticky': ''}),
    #                             ('Treeitem.image', {'side': 'left', 'sticky': ''}),
    #                             ('Treeitem.text', {'side': 'left', 'sticky': 'w'})]})])

    # Đặt Treeview để hiển thị nội dung ở vị trí căn giữa
    treeview.pack(anchor="center")
    
    # Tạo thanh cuộn để di chuyển trong trường hợp nội dung quá dài
    scrollbar = ttk.Scrollbar(warehourse_window, orient='vertical', command=treeview.yview)
    scrollbar.pack(side='right', fill='y')
    treeview.configure(yscrollcommand=scrollbar.set)

    # Tạo các label và entry để nhập thông tin sản phẩm
    frame_button = ttk.Frame(warehourse_window)
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

    # Truy vấn dữ liệu từ cơ sở dữ liệu và hiển thị lên Treeview

    cursor.execute("SELECT name, type, stock, price FROM products")
    products = cursor.fetchall()
    for product in products:
        treeview.insert('', 'end', values=product)

    # Đặt kiểu trình bày tùy chỉnh cho Treeview để đặt cỡ chữ
    style.configure("Treeview")























    def close_window_2():
        warehourse_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    frame_back = ttk.Frame(warehourse_window)
    frame_back.place(x=20,y=20)
    back_button = ttk.Button(frame_back, text="Quay lại", command=close_window_2, style='Back_Bbutton.TButton')
    back_button.grid(column=0,row=0,padx=(0,250))
    
    # Thêm nội dung vào cửa sổ mới và đảm bảo nó nằm ở giữa
    
    label = tk.Label(frame_back, text="Kho hàng", foreground="green",font=("Arial", 25,'bold'),)  # Đặt kích thước font là 16
    label.grid(column=1, row=0)