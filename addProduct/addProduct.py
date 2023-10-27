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
    
    label = ttk.Label(frame_back, text="Thêm sản phẩm mới tại đây", foreground="green",font=("Arial", 25,'bold'),)  # Đặt kích thước font là 16
    label.grid(row=0, column=1)
    





    # #Để tạm mai fix
    # db = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="PHW#84#jeor",
    #     database="amitdb"
    # )

    # mycursor = db.cursor()

    # def Add():
    #     ProID = e1.get()
    #     ProName = e2.get()
    #     ProType = e3.get()
    #     ProCost = e4.get()
    #     ProNum = e5.get()

    #     sql = "INSERT INTO product (ProID, ProName, ProType, ProCost, ProNum) VALUES (%s, %s, %s, %s, %s)"
    #     val = (ProID, ProName, ProType, ProCost, ProNum)
    #     mycursor.execute(sql, val)
    #     db.commit()

    # def Edit():
    #     ProID = e1.get()
    #     ProName = e2.get()
    #     ProType = e3.get()
    #     ProCost = e4.get()
    #     ProNum = e5.get()

    #     sql = "UPDATE product SET ProName = %s, ProType = %s, ProCost = %s, ProNum = %s WHERE ProID = %s"
    #     val = (ProName, ProType, ProCost, ProNum, ProID)
    #     mycursor.execute(sql, val)
    #     db.commit()

    # def Delete():
    #     ProID = e1.get()

    #     sql = "DELETE FROM product WHERE ProID = %s"
    #     val = (ProID,)
    #     mycursor.execute(sql, val)
    #     db.commit()

    # def show():
    #     mycursor.execute("SELECT ProID, ProName, ProType, ProCost, ProNum FROM product")
    #     records = mycursor.fetchall()
    #     print(records)

    #     for i, (ProID, ProName, ProType, ProCost, ProNum) in enumerate(records, start=1):
    #         listBox.insert("", "end", values=(ProID, ProName, ProType, ProCost, ProNum))

    # root = Tk()
    # root.geometry("800x800")

    # ProID = Label(root, text="ProID")
    # ProName = Label(root, text="ProName")
    # ProType = Label(root, text="ProType")
    # ProCost = Label(root, text="ProCost")
    # ProNum = Label(root, text="ProNum")

    # ProID.grid(row=1, column=2)
    # ProName.grid(row=2, column=2)
    # ProType.grid(row=3, column=2)
    # ProCost.grid(row=4, column=2)
    # ProNum.grid(row=5, column=2)

    # e1 = Entry(root)
    # e2 = Entry(root)
    # e3 = Entry(root)
    # e4 = Entry(root)
    # e5 = Entry(root)

    # e1.grid(row=1, column=3)
    # e2.grid(row=2, column=3)
    # e3.grid(row=3, column=3)
    # e4.grid(row=4, column=3)
    # e5.grid(row=5, column=3)

    # Button(root, text="Add", command=Add, height=3, width=10).place(x=150, y=450)
    # Button(root, text="Edit", command=Edit, height=3, width=10).place(x=400, y=450)
    # Button(root, text="Delete", command=Delete, height=3, width=10).place(x=650, y=450)

    # cols = ('ProID', 'ProName', 'ProType', 'ProCost', 'ProNum')
    # listBox = ttk.Treeview(root, columns=cols, show='headings')

    # for col in cols:
    #     listBox.heading(col, text=col)
    #     listBox.grid(row=1, column=0, columnspan=2)
    #     listBox.place(x=9, y=150)

    # Button(root, text="Show", command=show, height=3, width=10).place(x=250, y=450)

    # root.mainloop()
