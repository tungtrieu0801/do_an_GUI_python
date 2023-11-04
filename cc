import tkinter as tk
from tkinter import ttk
import mysql.connector

def load_data():
    # Kết nối cơ sở dữ liệu MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='PHW#84#jeor',
        database='amitdb'
    )

    # Tạo con trỏ để thao tác với cơ sở dữ liệu
    cursor = connection.cursor()

    # Truy vấn để lấy dữ liệu từ bảng "products"
    query = "SELECT * FROM products"

    # Thực thi truy vấn
    cursor.execute(query)

    # Xóa tất cả các dòng trong treeview1 trước khi cập nhật dữ liệu mới
    treeview1.delete(*treeview1.get_children())

    # Lặp qua kết quả truy vấn và cập nhật dữ liệu vào treeview1
    for row in cursor:
        product_name = row[0]
        product_type = row[1]
        quantity = row[2]
        unit_price = row[3]

        treeview1.insert("", "end", text=product_name, values=(product_type, quantity, unit_price))

    # Đóng con trỏ và kết nối cơ sở dữ liệu
    cursor.close()
    connection.close()

def copy_selected_item(event):
    selected_items = treeview1.selection()
    for item in selected_items:
        values = treeview1.item(item, "values")
        product_name = treeview1.item(item, "text")

        # Kiểm tra xem sản phẩm đã tồn tại trong treeview2 chưa
        existing_items = treeview2.get_children()
        for existing_item in existing_items:
            existing_values = treeview2.item(existing_item, "values")
            existing_product_name = treeview2.item(existing_item, "text")
            existing_product_type = existing_values[0]

            if existing_product_name == product_name and existing_product_type == values[0]:
                # Sản phẩm đã tồn tại và type giống nhau, update số lượng gấp đôi
                updated_quantity = int(existing_values[1]) +  int(values[1])
                treeview2.item(existing_item, values=(existing_values[0], updated_quantity, existing_values[2]))
                break
        else:
        # Sản phẩm chưa tồn tại, thêm mới vào treeview2
            treeview2.insert("", "end", text=product_name, values=values)

root = tk.Tk()
# Tạo Treeview 1
treeview1 = ttk.Treeview(root, columns=("type", "quantity", "cost"))
treeview1.heading("#0", text="Tên sản phẩm")
treeview1.heading("type", text="Loại sản phẩm")
treeview1.heading("quantity", text="Số lượng")
treeview1.heading("cost", text="Đơn giá")
treeview1.pack(side=tk.LEFT, padx=10, pady=10)

# Cài đặt kích thước các cột trong Treeview 1
treeview1.column("#0", width=150)
treeview1.column("type", width=150)
treeview1.column("quantity", width=100)
treeview1.column("cost", width=100)

# Tạo Treeview 2
treeview2 = ttk.Treeview(root, columns=("type", "quantity", "cost"))
treeview2.heading("#0", text="Tên sản phẩm")
treeview2.heading("type", text="Loại sản phẩm")
treeview2.heading("quantity", text="Số lượng")
treeview2.heading("cost", text="Đơn giá")
treeview2.pack(side=tk.LEFT, padx=10, pady=10)

# Cài đặt kích thước các cột trong Treeview 2
treeview2.column("#0", width=150)
treeview2.column("type", width=150)
treeview2.column("quantity", width=100)
treeview2.column("cost", width=100)

# Gắn sự kiện nhấp chuột vào Treeview 1
treeview1.bind("<ButtonRelease-1>", copy_selected_item)

# Hàm xóa sản phẩm
def delete_selected_item():
    selected_item = treeview2.focus()
    if selected_item:
        treeview2.delete(selected_item)

# Tạo nút "Xóa"
delete_button = tk.Button(root, text="Xóa", command=delete_selected_item)
delete_button.pack(pady=10)

def search_product():
    # Lấy giá trị từ ô tìm kiếm
    search_text = search_entry.get()

    # Xóa tất cả các dòng trong treeview1
    treeview1.delete(*treeview1.get_children())

    # Kết nối cơ sở dữ liệu MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='PHW#84#jeor',
        database='amitdb'
    )

    # Tạo con trỏ để thao tác với cơ sở dữ liệu
    cursor = connection.cursor()

    # Truy vấn để lấy dữ liệu từ bảng "products" dựa trên tên sản phẩm hoặc loại sản phẩm
    query = "SELECT * FROM products WHERE name LIKE %s OR type LIKE %s"
    values = (f"%{search_text}%", f"%{search_text}%")

    # Thực thi truy vấn
    cursor.execute(query, values)

    # Lặp qua kết quả truy vấn và cập nhật dữ liệu vào treeview1
    for row in cursor:
        product_name = row[0]
        product_type = row[1]
        quantity = row[2]
        unit_price = row[3]

        treeview1.insert("", "end", text=product_name, values=(product_type, quantity, unit_price))

    # Đóng con trỏ và kết nối cơ sở dữ liệu
    cursor.close()
    connection.close()
# Tạo Entry và Button cho ô tìm kiếm
search_frame = tk.Frame(root)
search_frame.pack(padx=10, pady=10)

search_label = tk.Label(search_frame, text="Tìm kiếm:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Tìm", command=search_product)
search_button.pack(side=tk.LEFT)

# Tạo ô tính tổng tiền
total_label = tk.Label(root, text="Tổng tiền:")
total_label.pack()
# Tạo nút tính tổng tiền
def calculate_total():
    total = 0

    # Lặp qua các dòng trong treeview
    for child in treeview2.get_children():
        quantity = int(treeview2.item(child, "values")[1])
        price = float(treeview2.item(child, "values")[2])
        total += quantity * price

    # Cập nhật giá trị tổng tiền vào ô tương ứng
    total_label.config(text="Tổng tiền: {:.2f}".format(total))
calculate_button = tk.Button(root, text="Tính tổng tiền", command=calculate_total)
calculate_button.pack()
# Gọi hàm tính tổng tiền khi cần thiết
calculate_total()

# Tạo nút "Tăng" để tăng số lượng sản phẩm trong treeview2
def increase_quantity():
    selected_item = treeview2.focus()
    current_quantity = int(treeview2.item(selected_item, "values")[1])
    new_quantity = current_quantity + 1
    treeview2.set(selected_item, "quantity", new_quantity)

# Tạo nút "Giảm" để giảm số lượng sản phẩm trong treeview2
def decrease_quantity():
    selected_item = treeview2.focus()
    current_quantity = int(treeview2.item(selected_item, "values")[1])
    if current_quantity > 1:
        new_quantity = current_quantity - 1
        treeview2.set(selected_item, "quantity", new_quantity)
# Tạo nút "Tăng" để tăng số lượng sản phẩm trong treeview2
increase_button = tk.Button(root, text="↑", command=increase_quantity)
increase_button.pack(padx=10, pady=5)

# Tạo nút "Giảm" để giảm số lượng sản phẩm trong treeview2
decrease_button = tk.Button(root, text="↓", command=decrease_quantity)
decrease_button.pack(padx=10, pady=5)

def delete_all():
    treeview2.delete(*treeview2.get_children())

    # Cập nhật lại tổng tiền
    calculate_total()
# Tạo nút "Xóa" để xóa dữ liệu trongtreeview2
delete_all_button = tk.Button(root, text="Xóa", command=delete_all)
delete_all_button.pack(padx=10, pady=5)
    
# Tải dữ liệu từ bảng "products" và cập nhật vào treeview1
load_data()
root.mainloop()
