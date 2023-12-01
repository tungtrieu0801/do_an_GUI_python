def edit_quantity():
        # Lấy item được chọn trong treeview_selected
        selected_item = treeview_selected.focus()

        if selected_item:
            # Lấy giá trị của cột "Số lượng" của item đang được chọn
            current_quantity = treeview_selected.item(selected_item, "values")[2]

            # Tạo một cửa sổ popup cho phép chỉnh sửa số lượng
            popup_window = tk.Toplevel(sell_window)

            # Tính toán vị trí giữa màn hình cho cửa sổ popup
            window_width = 200
            window_height = 150
            screen_width = sell_window.winfo_screenwidth()
            screen_height = sell_window.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Đặt tọa độ cửa sổ popup
            popup_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Tạo một nhãn và ô văn bản để hiển thị và chỉnh sửa số lượng
            quantity_label = ttk.Label(popup_window, text="Số lượng:")
            quantity_label.pack()

            quantity_entry = ttk.Entry(popup_window)
            quantity_entry.insert(0, current_quantity)
            quantity_entry.pack()

            # Tạo một hàm xử lý sự kiện khi nhấn nút "Lưu"
            def save_quantity():
                new_quantity = quantity_entry.get()

                # Cập nhật giá trị số lượng trong treeview_selected
                treeview_selected.set(selected_item, "Số lượng", new_quantity)

                # Đóng cửa sổ popup
                popup_window.destroy()

            # Tạo nút "Lưu" để lưu giá trị mới của số lượng
            save_button = ttk.Button(popup_window, text="Lưu", command=save_quantity)
            save_button.pack()
    edit_button = ttk.Button(sell_window, text="Chỉnh số lượng", command=edit_quantity)
    edit_button.place(relx=0.84, rely=0.16)