import os
from tkinter import *
from tkinter import messagebox

main = Tk()
# main.geometry("1366x768")

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
    
window_width = 1366  # Thay đổi kích thước theo nhu cầu
window_height = 768  # Thay đổi kích thước theo nhu cầu
# Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

    # Đặt vị trí cửa sổ
main.geometry(f"{window_width}x{window_height}+{x}+{y}")
main.resizable(width=False, height=False)
main.title("Home")
main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=146, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)

main.mainloop()
