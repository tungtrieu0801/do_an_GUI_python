import tkinter as tk
from tkinter import ttk

def setting(root):
    setting_window = tk.Toplevel(root)
    setting_window.title("setting")
    setting_window.geometry("1140x820")

    def close_window_2():
        setting_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(setting_window, text="Back", command=close_window_2)
    back_button.pack()
    label = tk.Label(setting_window, text="Đây là setting", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")
    