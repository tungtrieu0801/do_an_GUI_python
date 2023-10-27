
import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

db=mysql.connector.connect(user="root",password='vantung2002',host='localhost',database='qlsp')
#windown
r=tk.Tk()
r.title('SN_PHAM')
r.geometry('800x600')
r.resizable(False,False)
frm=Frame(r)
frm.pack(side=tk.LEFT)

#Load table
query='select * from ten_san_pham'
q_show=db.cursor()
q_show.execute(query)
rows=q_show.fetchall()

#Tree view
tree=ttk.Treeview(frm,columns=(1,2,3,4),show='headings',height='5')
tree.heading(1,text='Tên sản phẩm')
tree.heading(2,text='Loại sản phẩm')
tree.heading(3,text='Số lượng')
tree.heading(4,text='Giá tiền')

#Load db
for i in rows:
    tree.insert('','end',iid=i[0],values=i)
tree.pack()

#Delete row
def delete():
    selected=tree.selection()[0]
    query= 'delete from ten_san_pham where ten_san_pham=%s'
    #Data is tuple
    data=(selected,)
    q_del=db.cursor()
    q_del.execute(query,data)
    db.commit()
    tree.delete(selected)

#update row
# Tạo các trường nhập liệu
entry_name = tk.Entry(frm)
entry_name.pack()

entry_type = tk.Entry(frm)
entry_type.pack()

entry_quantity = tk.Entry(frm)
entry_quantity.pack()

entry_price = tk.Entry(frm)
entry_price.pack()

# Hàm xử lý sự kiện thêm sản phẩm
def add_product():
    # Lấy thông tin từ các trường nhập liệu
    product_name = entry_name.get()
    product_type = entry_type.get()
    product_quantity = entry_quantity.get()
    product_price = entry_price.get()

    # Thực hiện câu lệnh SQL để thêm sản phẩm vào cơ sở dữ liệu
    query = "INSERT INTO ten_san_pham (TEN_SAN_PHAM, TYPE, QUANTITY, PRICE) VALUES (%s, %s, %s, %s)"
    product_data = (product_name, product_type, product_quantity, product_price)
    cursor = db.cursor()
    cursor.execute(query, product_data)
    db.commit()

    # Xóa dữ liệu đã nhập trong các trường nhập liệu
    entry_name.delete(0, tk.END)
    entry_type.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)
b2 = tk.Button(frm, text='Thêm sản phẩm', bg='green', width=20, command=add_product)
b2.pack()



b1=tk.Button(frm,text='Delete',bg='red',width=20,command=delete)
b1.pack()


r.mainloop()



#QUERY
#code= ' create  database `qlsp` ;  '
#create table
#code1="INSERT INTO `ten_san_pham` (`TEN_SAN_PHAM`,`TYPE`, `PRICE`, `QUANTITY` , `PRICE`) VALUES (%s,%s,%s,%s);"
#val=[]
    
    

#delête row
#code2= "DELETE FROM  `ten_san_pham` WHERE  `TEN_SAN_PHAM`='Bim Bim bí đỏ'"    
#RUN

#mycursor=db.cursor()
#mycursor.execute(code2) // xoa san pham
#for item in val:
    #mycursor.execute(code1,item)
#update db
#db.commit()
