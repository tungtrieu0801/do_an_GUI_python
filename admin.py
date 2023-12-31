import re
from sqlite3 import Cursor
from tkinter import simpledialog
import tkinter
from turtle import color
from PIL import Image, ImageTk
import pandas as pd
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
root = Tk()
root.geometry("1366x768")
root.title("Retail Manager(ADMIN)")
user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
def valid_phone(phn):
    pass
def statistics():
    adm.withdraw()
    global statistic
    statistic = Toplevel()
    page10 = Statistics(statistic)
    statistic.protocol("WM_DELETE_WINDOW", exitt)
    statistic.mainloop()
def invoices():
    adm.withdraw()
    global invoice
    invoice = Toplevel()
    page7 = Invoice(invoice)
    page7.time()
    invoice.protocol("WM_DELETE_WINDOW", exitt)
    invoice.mainloop()
def random_emp_id(stringLength):
    Digits = string.digits
    strr=''.join(random.choice(Digits) for i in range(stringLength-3))
    return ('EMP'+strr)

def inventory():
    adm.withdraw()
    global inv
    global page3
    inv = Toplevel()
    page3 = Inventory(inv)

    inv.protocol("WM_DELETE_WINDOW", exitt)
    inv.mainloop()

class Admin_Page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Quản trị")

        self.label1 = Label(adm)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/admin.png")
        self.label1.configure(image=self.img)

        self.message = Label(adm)
        self.message.place(relx=0.046, rely=0.056, width=62, height=30)
        self.message.configure(font="-family {Poppins} -size 12")
        self.message.configure(foreground="#ffffff")
        self.message.configure(background="#FE6B61")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.button1 = Button(adm)
        self.button1.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Đăng xuất""")
        self.button1.configure(command=self.Logout)

        self.button2 = Button(adm)
        self.button2.place(relx=0.14, rely=0.508, width=146, height=63)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#333333")
        self.button2.configure(background="#ffffff")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Kho hàng""")
        self.button2.configure(command=inventory)

        self.button3 = Button(adm)
        self.button3.place(relx=0.338, rely=0.508, width=146, height=63)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#ffffff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#333333")
        self.button3.configure(background="#ffffff")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Nhân viên""")
        self.button3.configure(command=employee)

        self.button4 = Button(adm)
        self.button4.place(relx=0.536, rely=0.508, width=146, height=63)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#ffffff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#333333")
        self.button4.configure(background="#ffffff")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Đơn hàng""")
        self.button4.configure(command=invoices)

        self.button5 = Button(adm)
        self.button5.place(relx=0.732, rely=0.508, width=146, height=63)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#ffffff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#333333")
        self.button5.configure(background="#ffffff")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""LIÊN HỆ""")
        self.button5.configure(command=statistics)
    def Logout(self):
        sure = messagebox.askyesno("Đăng xuất", "Bạn muốn đăng xuất?", parent=adm)
        if sure == True:
            adm.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


def employee():
    adm.withdraw()
    global emp
    global page5
    emp = Toplevel()
    page5 = Employee(emp)
    page5.time()
    emp.protocol("WM_DELETE_WINDOW", exitt)
    emp.mainloop()
class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Retail Manager(ADMIN)")
        self.center_window(top)
        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/admin_login_fixx.png")
        self.label1.configure(image=self.img)
        

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.373, rely=0.273, width=374, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.373, rely=0.384, width=374, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passwd)

        self.button1 = Button(root)
        self.button1.place(relx=0.366, rely=0.685, width=356, height=43)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#D2463E")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#D2463E")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Đăng nhập""")
        self.button1.configure(command=self.login)
    def center_window(self, top):
        top.update_idletasks()
        width = top.winfo_width()
        height = top.winfo_height()
        x = (top.winfo_screenwidth() // 2) - (width // 2)
        y = (top.winfo_screenheight() // 2) - (height // 2)
        top.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    def login(self, Event=None):
        username = user.get()
        password = passwd.get()

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            # database='store'
            database= 'mydatabase'
        )
        cursor = connection.cursor()

        find_user = "SELECT * FROM employee WHERE emp_id = %s AND password = %s"
        cursor.execute(find_user, (username, password))

        results = cursor.fetchall()
        cursor.close()  # Đóng con trỏ sau khi thực hiện truy vấn
        connection.close()  # Đóng kết nối cơ sở dữ liệu
        if results:
            if results[0][0]=="ADMIN":
                messagebox.showinfo("OK", "Đăng nhập thành công.")
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)

                root.withdraw()
                global adm
                global page2
                adm = Toplevel()
                page2 = Admin_Page(adm)
                #page2.time()
                adm.protocol("WM_DELETE_WINDOW", exitt)
                adm.mainloop()
            else:
                messagebox.showerror("No!!", "Bạn không phải người quản trị.")

        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            page1.entry2.delete(0, END)
def exitt():
    sure = messagebox.askyesno("Thoát","Bạn muốn thoát?", parent=root)
    if sure == True:
        adm.destroy()
        root.destroy()

class Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Quản lí nhân viên")


        self.label1 = Label(emp)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/employee_fix.png")
        self.label1.configure(image=self.img)

        self.message = Label(emp)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(emp)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(emp)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(emp)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Tìm kiếm""")
        self.button1.configure(command=self.search_emp)

        self.button2 = Button(emp)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Đăng xuất""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(emp)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""THÊM NHÂN VIÊN""")
        self.button3.configure(command=self.add_emp)

        self.button4 = Button(emp)
        self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""CẬP NHẬT THÔNG TIN""")
        self.button4.configure(command=self.update_emp)

        self.button5 = Button(emp)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""XOÁ NHÂN VIÊN""")
        self.button5.configure(command=self.delete_emp)

        self.button6 = Button(emp)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""THOÁT""")
        self.button6.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(emp, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(emp, orient=VERTICAL)
        self.tree = ttk.Treeview(emp)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Account",
                "Employee Name",
                "Password",
                "Address",
                "PhoneNumber",
            )
        )

        self.tree.heading("Account", text="Tài khoản", anchor=W)
        self.tree.heading("Employee Name", text="Tên nhân viên", anchor=W)
        self.tree.heading("Password", text="Mật khẩu", anchor=W)
        self.tree.heading("Address", text="Địa chỉ", anchor=W)
        self.tree.heading("PhoneNumber", text="Số điện thoại", anchor=W)
        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=100)
        self.tree.column("#2", stretch=NO, minwidth=0, width=200)
        self.tree.column("#3", stretch=NO, minwidth=0, width=160)
        self.tree.column("#4", stretch=NO, minwidth=0, width=178)
        self.DisplayData()

    def DisplayData(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            database='mydatabase'
        )
        cursor = connection.cursor()

        # find_user = "SELECT * FROM employee WHERE emp_id = %s AND password = %s"
        cursor.execute("SELECT * FROM employee")
        
        # cursor.execute("SELECT * FROM employee")
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))
        self.all_items = fetch
    def search_emp(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Thành công!!", "Tìm thấy nhân viên: {} ".format(self.entry1.get()), parent=emp)
                break
        else: 
            messagebox.showerror("Xin lỗi!!", "Không tồn tại nhân viên: {} .".format(self.entry1.get()), parent=emp)
    def search_emp(self):
        search_text = self.entry1.get()  # Lấy giá trị từ ô tìm kiếm
        if not search_text:
            for item in self.tree.get_children():
                self.tree.delete(item)
        # Hiển thị toàn bộ sản phẩm trên treeview
            for item in self.all_items:
                self.tree.insert("", "end", values=item)
            return
        # Xóa toàn bộ sản phẩm hiển thị trên treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        found = False
        for item in self.all_items:  # all_items là danh sách tất cả các sản phẩm trước khi tìm kiếm
            if search_text in str(item[0]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

            if search_text in str(item[1]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

            if search_text in str(item[2]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

            if search_text in str(item[3]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True
            if search_text in str(item[4]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

        if not found:
            messagebox.showerror("Ôi không!!", f"Không tìm thấy nhân viên: {search_text} .", parent=inv)

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_emp(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xoá không?", parent=emp)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])
                
                flag = 1

                for k in to_delete:
                    if k=="EMP0000":
                        flag = 0
                        break
                    else:
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='080102',
                            database='mydatabase'
                        )
                        cursor = connection.cursor()
                        delete = "DELETE FROM employee WHERE emp_id = %s"
                        cursor.execute(delete, [k])
                        connection.commit()

                if flag==1:
                    messagebox.showinfo("Thành công!!", "Đã xoá tài khoản nhân viên.", parent=emp)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())
                    self.DisplayData()
                else:
                    messagebox.showerror("Lỗi!!","Không thể xoá tài quản quản trị viên .")
        else:
            messagebox.showerror("Lỗi!!","Hãy chọn một nhân viên.", parent=emp)

    def update_emp(self):
        
        if len(self.sel)==1:
            global e_update
            e_update = Toplevel()
            page8 = Update_Employee(e_update)
            page8.time()
            e_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)
            page8.entry1.insert(0, vall[1])
            page8.entry2.insert(0, vall[2])
            page8.entry3.insert(0, vall[3])
            page8.entry4.insert(0, vall[4])
            e_update.mainloop()
        elif len(self.sel)==0:
            messagebox.showerror("Lỗi","Vui lòng chọn một nhân viên để cập nhật.")
        else:
            messagebox.showerror("Lỗi","Can only update one employee at a time.")

    def add_emp(self):
        global e_add
        global page6
        e_add = Toplevel()
        page6 = add_employee(e_add)
        page6.time()
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.mainloop()


    def ex(self):
        e_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()   

    def ex2(self):
        e_update.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()  

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Thoát","Bạn muốn thoát?", parent=emp)
        if sure == True:
            emp.destroy()
            adm.deiconify()

    def Logout(self):
        sure = messagebox.askyesno("Đăng xuất", "Bạn muốn đăng xuất?")
        if sure == True:
            emp.destroy()
            root.deiconify()
            
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

class Inventory:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Inventory")
        self.center_window(top)
        self.label1 = Label(inv)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/inventory_fix.png")
        self.label1.configure(image=self.img)
            # Create a custom style with padding
        style = ttk.Style()
        style.configure("Padded.TButton", padding=(10, 5))
        self.message = Label(inv)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(inv)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(inv)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(inv)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Tìm kiếm""")
        self.button1.configure(command=self.search_product)

        self.button2 = Button(inv)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Đăng xuất""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(inv)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""THÊM SẢN PHẨM""")
        self.button3.configure(command=self.add_product)
        
        self.button4 = Button(inv)
        self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""CẬP NHẬT SẢN PHẨM""")
        self.button4.configure(command=self.update_product)

        self.button5 = Button(inv)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""XOÁ SẢN PHẨM""")
        self.button5.configure(command=self.delete_product)

        self.button7 = ttk.Button(inv,style="Padded.TButton")
        self.button7.place(relx=0.052, rely=0.67)
        self.button7.configure(text="Xuất excel")
        self.button7.configure(command=self.export_excel)


    
        self.button8 = ttk.Button(inv,style="Padded.TButton")
        self.button8.place(relx=0.15, rely=0.67)
        self.button8.configure(text="Nhập excel")
        self.button8.configure(command=self.import_excel)


        self.button6 = Button(inv)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Thoát""")
        self.button6.configure(command=self.Exit)


        self.scrollbarx = Scrollbar(inv, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(inv, orient=VERTICAL)
        self.tree = ttk.Treeview(inv)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

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
        self.tree.heading("ID", text="ID", anchor=W)
        self.tree.heading("Tên sản phẩm", text="Tên sản phẩm", anchor=W)
        self.tree.heading("Loại sản phẩm", text="Loại sản phẩm", anchor=W)
        self.tree.heading("Số lượng", text="Giá(VND", anchor=W)
        self.tree.heading("Giá", text="Số lượng", anchor=W)
        self.tree.heading("Nhà cung cấp", text="Nhà cung cấp", anchor=W)
        self.tree.heading("Liên lạc nhà cung cấp", text="Số điện thoại", anchor=W)


        self.tree.column("#0", stretch=NO, minwidth=0, width=10)
        self.tree.column("#1", stretch=NO, minwidth=0, width=60)
        self.tree.column("#2", stretch=NO, minwidth=0, width=240)
        self.tree.column("#3", stretch=NO, minwidth=0, width=110)
        self.tree.column("#4", stretch=NO, minwidth=0, width=70)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=100)
        self.tree.column("#7", stretch=NO, minwidth=0, width=120)

        self.DisplayData()
        #################3
        self.total_value_label = Label(inv)
        self.total_value_label.place(relx=0.06, rely=0.8, width=280, height=23)
        self.total_value_label.configure(font="-family {Poppins SemiBold} -size 12")
        self.total_value_label.configure(foreground="#000000")
        self.total_value_label.configure(background="#ffffff")
        self.update_total_value_label() 
    #dieu chinh label tong gia tri
    def update_total_value_label(self):
        total_value = self.calculate_total_value()
        self.total_value_label.configure(text=f"Tổng giá trị kho hàng: {total_value} VND")

    def calculate_total_value(self):
        total_value = 0
        for item in self.tree.get_children():
            quantity = int(self.tree.item(item, 'values')[3])
            price = float(self.tree.item(item, 'values')[4])
            total_value += quantity * price
        return total_value
    def center_window(self, top):
        top.update_idletasks()
        width = top.winfo_width()
        height = top.winfo_height()
        x = (top.winfo_screenwidth() // 2) - (width // 2)
        y = (top.winfo_screenheight() // 2) - (height // 2)
        top.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    def import_excel(self):
        # Ask the user to choose an Excel file for import
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        df = pd.read_excel(file_path)
        df = df.dropna()
        df = df.fillna(value='none')  # Thay 'default_value' bằng giá trị bạn muốn

        # If the user selected a file, proceed with import
        if file_path:
            try:
                # Connect to the MySQL database
                connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password='080102',
                database='myDatabase'
                )  # Replace with your database credentials

                cursor = connection.cursor()

                # Tên bảng trong MySQL để lưu trữ dữ liệu
                table_name = "inventory"

                # Xóa bảng cũ nếu tồn tại
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

                # Tạo bảng mới với các cột tương ứng từ tệp Excel
                cursor.execute(f"CREATE TABLE {table_name} ({', '.join([f'{col} VARCHAR(255)' for col in df.columns])})")

                # Chuyển dữ liệu từ pandas DataFrame vào MySQL
                for _, row in df.iterrows():
                    cursor.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['%s' for _ in df.columns])})", tuple(row))

                # Lưu thay đổi và đóng kết nối
                connection.commit()
                connection.close()
                page3.tree.delete(*page3.tree.get_children())
                self.DisplayData()
                
            except Exception as e:
                print(f"Lỗi: {e}")

    def export_excel(self):
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password='080102',
        database='myDatabase'
        )  # Replace with your database credentials
        # Query to fetch data from your MySQL table
        query = "SELECT * FROM inventory"  # Replace with your table name

        # Use pandas to read the SQL query result into a DataFrame
        df = pd.read_sql_query(query, connection)

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

        # If the user selected a file, export the DataFrame to Excel
        if file_path:
            df.to_excel(file_path, index=False)
            print(f"Data exported to {file_path}")

        # Close the database connection
        connection.close()
    def DisplayData(self):
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
            self.tree.insert("", "end", values=(data))
        self.all_items = fetch

    def search_product(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        try:
            to_search = int(self.entry1.get())
        except ValueError:
            messagebox.showerror("Lỗi!!", "Không hợp lệ.", parent=inv)
        else:
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Thành công!!", "Tìm thấy sản phẩm: {} .".format(self.entry1.get()), parent=inv)
                    break
            else: 
                messagebox.showerror("Lỗi!!", "Không tìm thấy sản phẩm: {} .".format(self.entry1.get()), parent=inv)
    
    def search_product(self):
        search_text = self.entry1.get()  # Lấy giá trị từ ô tìm kiếm
        if not search_text:
            for item in self.tree.get_children():
                self.tree.delete(item)

        # Hiển thị toàn bộ sản phẩm trên treeview
            for item in self.all_items:
                self.tree.insert("", "end", values=item)
            return
        # Xóa toàn bộ sản phẩm hiển thị trên treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        found = False
        for item in self.all_items:  # all_items là danh sách tất cả các sản phẩm trước khi tìm kiếm
            if search_text in str(item[0]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

            if search_text in str(item[1]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

            if search_text in str(item[2]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

            if search_text in str(item[5]):  # Kiểm tra xem giá trị tìm kiếm có trong sản phẩm hay không
                self.tree.insert("", "end", values=item)  # Nếu tìm thấy, thêm sản phẩm đó vào treeview
                found = True

        if not found:
            messagebox.showerror("Lỗi!!", f"Không tìm thấy sản phẩm: {search_text}.", parent=inv)

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_product(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            database='myDatabase'
        )
        cursor = connection.cursor()

        val = []
        to_delete = []

        if len(self.sel) != 0:
            sure = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xoá các sản phẩm đã chọn?", parent=inv)
            if sure:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)

                    for j in range(len(val)):
                        if j % 8 == 0:
                            to_delete.append(val[j])

                    for k in to_delete:
                        delete = "DELETE FROM inventory WHERE product_id = %s"
                        cursor.execute(delete, (k,))

                    connection.commit()

                messagebox.showinfo("Thành công!!", "Xoá sản phẩm thành công.", parent=inv)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
                self.update_total_value_label()
        else:
            messagebox.showerror("Lỗi!!","Hãy chọn một sản phẩm.", parent=inv)

    def update_product(self):
        if len(self.sel)==1:
            global p_update
            p_update = Toplevel()
            page9 = Update_Product(p_update)
            page9.time()
            p_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global valll
            valll = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    valll.append(j)

            page9.entry1.insert(0, valll[1])
            page9.entry2.insert(0, valll[2])
            page9.entry3.insert(0, valll[4])
            page9.entry4.insert(0, valll[5])
            page9.entry6.insert(0, valll[3])
            page9.entry7.insert(0, valll[6])

        elif len(self.sel)==0:
            messagebox.showerror("Lỗi","Hãy chọn sản phẩm muốn cập nhật.", parent=inv)
        else:
            messagebox.showerror("Lỗi","Can only update one product at a time.", parent=inv)

        p_update.mainloop()

    

    def add_product(self):
        global p_add
        global page4
        p_add = Toplevel()
        page4 = add_product(p_add)
        page4.time()
        p_add.mainloop()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Thoát","Bạn muốn thoát?", parent=inv)
        if sure == True:
            inv.destroy()
            adm.deiconify()

    def ex2(self):
        sure = messagebox.askyesno("Thoát","Bạn muốn thoát??", parent=p_update)
        if sure == True:
            p_update.destroy()
            inv.deiconify()



    def Logout(self):
        sure = messagebox.askyesno("Đăng xuất", "Bạn muốn đăng xuất?")
        if sure == True:
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

class add_product:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Product")

        self.label1 = Label(p_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/add_product2.png")
        self.label1.configure(image=self.img)

        self.clock = Label(p_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(p_add)
        self.entry1.place(relx=0.132, rely=0.296, width=996, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(p_add)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")

        self.r2 = p_add.register(self.testint)

        self.entry3 = Entry(p_add)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry4 = Entry(p_add)
        self.entry4.place(relx=0.132, rely=0.646, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry6 = Entry(p_add)
        self.entry6.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
       

        self.entry7 = Entry(p_add)
        self.entry7.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry7.configure(font="-family {Poppins} -size 12")
        self.entry7.configure(relief="flat")
        self.entry7.configure(validate="key", validatecommand=(self.r2, "%P"))
        self.button1 = Button(p_add)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Thêm""")
        self.button1.configure(command=self.add)

        self.button2 = Button(p_add)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Xoá""")
        self.button2.configure(command=self.clearr)
    
    def add(self):
        
        pqty = self.entry3.get()
        pcat = self.entry2.get()  
        pmrp = self.entry6.get()  
        pname = self.entry1.get()  
        psubcat = self.entry4.get()  
        pcp = self.entry7.get()  
        product_id = random.randint(1000, 9999)

        if pname.strip():
            if pcat.strip():
                if psubcat.strip():
                    if pqty:
                        if pcp:
                                if pmrp:
                                        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='080102',
                                            database='myDatabase'
                                        )
                                        cur = connection.cursor()
                                        # cur = db.cursor()
                                        insert = (
                                                    "INSERT INTO inventory (product_id, product_name, category,stock, product_price,  vendor, vendor_phoneno) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                                                )
                                        cur.execute(insert, [product_id,pname, pcat, int(pqty), psubcat, pmrp, pcp])
                                        connection.commit()
                                        messagebox.showinfo("Thành công!", "Đã thêm sản phẩm.", parent=p_add)
                                        p_add.destroy()
                                        page3.tree.delete(*page3.tree.get_children())
                                        page3.DisplayData()
                                        #############
                                        
                                        p_add.destroy()
                                        
                                else:
                                    messagebox.showerror("Lỗi!", "Sửa thông tin không phù hợp.", parent=p_add)
                        else:
                            messagebox.showerror("Lỗi!", "Sửa thông tin không phù hợp.", parent=p_add)
                    else:
                        messagebox.showerror("Lỗi!", "Sửa thông tin không phù hợp.", parent=p_add)
                else:
                    messagebox.showerror("Lỗi!", "Sửa thông tin không phù hợp.", parent=p_add)
            else:
                messagebox.showerror("Lỗi!", "Sửa thông tin không phù hợp.", parent=p_add)
        else:
            messagebox.showerror("Lỗi!", "Sửa thông tin không phù hợp.", parent=p_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        # self.entry8.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


class Update_Product:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Product")

        self.label1 = Label(p_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_product3.png")
        self.label1.configure(image=self.img)

        self.clock = Label(p_update)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(p_update)
        self.entry1.place(relx=0.132, rely=0.296, width=996, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(p_update)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")

        self.r2 = p_update.register(self.testint)

        self.entry3 = Entry(p_update)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry4 = Entry(p_update)
        self.entry4.place(relx=0.132, rely=0.646, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
       

        self.entry6 = Entry(p_update)
        self.entry6.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry7 = Entry(p_update)
        self.entry7.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry7.configure(font="-family {Poppins} -size 12")
        self.entry7.configure(relief="flat")
       
        self.button1 = Button(p_update)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Cập nhật""")
        self.button1.configure(command=self.update)

        self.button2 = Button(p_update)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Xoá""")
        self.button2.configure(command=self.clearr)

    def update(self):
            pname = self.entry1.get()  # Tên
            pcat = self.entry2.get()   # Loại
            pqty = self.entry3.get()   # Số lượng
            pvender = self.entry4.get()  # Nhà cung cấp
            pprice = self.entry6.get()  # Giá tiền
            pphone = self.entry7.get()  # Số điện thoại

            if pname.strip() and pcat.strip() and pvender.strip() and pprice.strip() and pphone.strip() and pqty.strip():
                try:
                    product_id = valll[0]
                    connection = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='080102',
                        database='myDatabase'
                    )
                    cursor = connection.cursor()
                    update_query = "UPDATE inventory SET product_name = %s, category = %s, product_price = %s, stock = %s, vendor = %s, vendor_phoneno = %s WHERE product_id = %s"
                    cursor.execute(update_query, [pname, pcat, pprice, pqty, pvender, pphone, product_id])
                    connection.commit()
                    messagebox.showinfo("Success!!", "Product successfully updated in inventory.", parent=p_update)
                    valll.clear()
                    Inventory.sel.clear()
                    p_update.destroy()
                    page3.tree.delete(*page3.tree.get_children())
                    page3.DisplayData()
                except Exception as e:
                    messagebox.showerror("Error", "An error occurred: {}".format(str(e)), parent=p_update)
                finally:
                    connection.close()
            else:
                messagebox.showerror("Error!", "Please fill in all the fields.", parent=p_update)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)
    
class add_employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Employee")

        self.label1 = Label(e_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/add_employee_fix.png")
        self.label1.configure(image=self.img)

        self.clock = Label(e_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.r1 = e_add.register(self.testint)
        self.r2 = e_add.register(self.testchar)

        self.entry1 = Entry(e_add)
        self.entry1.place(relx=0.132, rely=0.296, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        

        self.entry2 = Entry(e_add)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")

        self.entry3 = Entry(e_add)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")

        self.entry4 = Entry(e_add)
        self.entry4.place(relx=0.527, rely=0.296, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.button1 = Button(e_add)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Thêm""")
        self.button1.configure(command=self.add)

        self.button2 = Button(e_add)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Xoá""")
        self.button2.configure(command=self.clearr)


    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def add(self):
            ename = self.entry1.get()
            epass = self.entry2.get()
            eadd = self.entry3.get()
            ephone_number = self.entry4.get()

            if ename.strip() and eadd and epass and ephone_number:
                try:
                    emp_id = random_emp_id(7)
                    connection = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='080102',
                        database='myDatabase'
                    )
                    cur = connection.cursor()
                    insert = "INSERT INTO employee(emp_id, name, address, password, phone_number) VALUES (%s, %s, %s, %s, %s)"
                    cur.execute(insert, [emp_id, ename, eadd, epass, ephone_number])
                    connection.commit()
                    messagebox.showinfo("Success!!", "Employee ID: {} successfully added in database.".format(emp_id))
                    self.clearr()
                    page5.tree.delete(*page5.tree.get_children())
                    page5.DisplayData()
                except Exception as e:
                    messagebox.showerror("Error", "An error occurred: {}".format(str(e)))
                finally:
                    connection.close()
            else:
                messagebox.showerror("Validation Error", "Please fill in all the fields.")


    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)

class Update_Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Employee")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_employee_fix.png")
        self.label1.configure(image=self.img)

        self.clock = Label(e_update)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)

        self.entry1 = Entry(e_update)
        self.entry1.place(relx=0.132, rely=0.296, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(e_update)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")

        self.entry3 = Entry(e_update)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")


        self.entry4 = Entry(e_update)
        self.entry4.place(relx=0.527, rely=0.296, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r1, "%P"))
        self.button1 = Button(e_update)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Cập nhật""")
        self.button1.configure(command=self.update)

        self.button2 = Button(e_update)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Xoá""")
        self.button2.configure(command=self.clearr)

    def update(self):
            ename = self.entry1.get()
            epass = self.entry2.get()
            eadd = self.entry3.get()
            ephone_number = self.entry4.get()

            if ename.strip() and eadd and epass and ephone_number:
                try:
                    emp_id = vall[0]
                    connection = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='080102',
                        database='myDatabase'
                    )
                    cur = connection.cursor()
                    update_query = "UPDATE employee SET name = %s, password = %s, address = %s, phone_number = %s WHERE emp_id = %s"
                    cur.execute(update_query, [ename, epass, eadd, ephone_number, emp_id])
                    connection.commit()
                    messagebox.showinfo("Thành công!!", "Cập nhật thông tin thành công.", parent=e_update)
                    vall.clear()
                    page5.tree.delete(*page5.tree.get_children())
                    page5.DisplayData()
                    Employee.sel.clear()
                    e_update.destroy()
                except Exception as e:
                    messagebox.showerror("Error", "An error occurred: {}".format(str(e)))
                finally:
                    connection.close()
            else:
                messagebox.showerror("Lỗi", "Hãy điền đủ thông tin.")

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

class Invoice:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Invoices")
        self.center_window(top)
        self.label1 = Label(invoice)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/invoices_fix.png")
        self.label1.configure(image=self.img)
        
        # Create a custom style with padding
        style = ttk.Style()
        style.configure("Padded.TButton", padding=(10, 5))
        self.message = Label(invoice)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(invoice)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(invoice)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(invoice)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Tìm kiếm""")
        self.button1.configure(command=self.search_inv)

        self.button2 = Button(invoice)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Đăng xuất""")
        self.button2.configure(command=self.Logout)

        self.button3 = ttk.Button(invoice, style="Padded.TButton")
        self.button3.place(relx=0.052, rely=0.47)
        self.button3.configure(text="""Xoá đơn hàng""")
        self.button3.configure(command=self.delete_invoice)

        self.button5 = ttk.Button(invoice, style="Padded.TButton")
        self.button5.place(relx=0.052, rely=0.59)
        self.button5.configure(text="""Danh sách khách hàng""")
        self.button5.configure(command=self.show_customers)

        self.total_revenue_label = Label(invoice)
        self.total_revenue_label.place(relx=0.052, rely=0.65,width=200, height=36)
        self.total_revenue_label.configure(font="-family {Poppins Light} -size 12")
        self.total_revenue_label.configure(foreground="#000000")
        self.total_revenue_label.configure(background="#ffffff")




        self.button7 = ttk.Button(invoice, style="Padded.TButton")
        self.button7.place(relx=0.052, rely=0.53)
        self.button7.configure(text="""Danh sách đơn hàng""")
        self.button7.configure(command=self.DisplayData)


        self.button4 = Button(invoice)
        self.button4.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Thoát""")
        self.button4.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(invoice, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(invoice, orient=VERTICAL)
        self.tree = ttk.Treeview(invoice)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        # self.tree.bind("<Double-1>", self.double_tap)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "name",
                "total",
                "phone",
                "email",
            )
        )

        self.tree.heading("name", text="Tên khách hàng", anchor=W)
        self.tree.heading("total", text="Giá trị đơn hàng", anchor=W)
        self.tree.heading("phone", text="Số điện thoại", anchor=W)
        self.tree.heading("email", text="Email", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=179)
        self.tree.column("#2", stretch=NO, minwidth=0, width=179)
        self.tree.column("#3", stretch=NO, minwidth=0, width=179)
        self.tree.column("#4", stretch=NO, minwidth=0, width=185)
        self.update_total_revenue_label()  #
        self.DisplayData()

    #hamtinhtongthu
    def update_total_revenue_label(self):
        total_value = self.calculate_total_value()
        self.total_revenue_label.configure(text=f"Tổng thu: {total_value} VND")

    def calculate_total_value(self):
        total_value = 0
        try:
            # Kết nối đến database
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='080102',
                database='mydatabase'
            )

            cursor = connection.cursor()

            # Thực hiện truy vấn để lấy dữ liệu
            cursor.execute("SELECT total FROM invoices")

            # Lấy dữ liệu từ truy vấn
            rows = cursor.fetchall()

            # Tính tổng giá trị
            for row in rows:
                price = float(row[0])
                total_value += price

            # In giá trị để kiểm tra
            print(total_value)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Đóng kết nối với database
            if connection.is_connected():
                cursor.close()
                connection.close()

        return total_value
    






    def center_window(self, top):
        top.update_idletasks()
        width = top.winfo_width()
        height = top.winfo_height()
        x = (top.winfo_screenwidth() // 2) - (width // 2)
        y = (top.winfo_screenheight() // 2) - (height // 2)
        top.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    def show_customers(self):
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            database='mydatabase'
        )

        cursor = conn.cursor()

        # Query data from the database
        cursor.execute("SELECT customer_name, SUM(total) as total FROM invoices GROUP BY customer_name")
        rows = cursor.fetchall()

        # Convert data to a list of tuples
        self.data = [(customer_name, total) for customer_name, total in rows]

        # Update TreeView
        self.update_treeview_customer()

        # Close the database connection
        cursor.close()
        conn.close()

    def update_treeview_customer(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        for index, item in enumerate(self.data, start=1):
            pay_total = item[1]  # Giả sử cột "pay_total" là cột thứ 3 (index 2)
            ranking = 1 if pay_total > 100 else 2
            self.tree.insert("", tkinter.END, iid=index, values=(index,) + item + (ranking,))


        # Configure and place the tree
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        # self.tree.bind("<Double-1>", self.double_tap)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "ID","Customer Name", "Paying Total","Ranking"
            )
        )
        self.tree.heading("ID", text="ID", anchor=tkinter.W)
        self.tree.heading("Customer Name", text="Tên khách hàng", anchor=tkinter.W)
        self.tree.heading("Paying Total", text="Tổng giá", anchor=tkinter.W)
        # self.tree.heading("Ranking", text="Số điện thoại", anchor=tkinter.W)
        self.tree.heading("Ranking", text="Ranking", anchor=tkinter.W)

        self.tree.column("#0", stretch=tkinter.NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=tkinter.NO, minwidth=0, width=179)
        self.tree.column("#2", stretch=tkinter.NO, minwidth=0, width=179)
        self.tree.column("#3", stretch=tkinter.NO, minwidth=0, width=179)
        self.tree.column("#3", stretch=tkinter.NO, minwidth=0, width=179)

#----------------------------------------------------------------------------------------------------------------------------
    
#------------------------------------------------------------------------------


    def DisplayData(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            database='myDatabase'
        )
        cursor = connection.cursor()
                # find_user = "SELECT * FROM inventory"
        cursor.execute("SELECT * FROM invoices")

        # cur.execute("SELECT * FROM raw_inventory")
        fetch = cursor.fetchall()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for data in fetch:
            self.tree.insert("", "end", values=(data[1], data[2], data[3], data[4]))
        self.all_items = fetch

        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        # self.tree.bind("<Double-1>", self.double_tap)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "name",
                "total",
                "phone",
                "email",
            )
        )

        self.tree.heading("name", text="Tên khách hàng", anchor=W)
        self.tree.heading("total", text="Tổng giá", anchor=W)
        self.tree.heading("phone", text="Số điện thoại", anchor=W)
        self.tree.heading("email", text="Email", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=179)
        self.tree.column("#2", stretch=NO, minwidth=0, width=179)
        self.tree.column("#3", stretch=NO, minwidth=0, width=179)
        self.tree.column("#4", stretch=NO, minwidth=0, width=179)

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_invoice(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='080102',
            database='myDatabase'
        )
        cursor = connection.cursor()
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Xác nhận", "Bạn muốn xoá đơn hàng?", parent=invoice)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%5==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    # Convert k to integer if it's a string
                    k = str(k)
                    # Xóa các bản ghi liên quan trong bảng invoice_details
                    delete_details = "DELETE FROM invoice_details WHERE customer_name = %s"
                    cursor.execute(delete_details, (k,))
                    connection.commit()

                    print("Đang xóa hóa đơn với customer_name:", k)
                    # Sau đó, xóa bản ghi trong bảng invoices
                    delete_invoice = "DELETE FROM invoices WHERE customer_name = %s"
                    cursor.execute(delete_invoice, (k,))
                    connection.commit()

                messagebox.showinfo("Thành công!!", "Đã xoá đơn hàng.", parent=invoice)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Lỗi!!","Hãy chọn một đơn hàng", parent=invoice)

    def search_inv(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Thành công!!", parent=invoice)
                break
        else: 
            messagebox.showerror("Lỗi!", "Không tìm thấy.", parent=invoice)

    def Logout(self):
        sure = messagebox.askyesno("Đăng xuất", "Bạn muốn đăng xuất?")
        if sure == True:
            invoice.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Thoát","Bạn muốn thoát?", parent=invoice)
        if sure == True:
            invoice.destroy()
            adm.deiconify()

#Contact us
class Statistics:
    def __init__(self, top=None):
        top.geometry("766x468")
        top.resizable(0, 0)
        top.title("Liên hệ")

        
        self.center_window(top)

        self.button4 = ttk.Button(statistic,text="Quay lại",command=self.Exit)
        self.button4.place(x=40,y=14)
        self.contact_us = self.ContactUs(top)
    def center_window(self, top):
        top.update_idletasks()
        width = top.winfo_width()
        height = top.winfo_height()
        x = (top.winfo_screenwidth() // 2) - (width // 2)
        y = (top.winfo_screenheight() // 2) - (height // 2)
        top.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    def Logout(self):
        sure = messagebox.askyesno("Đăng xuất?", "Bạn muốn đăng xuất?")
        if sure == True:
            statistic.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

    def Exit(self):
        sure = messagebox.askyesno("Thoát?","Bạn muốn thoát?", parent=statistic)
        if sure == True:
            statistic.destroy()
            adm.deiconify()

    class ContactUs:
        def __init__(self, top):
            frame_back = ttk.Frame(top)
            frame_back.place(x=20, y=20)

            label = tkinter.Label(top, text="Liên hệ với chúng tôi", foreground="green", font=("Arial", 20, 'bold'))
            label.place(x=40, y=75)

            frame_information = ttk.Frame(top)
            frame_information.place(x=80, y=130, width=600, height=200)

            style = ttk.Style()
            style.configure("Custom.TFrame")
            frame_information["style"] = "Custom.TFrame"

            style = ttk.Style()
            style.configure("White.TLabel", font=("Poppins SemiBold", 13))

            district = ttk.Label(frame_information, text="Địa chỉ: 108 Phố Nguyên Xá, Minh Khai, Bắc Từ Liêm, Hà Nội",
                                 style='White.TLabel')
            district.place(x=10,y=50)

            phone_number = ttk.Label(frame_information, text="Số điện thoại: 0987654321", style='White.TLabel')
            phone_number.place(x=10,y=85)

            gmail = ttk.Label(frame_information, text="Gmail: trieutungvp@gmail.com", style='White.TLabel')
            gmail.place(x=10,y=120)
            image = tkinter.PhotoImage(file="./images/map (1).png")  # Replace with the actual path to your image
            resized_image = image.subsample(1, 1)  # Adjust the subsample values to resize the image
            image_label = tkinter.Label(frame_information, image=resized_image)
            image_label.image = resized_image  # To prevent the image from being garbage collected
            image_label.place(x=470, y=50)           


page1 = login_page(root)
root.bind("<Return>", login_page.login)
root.mainloop()
