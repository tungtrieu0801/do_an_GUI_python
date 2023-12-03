import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TreeView Example")

        # TreeView
        self.tree = ttk.Treeview(root)

        # Define columns
        self.tree["columns"] = ("Column1", "Column2")

        # Configure columns
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Column1", anchor=tk.W, width=100)
        self.tree.column("Column2", anchor=tk.W, width=100)

        # Add headings
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Column1", text="Column 1", anchor=tk.W)
        self.tree.heading("Column2", text="Column 2", anchor=tk.W)

        # Button 1
        btn_show_info = tk.Button(root, text="Show Name and Age", command=self.show_name_and_age)
        btn_show_info.pack(pady=10)

        # Button 2
        btn_show_date = tk.Button(root, text="Show Date and Month", command=self.show_date_and_month)
        btn_show_date.pack(pady=10)

        # Initialize data
        self.data = [
            ("John", 25),
            ("Alice", 30),
            ("Bob", 22),
        ]

        # Add sample data
        self.update_treeview()

    def show_name_and_age(self):
        # Update data for Name and Age
        self.data = [
            ("John", 25),
            ("Alice", 30),
            ("Bob", 22),
        ]
        self.update_treeview()

    def show_date_and_month(self):
        # Update data for Date and Month
        self.data = [
            ("01", "January"),
            ("15", "February"),
            ("20", "March"),
        ]
        self.update_treeview()

    def update_treeview(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add updated data to the TreeView
        for item in self.data:
            self.tree.insert("", tk.END, values=item)

        self.tree.pack(expand=tk.YES, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
