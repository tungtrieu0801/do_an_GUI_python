
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
