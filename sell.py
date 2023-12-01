from ast import main
import tkinter as tk
from tkinter import ttk
from styles import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from sale.home import create_home_page
from sale.contact_page import create_contact_page
from sale.about_page import create_about_page
from sale.product_page import create_product_page
import re
from sqlite3 import Cursor
from tkinter import simpledialog

import pandas as pd
from tkinter import filedialog
import mysql.connector
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
def sell(root):
    def display_data(tree):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            database='myDatabase'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM inventory")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert("", "end", values=data)
        tree.all_items = fetch
    # def search_product():
    #     # Lấy giá trị từ ô tìm kiếm
    #     search_text = search_entry.get()

    #     # Xóa tất cả các dòng trong treeview1
    #     tree.delete(*tree.get_children())

    #     # Kết nối cơ sở dữ liệu MySQL
    #     connection = mysql.connector.connect(
    #         host='localhost',
    #         user='root',
    #         password='080102',
    #         database='mydatabase'
    #     )

    #     # Tạo con trỏ để thao tác với cơ sở dữ liệu
    #     cursor = connection.cursor()
    #     if search_text:  # Nếu có giá trị trong ô tìm kiếm
    #     # Truy vấn để lấy dữ liệu từ bảng "inventory" dựa trên tên sản phẩm hoặc loại sản phẩm
    #         query = "SELECT * FROM inventory WHERE product_name LIKE %s OR category LIKE %s"
    #         values = (f"%{search_text}%", f"%{search_text}%")

    #     # Thực thi truy vấn
    #         cursor.execute(query, values)
    #     else:  # Nếu không có giá trị trong ô tìm kiếm, lấy toàn bộ dữ liệu
    #     # Truy vấn để lấy toàn bộ dữ liệu từ bảng "inventory"
    #         query = "SELECT * FROM inventory"

    #     # Thực thi truy vấn
    #     cursor.execute(query)
    #     for row in cursor:
    #         product_name = row[1]
    #         category = row[2]
    #         quantity = row[4]  # Assuming "stock" is the correct column index
    #         unit_price = row[3]  # Assuming "product_price" is the correct column index

    #     tree.insert("", "end", values=(product_name, category, quantity, unit_price))


    #     # Đóng con trỏ và kết nối cơ sở dữ liệu
    #     cursor.close()
    #     connection.close()
    def search_product():
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            database='myDatabase'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM inventory")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert("", "end", values=data)
        all_items = fetch
        search_text = search_entry.get()  # Lấy giá trị từ ô tìm kiếm
        if not search_text:
            for item in tree.get_children():
                tree.delete(item)
        # Hiển thị toàn bộ sản phẩm trên treeview
            for item in all_items:
                tree.insert("", "end", values=item)
            return
        # Xóa toàn bộ sản phẩm hiển thị trên treeview
        for item in tree.get_children():
            tree.delete(item)

        found = False
        for item in all_items:  # all_items là danh sách tất cả các sản phẩm trước khi tìm kiếm
            if search_text in str(item[0]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

            if search_text in str(item[1]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

            if search_text in str(item[2]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

        if not found:
            messagebox.showerror("Oops!!", f"Product ID: {search_text} not found.")



    #gọi hàm style căn chỉnh
    configure_styles()
    sell_window = tk.Toplevel(root)
    sell_window.title("sell")
        # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    #1366x768
    window_width = 1366  # Thay đổi kích thước theo nhu cầu
    window_height = 768  # Thay đổi kích thước theo nhu cầu
    # Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
    sell_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    sell_window.resizable(width=False, height=False)

    def close_window_2():
        sell_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    # frame_back = ttk.Frame(sell_window)
    # frame_back.place(x=20,y=20)
    back_button = ttk.Button(sell_window, text="Quay lại", command=close_window_2, style='Back_Bbutton.TButton')
    back_button.place(relx=0.007, rely=0.008, width=100, height=45)
    
    scrollbarx = Scrollbar(sell_window, orient=HORIZONTAL)
    scrollbary = Scrollbar(sell_window, orient=VERTICAL)
    tree = ttk.Treeview(sell_window)
    tree.place(relx=0.03, rely=0.2, width=880, height=550)
    tree.configure(
            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set
        )
    tree.configure(selectmode="extended")

    # tree.bind("<<TreeviewSelect>>", on_tree_select)

    scrollbary.configure(command=tree.yview)
    scrollbarx.configure(command=tree.xview)

    scrollbary.place(relx=0.68, rely=0.2, width=22, height=548)
    scrollbarx.place(relx=0.03, rely=0.92, width=884, height=22)
    tree.configure(
            columns=(
                "ID",
                "Tên sản phẩm",
                "Loại sản phẩm",
                "Số lượng",
                "Giá",
                "Nhà cung cấp",
                "Liên lạc nhà cung cấp"
            )
        )
#product_id, product_name,category ,stock, product_price
    tree.heading("ID", text="Employee ID", anchor=W)
    tree.heading("Tên sản phẩm", text="Tên sản phẩm", anchor=W)
    tree.heading("Loại sản phẩm", text="Loại sản phẩm", anchor=W)
    tree.heading("Số lượng", text="Số lượng", anchor=W)
    tree.heading("Giá", text="Giá", anchor=W)
    tree.heading("Nhà cung cấp", text="Nhà cung cấp", anchor=W)
    tree.heading("Liên lạc nhà cung cấp", text="Liên lạc nhà cung cấp", anchor=W)


    tree.column("#0", stretch=NO, minwidth=0, width=10)
    tree.column("#1", stretch=NO, minwidth=0, width=80)
    tree.column("#2", stretch=NO, minwidth=0, width=260)
    tree.column("#3", stretch=NO, minwidth=0, width=100)
    tree.column("#4", stretch=NO, minwidth=0, width=120)
    tree.column("#5", stretch=NO, minwidth=0, width=80)
    tree.column("#6", stretch=NO, minwidth=0, width=80)
    tree.column("#7", stretch=NO, minwidth=0, width=80)
    display_data(tree)
    side_frame = Frame(sell_window, bd=1, relief="solid")
    side_frame.place(relx=0.7, rely=0.2, width=350, height=550)

    search_entry = ttk.Entry(sell_window)
    search_entry.place(relx=0.03, rely=0.1, width=200, height=30)
    button1 = Button(sell_window)
    button1.place(relx=0.19, rely=0.105, width=76, height=23)
    button1.configure(relief="flat")
    button1.configure(overrelief="flat")
    button1.configure(activebackground="#CF1E14")
    button1.configure(cursor="hand2")
    button1.configure(foreground="#ffffff")
    button1.configure(background="#CF1E14")
    button1.configure(font="-family {Poppins SemiBold} -size 10")
    button1.configure(borderwidth="0")
    button1.configure(text="""Tìm kiếm""")
    button1.configure(command=search_product)

    


