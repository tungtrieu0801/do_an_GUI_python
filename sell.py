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
    back_button.place(relx=0.007, rely=0.003, width=100, height=45)
    
    scrollbarx = Scrollbar(sell_window, orient=HORIZONTAL)
    scrollbary = Scrollbar(sell_window, orient=VERTICAL)
    tree = ttk.Treeview(sell_window)
    tree.place(relx=0.03, rely=0.073, width=880, height=550)
    tree.configure(
            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set
        )
    tree.configure(selectmode="extended")

    # tree.bind("<<TreeviewSelect>>", on_tree_select)

    scrollbary.configure(command=tree.yview)
    scrollbarx.configure(command=tree.xview)

    scrollbary.place(relx=0.694, rely=0.003, width=22, height=548)
    scrollbarx.place(relx=0.007, rely=0.824, width=884, height=22)
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
    DisplayData(tree)
    side_frame = Frame(sell_window, bd=1, relief="solid")
    side_frame.place(relx=0.7, rely=0.073, width=350, height=550)
    
def DisplayData(tree):
    connection = mysql.connector.connect(
        host='localhost',
            user='root',
            password='080102',
            database='myDatabase'
        )
    cursor = connection.cursor()

        # find_user = "SELECT * FROM inventory"
    cursor.execute("SELECT * FROM inventory")

        # cur.execute("SELECT * FROM raw_inventory")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert("", "end", values=(data))
    # all_items = fetch
    