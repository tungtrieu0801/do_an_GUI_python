import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

def draw_bar_chart():
    # Dữ liệu mẫu (tên sản phẩm và số lượng bán ra)
    product_names = ["Sản phẩm A", "Sản phẩm B", "Sản phẩm C", "Sản phẩm D"]
    quantity_sold = [10, 25, 15, 30]

    # Vẽ biểu đồ cột
    plt.bar(product_names, quantity_sold, color='blue')

    # Hiển thị biểu đồ
    plt.show()

def populate_treeview():
    # Xóa dữ liệu cũ trên Treeview (nếu có)
    for row in tree.get_children():
        tree.delete(row)

    # Dữ liệu mẫu (tên sản phẩm và số lượng bán ra)
    product_names = ["Sản phẩm A", "Sản phẩm B", "Sản phẩm C", "Sản phẩm D"]
    quantity_sold = [10, 25, 15, 30]

    # Thêm dữ liệu vào Treeview
    for i in range(len(product_names)):
        tree.insert("", i, values=(product_names[i], quantity_sold[i]))

# Tạo cửa sổ
root = tk.Tk()
root.title("Thống Kê Số Lượng Bán Ra")

# Tạo nút "Vẽ Biểu Đồ"
draw_chart_button = ttk.Button(root, text="Vẽ Biểu Đồ", command=draw_bar_chart)
draw_chart_button.pack(pady=10)

# Tạo Treeview
tree = ttk.Treeview(root, columns=("Product", "Quantity"), show="headings")
tree.heading("Product", text="Tên Sản Phẩm")
tree.heading("Quantity", text="Số Lượng Bán Ra")
tree.pack(pady=10)

# Tạo nút "Hiển Thị Thông Tin Trên Treeview"
show_info_button = ttk.Button(root, text="Hiển Thị Thông Tin", command=populate_treeview)
show_info_button.pack(pady=10)

# Chạy ứng dụng
root.mainloop()
