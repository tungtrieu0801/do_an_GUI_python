import mysql.connector

# Kết nối đến MySQL (chắc chắn sửa các thông tin kết nối cho phù hợp)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="080102"
)

# Tạo cơ sở dữ liệu
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS store")

# Sử dụng cơ sở dữ liệu "store"
cur.execute("USE store")

# Tạo bảng "employee"
cur.execute('''CREATE TABLE IF NOT EXISTS employee (
               emp_id VARCHAR(50) PRIMARY KEY,
               password VARCHAR(50))''')

# Tạo bảng "bill"
cur.execute('''CREATE TABLE IF NOT EXISTS bill (
               bill_no VARCHAR(50) PRIMARY KEY,
               date DATE,
               customer_name VARCHAR(100),
               customer_no VARCHAR(20),
               bill_details TEXT)''')

# Tạo bảng "raw_inventory"
cur.execute('''CREATE TABLE IF NOT EXISTS raw_inventory (
               product_id INT AUTO_INCREMENT PRIMARY KEY,
               product_name VARCHAR(100),
               product_cat VARCHAR(100),
               product_subcat VARCHAR(100),
               mrp DECIMAL(10, 2),
               stock INT)''')

# Đồng bộ hóa các thay đổi với cơ sở dữ liệu
conn.commit()

# Đóng kết nối
conn.close()
