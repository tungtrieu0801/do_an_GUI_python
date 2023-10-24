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
def sell(root):
    #gọi hàm style căn chỉnh
    configure_styles()
    sell_window = tk.Toplevel(root)
    sell_window.title("sell")
        # Lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 1600  # Thay đổi kích thước theo nhu cầu
    window_height = 920  # Thay đổi kích thước theo nhu cầu
    # Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
    sell_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    sell_window.resizable(width=False, height=False)

    def close_window_2():
        sell_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    frame_back = ttk.Frame(sell_window)
    frame_back.place(x=20,y=20)
    back_button = ttk.Button(frame_back, text="Quay lại", command=close_window_2, style='Back_Bbutton.TButton')
    back_button.grid(column=0,row=0,padx=(0,250))
    
    def search():
        query = search_widget.get()
    # Thực hiện tìm kiếm hoặc xử lý dữ liệu theo query ở đây
    
    #tao frame san pham
    product_frame = ttk.Frame(sell_window)
    product_frame.place(x=50, y=100, width=1000, height=700)
    style = ttk.Style()
    style.configure("Custom.TFrame", background="#c8c3d9")  # Thay đổi màu nền ở đây
    product_frame["style"] = "Custom.TFrame"

    def on_entry_click(event):
        if search_widget.get() == "Tìm kiếm":
            search_widget.delete(0, "end")
            search_widget.configure(foreground="black")  # Thay đổi màu chữ thành đen

    def on_entry_leave(event):
        if search_widget.get() == "":
            search_widget.insert(0, "Tìm kiếm")
            search_widget.configure(foreground="gray")  # Thay đổi màu chữ thành màu xám
    style = ttk.Style()
    style.configure("Search.TEntry", padding=(5, 5), font=("Helvetica", 20), background="white", bordercolor="gray", relief="flat")

    search_widget = ttk.Entry(product_frame, foreground="gray", width=30, style="Search.TEntry")
    search_widget.insert(0, "Tìm kiếm")
    search_widget.configure(font=("Helvetica", 17))  # Điều chỉnh font size
    search_widget.grid(column=0, row=0, padx=(50, 0), pady=20)

    search_widget.bind("<FocusIn>", on_entry_click)
    search_widget.bind("<FocusOut>", on_entry_leave)



    def switch_indicator(indicator_color, create_page_function):
        for child in option_fm.winfo_children():
            if isinstance(child, tk.Label):
                child['bg'] = 'SystemButtonFace'
        indicator_color['bg'] = 'green'

        for fm in main_fm.winfo_children():
            fm.destroy()
            root.update()

        create_page_function(main_fm)
        # create_page_function(sell_window)

    option_fm = tk.Frame(product_frame)
    option_fm.grid(column=0, row=1,padx=(20,0))
    option_fm.pack_propagate(False)
    option_fm.configure(width=900, height=200)

    button_width = 125
    button_count = 4
    space_between_buttons = (800 - (button_count * button_width)) // (button_count + 1)

    btn_home = tk.Button(option_fm, text="Đồ ăn nhanh", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(home_indicator_lb, create_home_page))
    btn_home.place(x=space_between_buttons, y=0, width=button_width)

    btn_product = tk.Button(option_fm, text="Đồ uống", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(product_indicator_lb, create_product_page))
    btn_product.place(x=2 * space_between_buttons + button_width, y=0, width=button_width)

    btn_contact = tk.Button(option_fm, text="Hoa quả", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(contact_indicator_lb, create_contact_page))
    btn_contact.place(x=3 * space_between_buttons + 2 * button_width, y=0, width=button_width)

    btn_about = tk.Button(option_fm, text="Khác", activeforeground="red", bd=0, fg="black", command=lambda: switch_indicator(about_indicator_lb, create_about_page))
    btn_about.place(x=4 * space_between_buttons + 3 * button_width, y=0, width=button_width)

    home_indicator_lb = tk.Label(option_fm, bg='green')
    home_indicator_lb.place(x=98, y=30, width=50, height=2)

    product_indicator_lb = tk.Label(option_fm)
    product_indicator_lb.place(x=285, y=30, width=50, height=2)

    contact_indicator_lb = tk.Label(option_fm)
    contact_indicator_lb.place(x=470, y=30, width=50, height=2)

    about_indicator_lb = tk.Label(option_fm)
    about_indicator_lb.place(x=650, y=30, width=50, height=2)
    
    main_fm = tk.Frame(product_frame,width=900, height=400)
    main_fm.grid(column=0, row=2,padx=(20,0))
    create_home_page(main_fm)  # Hiển thị trang Home ban đầu
    # create_contact_page(main_fm)
    # create_product_page(main_fm)
    # create_about_page(main_fm)

    


















    # fastFood = ttk.Label(product_frame,text="Đồ ăn nhanh")
    # fastFood.grid(column=0, row=1,padx=30, pady=30)

    # drinkFood = ttk.Label(product_frame,text="Đồ uống")
    # drinkFood.grid(column=1, row=1,padx=30, pady=30)

    # vegetable = ttk.Label(product_frame,text="Rau, hoa quả")
    # vegetable.grid(column=2, row=1,padx=30, pady=30)

    # do_dung_gia_dinh = ttk.Label(product_frame,text="Đồ dùng gia đình")
    # do_dung_gia_dinh.grid(column=3, row=1)


    #tao frame tinh tien

    total_frame = ttk.Frame(sell_window)
    total_frame.place(x=1080, y=100, width=470, height=700)
    style = ttk.Style()
    style.configure("Custom.TFrame", background="#c8c3d9")  # Thay đổi màu nền ở đây
    total_frame["style"] = "Custom.TFrame"

    #frame thanh toan

    thanhtoan_label = ttk.Label(total_frame, text="Thanh Toán")
    thanhtoan_label.grid(row=0,column=0, padx=30,pady=30)

    showProduct = ttk.Label(total_frame, text="Sản phẩm đã mua")
    showProduct.grid(column=0, row=1)
    

    # prodcutShow = ttk.Frame(total_frame)
    # prodcutShow.grid(column=0, row=2)
    # style.configure("Custom.TFrame", background="black")  # Thay đổi màu nền ở đây
    # prodcutShow["style"] = "Custom.TFrame"
    
    total_label = ttk.Label(total_frame,text="Tong so tien")
    total_label.grid(column=0, row=2,padx=30, pady=30)

    money = ttk.Label(total_frame,text="300000")
    money.grid(column=1, row=2)


    buttonPay = ttk.Button(total_frame, text="Thanh Toan")
    buttonPay.grid(column=0, row=3, columnspan=2)