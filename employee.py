import sqlite3
import re
import os
import random
import mysql.connector
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
#============================================
import subprocess
import sell

root = Tk()

root.geometry("1366x768")
root.title("Retail Manager")


user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
new_user = StringVar()
new_passwd = StringVar()


cust_name = StringVar()
cust_num = StringVar()
cust_new_bill = StringVar()
cust_search_bill = StringVar()
bill_date = StringVar()




def random_bill_number(stringLength):
    lettersAndDigits = string.ascii_letters.upper() + string.digits
    strr=''.join(random.choice(lettersAndDigits) for i in range(stringLength-2))
    return ('BB'+strr)





class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Retail Manager(ADMIN)")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/employee_login.png")
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
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(command=self.login)
        
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
            messagebox.showinfo("Login Page", "The login is successful.")
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)
            root.withdraw()     
            # subprocess.run(["python", "employee1.py"])   
            sell.sell(root)
            # adm = Toplevel()
                #page2.time()
            root.protocol("WM_DELETE_WINDOW", exitt)

        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            page1.entry2.delete(0, END)
def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()
page1 = login_page(root)
login_page(root)
root.bind("<Return>", login_page.login)
root.mainloop()