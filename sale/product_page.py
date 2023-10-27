import tkinter as tk
from tkinter import ttk
from styles import style_for_text
import mysql.connector

def create_product_page(main_fm):
    style_for_text()
    home_page_fm = ttk.Frame(main_fm)
    home_page_fm.place(x=0, y=0, relwidth=1, relheight=1)
    
    treeview = ttk.Treeview(home_page_fm, columns=("Name", "Type", "Stock", "Price"), show="headings", style="Custom.Treeview")
    treeview.heading("Name", text="Tên sản phẩm")
    treeview.heading("Type", text="Loại sản phẩm")
    treeview.heading("Stock", text="Số lượng")
    treeview.heading("Price", text="Giá tiền")
    treeview.pack()



    # Định nghĩa hàm để cập nhật dữ liệu trên treeview
    def update_treeview():
        treeview.delete(*treeview.get_children())  # Xóa toàn bộ dữ liệu trong treeview
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            database='mydb'
        )
        cursor = connection.cursor()

        select_query = "SELECT * FROM products WHERE type = 'nguoi'"
        cursor.execute(select_query)

        # Lấy tất cả các sản phẩm có loại là "rượu" và hiển thị trong treeview
        for product in cursor.fetchall():
            treeview.insert("", "end", values=product)

        cursor.close()
        connection.close()

    # Đây có thể là nơi trong mã của bạn khi cơ sở dữ liệu thay đổi (ví dụ: khi thêm/sửa/xóa sản phẩm)
    # Bất cứ khi nào dữ liệu thay đổi, bạn gọi hàm update_treeview() để cập nhật treeview.
    update_treeview()
