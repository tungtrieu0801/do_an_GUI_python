import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ast import main
import tkinter as tk
from tkinter import ttk
from styles import *
import mysql.connector
from tkinter import PhotoImage
from PIL import Image, ImageTk
from sale.home import create_home_page
from sale.contact_page import create_contact_page
from sale.about_page import create_about_page
from sale.product_page import create_product_page
sell_window = Tk()
sell_window.geometry("1366x768")
sell_window.title("Big Bazaar")
sell_window.resizable(0, 0)

#gọi hàm style căn chỉnh
configure_styles()
# sell_window = tk.Toplevel(root)
sell_window.title("sell")
        # Lấy kích thước của màn hình
screen_width = sell_window.winfo_screenwidth()
screen_height = sell_window.winfo_screenheight()
    #1366x768
window_width = 1366  # Thay đổi kích thước theo nhu cầu
window_height = 768  # Thay đổi kích thước theo nhu cầu
    # Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
sell_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
sell_window.resizable(width=False, height=False)


class Inventory:
    def __init__(self, top=None):
        self.message = Label(sell_window)
        self.message.place(relx=0.001, rely=0.001, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(sell_window)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(sell_window)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")



        self.button2 = Button(sell_window)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")


        self.button6 = Button(sell_window)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")



        self.scrollbarx = Scrollbar(sell_window, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(sell_window, orient=VERTICAL)
        self.tree = ttk.Treeview(sell_window)
        self.tree.place(relx=0.107, rely=0.103, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")



        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)
        self.tree.configure(
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
        self.tree.heading("ID", text="Employee ID", anchor=W)
        self.tree.heading("Tên sản phẩm", text="Tên sản phẩm", anchor=W)
        self.tree.heading("Loại sản phẩm", text="Loại sản phẩm", anchor=W)
        self.tree.heading("Số lượng", text="Số lượng", anchor=W)
        self.tree.heading("Giá", text="Giá", anchor=W)
        self.tree.heading("Nhà cung cấp", text="Nhà cung cấp", anchor=W)
        self.tree.heading("Liên lạc nhà cung cấp", text="Liên lạc nhà cung cấp", anchor=W)


        self.tree.column("#0", stretch=NO, minwidth=0, width=10)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)


Inventory()









    
#     # def search():
#     #     query = search_widget.get()
#     # Thực hiện tìm kiếm hoặc xử lý dữ liệu theo query ở đây
    
#     #tao frame san pham
# frame_back = ttk.Frame(sell_window)
# frame_back.place(x=20,y=20)
# back_button = ttk.Button(frame_back, text="Quay lại",  style='Back_Bbutton.TButton')
# back_button.grid(column=0,row=0)
# product_frame = ttk.Frame(sell_window)
# product_frame.place(x=10, y=70, width=800, height=600)
# style = ttk.Style()
# style.configure("Custom.TFrame", background="#c8c3d9")  # Thay đổi màu nền ở đây
# product_frame["style"] = "Custom.TFrame"

#     # def on_entry_click(event):
#     #     if search_widget.get() == "Tìm kiếm":
#     #         search_widget.delete(0, "end")
#     #         search_widget.configure(foreground="black")  # Thay đổi màu chữ thành đen

#     # def on_entry_leave(event):
#     #     if search_widget.get() == "":
#     #         search_widget.insert(0, "Tìm kiếm")
#     #         search_widget.configure(foreground="gray")  # Thay đổi màu chữ thành màu xám
#     # style = ttk.Style()
#     # style.configure("Search.TEntry", padding=(5, 5), font=("Helvetica", 20), background="white", bordercolor="gray", relief="flat")

#     # search_widget = ttk.Entry(product_frame, foreground="gray", width=30, style="Search.TEntry")
#     # search_widget.insert(0, "Tìm kiếm")
#     # search_widget.configure(font=("Helvetica", 17))  # Điều chỉnh font size
#     # search_widget.grid(column=0, row=0, padx=(50, 0), pady=20)

#     # search_widget.bind("<FocusIn>", on_entry_click)
#     # search_widget.bind("<FocusOut>", on_entry_leave)



# def switch_indicator(indicator_color, create_page_function):
#     for child in product_frame.winfo_children():
#         if isinstance(child, tk.Label):
#             child['bg'] = 'SystemButtonFace'
#     indicator_color['bg'] = 'green'

#     for fm in main_fm.winfo_children():
#         fm.destroy()
#         sell_window.update()

#     create_page_function(main_fm)
#         # create_page_function(sell_window)
# option_fm = tk.Frame(product_frame)
# option_fm.grid(column=0, row=0)
# option_fm.pack_propagate(False)
# option_fm.configure(width=700, height=200)

# button_width = 100
# button_count = 5
# space_between_buttons = (600 - (button_count * button_width)) // (button_count + 1)

# btn_home = tk.Button(product_frame, text="Đồ ăn nhanh", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(home_indicator_lb, create_home_page))
# btn_home.place(x=space_between_buttons, y=0, width=button_width)

# btn_product = tk.Button(product_frame, text="Đồ uống", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(product_indicator_lb, create_product_page))
# btn_product.place(x=2 * space_between_buttons + button_width, y=0, width=button_width)

# btn_contact = tk.Button(product_frame, text="Hoa quả", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(contact_indicator_lb, create_contact_page))
# btn_contact.place(x=3 * space_between_buttons + 2 * button_width, y=0, width=button_width)

# btn_about = tk.Button(product_frame, text="Khác", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(about_indicator_lb, create_about_page))
# btn_about.place(x=4 * space_between_buttons + 3 * button_width, y=0, width=button_width)

# btn_about1 = tk.Button(product_frame, text="Khác", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(about_indicator_lb, create_about_page))
# btn_about1.place(x=4 * space_between_buttons + 4 * button_width, y=0, width=button_width)

# home_indicator_lb = tk.Label(product_frame, bg='green')
# home_indicator_lb.place(x=98, y=30, width=50, height=2)

# product_indicator_lb = tk.Label(product_frame)
# product_indicator_lb.place(x=285, y=30, width=50, height=2)

# contact_indicator_lb = tk.Label(product_frame)
# contact_indicator_lb.place(x=470, y=30, width=50, height=2)

# about_indicator_lb = tk.Label(product_frame)
# about_indicator_lb.place(x=650, y=30, width=50, height=2)
    
# main_fm = tk.Frame(product_frame,width=800, height=400)
# main_fm.place(x=10, y=50)
# create_home_page(main_fm)  # Hiển thị trang Home ban đầu



#     #tao frame tinh tien

# def update_total():
#     total_label.config(text="Tổng tiền: $100.00")  # Thay đổi giá trị này bằng tổng tiền thực tế

# total_frame = ttk.Frame(sell_window)
# total_frame.place(x=780, y=100, width=400, height=600)
# style = ttk.Style()
# style.configure("Custom.TFrame", background="#c8c3d9")  # Thay đổi màu nền ở đây
# total_frame["style"] = "Custom.TFrame"

#     # Thêm một Label để hiển thị tổng tiền
# total_label = ttk.Label(total_frame, text="Tổng tiền: $0.00", font=("Helvetica", 20))
# total_label.pack(pady=20)

#     # Thêm một Treeview để hiển thị danh sách sản phẩm trong giỏ hàng
    
# cart_treeview = ttk.Treeview(total_frame, columns=("Name", "Quantity", "Price"), show="headings")
# cart_treeview.heading("Name", text="Tên sản phẩm")
# cart_treeview.heading("Quantity", text="Số lượng")
# cart_treeview.heading("Price", text="Giá tiền")
# cart_treeview.pack(fill="both", expand=True)
    
#     # Thêm một nút để cập nhật tổng tiền
# update_button = ttk.Button(total_frame, text="Cập nhật tổng tiền", command=update_total)
# update_button.pack(pady=20)
    



sell_window.mainloop()