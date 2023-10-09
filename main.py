from tkinter import *
from tkinter import messagebox
import random
#function part
billnumber = random.randint(500,1000)

def bill_area():
    texteare.delete(1.0, END)
    if nameEntry.get =='' or phoneEntry.get()=='':
        messagebox.showerror('ERROR', 'ENTER ALL INFORMATION ABOUT CUSTOMER')
    elif cometicpriceEntry.get()=='':
        messagebox.showerror('ERROR', 'NO PRODUCT IS SELECTED')
    elif cometicpriceEntry.get()=='0':
        messagebox.showerror('ERROR', 'NO PRODUCT IS SELECTED')
    else:
        texteare.insert(END, '\t\tWelcome Customer\n')
        texteare.insert(END, f'\nBill Number: {billnumber}\n')
        texteare.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        texteare.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        texteare.insert(END, '\n========================================')
        texteare.insert(END, 'Product\t\tQuantity\t\tPrice')
        texteare.insert(END, '\n========================================')
        if bathsoapEntry.get()!='0':
            texteare.insert(END,f'\nBath soap\t\t{bathsoapEntry.get()}\t\t{soapprice}')
        if facecreamEntry.get()!='0':
            texteare.insert(END,f'\nFace Scream\t\t{facecreamEntry.get()}\t\t{facecreamprice}')
        if facewashEntry.get()!='0':
            texteare.insert(END,f'\nFace Wash\t\t{facewashEntry.get()}\t\t{facewashprice}')
        if hairgelEntry.get()!='0':
            texteare.insert(END,f'\nHair Gel\t\t{hairgelEntry.get()}\t\t{hairgelprice}')
        if hairsprayEntry.get()!='0':
            texteare.insert(END,f'\nHair Spray\t\t{hairsprayEntry.get()}\t\t{hairsprayprice}')
        if bodylotitionEntry.get()!='0':
            texteare.insert(END,f'\nBody lotion\t\t{bodylotitionEntry.get()}\t\t{bodylotitionprice}')
        texteare.insert(END, "\n========================================")
        if CosmetictaxEntry.get()!='0':
            texteare.insert(END,f'\nCosmetic tax\t\t{CosmetictaxEntry.get()}')
        texteare.insert(END,f'\nTotal Bill\t\t{totalbill}')
def total():
    global soapprice, facecreamprice, facewashprice, hairgelprice, hairsprayprice, bodylotitionprice,totalbill
    soapprice  = int(bathsoapEntry.get())*20
    facecreamprice = int(facecreamEntry.get())*50
    facewashprice = int(facewashEntry.get())*100
    hairgelprice = int(hairgelEntry.get())*150
    hairsprayprice = int(hairsprayEntry.get())*80
    bodylotitionprice = int(bodylotitionEntry.get()) *60
    totalprice = soapprice + facecreamprice + facewashprice + hairgelprice + hairsprayprice + bodylotitionprice
    cometicpriceEntry.delete(0, END)
    cometicpriceEntry.insert(0,totalprice)
    cometictax = totalprice *0.12
    CosmetictaxEntry.delete(0,END)
    CosmetictaxEntry.insert(0,cometictax)

    totalbill = totalprice + cometictax

root = Tk()
root.title("Retail Billing system")
root.geometry("1305x708")

headingLabel = Label(root, text='Retail Billing System', font=("Arial", 30,'bold' ), bg='gray20',fg='gold', relief=RIDGE)
headingLabel.pack(fill=X)
#------------------------------------------------------------
customer_details_frame = LabelFrame(root, text="Customer Detail", font=('Arial', 15, 'bold'), fg='gold', bd=8, relief=GROOVE, bg='gray20')
customer_details_frame.pack(fill=X, pady=5)

nameLabel = Label(customer_details_frame, text='Name', font=('Arial', 15, 'bold'), bg='gray20', fg='white', bd=5)
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_details_frame, font=('Arial', 15, 'bold'),relief=GROOVE, bd=5)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_details_frame, text='Phone', font=('Arial', 15, 'bold'), bg='gray20', fg='white')
phoneLabel.grid(row=0, column=2, padx=20)

phoneEntry = Entry(customer_details_frame, font=('Arial', 15, 'bold'),relief=GROOVE, bd=5)
phoneEntry.grid(row=0, column=3, padx=8)


bil_numberLabel = Label(customer_details_frame, text='Bill Number', font=('Arial', 15, 'bold'), bg='gray20', fg='white')
bil_numberLabel.grid(row=0, column=4, padx=20)

bil_numberEntry = Entry(customer_details_frame, font=('Arial', 15, 'bold'),relief=GROOVE, bd=5)
bil_numberEntry.grid(row=0, column=5, padx=8)


searchButton = Button(customer_details_frame, text='Add new product',font=('Arial', 12, 'bold'),relief=GROOVE, bd=5,width=15)
searchButton.grid(row=0, column=6, padx=6)

#-----------------------------------------------------------------------------------------------------------------------------------#
productsFrame = Frame(root)
productsFrame.pack()

cosmeticFrame = LabelFrame(productsFrame, text="Cosmetics", font=('Arial', 15, 'bold'), fg='gold', bd=8, relief=GROOVE, bg='gray20' )
cosmeticFrame.grid(row=0, column=0,padx=5)

bathsoapLabel = Label(cosmeticFrame, text="Bath soap",  font=('Arial', 15, 'bold'), fg='white', bg='gray20', bd=5)
bathsoapLabel.grid(row=0, column=0, pady=10, sticky=W, padx=10)
bathsoapEntry = Entry(cosmeticFrame,  font=('Arial', 15, 'bold'), width=14,bd=5)
bathsoapEntry.grid(row=0, column=1,pady=10, padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel = Label(cosmeticFrame, text="Face cream",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
facecreamLabel.grid(row=1, column=0,pady=10, sticky=W, padx=10)
facecreamEntry = Entry(cosmeticFrame,  font=('Arial', 15, 'bold'),width=14, bd=5)
facecreamEntry.grid(row=1, column=1,pady=10, padx=10)
facecreamEntry.insert(0,0)

facewashLabel = Label(cosmeticFrame, text="Face wash",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
facewashLabel.grid(row=2, column=0,pady=10, sticky=W, padx=10)
facewashEntry = Entry(cosmeticFrame,  font=('Arial', 15, 'bold'),width=14, bd=5)
facewashEntry.grid(row=2, column=1,pady=10, padx=10)
facewashEntry.insert(0,0)

hairsprayLabel = Label(cosmeticFrame, text="Hair spray",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
hairsprayLabel.grid(row=3, column=0, pady=10, sticky=W, padx=10)
hairsprayEntry = Entry(cosmeticFrame,  font=('Arial', 15, 'bold'), width=14, bd=5)
hairsprayEntry.grid(row=3, column=1,pady=10, padx=10)
hairsprayEntry.insert(0,0)


hairgelLabel = Label(cosmeticFrame, text="Hair gel",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
hairgelLabel.grid(row=4, column=0,pady=10, sticky=W, padx=10)
hairgelEntry = Entry(cosmeticFrame,  font=('Arial', 15, 'bold'),width=14, bd=5)
hairgelEntry.grid(row=4, column=1,pady=10, padx=10)
hairgelEntry.insert(0,0)

bodylotitionLabel = Label(cosmeticFrame, text="Body lotition",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
bodylotitionLabel.grid(row=5, column=0,pady=10, sticky=W, padx=10)
bodylotitionEntry = Entry(cosmeticFrame,  font=('Arial', 15, 'bold'),width=14, bd=5)
bodylotitionEntry.grid(row=5, column=1,pady=10, padx=10)
bodylotitionEntry.insert(0,0)

# 2

gorceryFrame = LabelFrame(productsFrame, text="Grocery", font=('Arial', 15, 'bold'), fg='gold', bd=8, relief=GROOVE, bg='gray20' )
gorceryFrame.grid(row=0, column=1, pady=5)

riceLabel = Label(gorceryFrame, text="Rice",  font=('Arial', 15, 'bold'), fg='white', bg='gray20', bd=5)
riceLabel.grid(row=0, column=0, pady=10, sticky=W, padx=10)
riceEntry = Entry(gorceryFrame,  font=('Arial', 15, 'bold'), width=14,bd=5)
riceEntry.grid(row=0, column=1,pady=10, padx=10)

oilLabel = Label(gorceryFrame, text="Oil",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
oilLabel.grid(row=1, column=0,pady=10, sticky=W, padx=10)
oilEntry = Entry(gorceryFrame,  font=('Arial', 15, 'bold'),width=14, bd=5)
oilEntry.grid(row=1, column=1,pady=10, padx=10)

dallLabel = Label(gorceryFrame, text="Dall",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
dallLabel.grid(row=2, column=0,pady=10, sticky=W, padx=10)
dallEntry = Entry(gorceryFrame,  font=('Arial', 15, 'bold'),width=14, bd=5)
dallEntry.grid(row=2, column=1,pady=10, padx=10)

WheatLabel = Label(gorceryFrame, text="Wheat",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
WheatLabel.grid(row=3, column=0, pady=10, sticky=W, padx=10)
WheatEntry = Entry(gorceryFrame,  font=('Arial', 15, 'bold'), width=14, bd=5)
WheatEntry.grid(row=3, column=1,pady=10, padx=10)

sugarLabel = Label(gorceryFrame, text="Surgar",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
sugarLabel.grid(row=4, column=0,pady=10, sticky=W, padx=10)
sugarEntry = Entry(gorceryFrame,  font=('Arial', 15, 'bold'),width=14, bd=5)
sugarEntry.grid(row=4, column=1,pady=10, padx=10)

teaLabel = Label(gorceryFrame, text="Tea",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
teaLabel.grid(row=5, column=0,pady=10, sticky=W, padx=10)
teaEntry = Entry(gorceryFrame,  font=('Arial', 15, 'bold'),width=14, bd=5)
teaEntry.grid(row=5, column=1,pady=10, padx=10)

#3

coldDrinks = LabelFrame(productsFrame, text="Cosmetics", font=('Arial', 15, 'bold'), fg='gold', bd=8, relief=GROOVE, bg='gray20' )
coldDrinks.grid(row=0, column=2, pady=5)

mazzaLabel = Label(coldDrinks, text="Mazza",  font=('Arial', 15, 'bold'), fg='white', bg='gray20', bd=5)
mazzaLabel.grid(row=0, column=0, pady=10, sticky=W, padx=10)
mazzaEntry = Entry(coldDrinks,  font=('Arial', 15, 'bold'), width=14,bd=5)
mazzaEntry.grid(row=0, column=1,pady=10, padx=10)

pepsiLabel = Label(coldDrinks, text="Pepsi",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
pepsiLabel.grid(row=1, column=0,pady=10, sticky=W, padx=10)
pepsiEntry = Entry(coldDrinks,  font=('Arial', 15, 'bold'),width=14, bd=5)
pepsiEntry.grid(row=1, column=1,pady=10, padx=10)

spriteLabel = Label(coldDrinks, text="Sprite",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
spriteLabel.grid(row=2, column=0,pady=10, sticky=W, padx=10)
spriteEntry = Entry(coldDrinks,  font=('Arial', 15, 'bold'),width=14, bd=5)
spriteEntry.grid(row=2, column=1,pady=10, padx=10)

dewLabel = Label(coldDrinks, text="Dew",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
dewLabel.grid(row=3, column=0, pady=10, sticky=W, padx=10)
dewEntry = Entry(coldDrinks,  font=('Arial', 15, 'bold'), width=14, bd=5)
dewEntry.grid(row=3, column=1,pady=10, padx=10)

frootiLabel = Label(coldDrinks, text="Frooti",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
frootiLabel.grid(row=4, column=0,pady=10, sticky=W, padx=10)
frootiEntry = Entry(coldDrinks,  font=('Arial', 15, 'bold'),width=14, bd=5)
frootiEntry.grid(row=4, column=1,pady=10, padx=10)

cocacolaLabel = Label(coldDrinks, text="Coca Cola",  font=('Arial', 15, 'bold'), fg='white', bg='gray20')
cocacolaLabel.grid(row=5, column=0,pady=10, sticky=W, padx=10)
cocacolaEntry = Entry(coldDrinks,  font=('Arial', 15, 'bold'),width=14, bd=5)
cocacolaEntry.grid(row=5, column=1,pady=10, padx=10)

#------------------------------------------------------------------------------------#
billFrame = Frame(productsFrame, relief=GROOVE)
billFrame.grid(row=0, column=3)

scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
billareaLabel = Label(billFrame, text='Bill Area',font=('Arial', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

texteare = Text(billFrame, height=21, width=40, yscrollcommand=scrollbar.set)
texteare.pack()
scrollbar.config(command=texteare.yview)



#-------------------------------------------------------------------------------------#
billmenuFrame = LabelFrame(root, text='Bill Menu',font=('Arial', 15, 'bold'),fg='white', bg='gray20')
billmenuFrame.pack()

cometicpriceFrame = Label(billmenuFrame, text='Cometic Price',font=('Arial', 15, 'bold'),fg='white', bg='gray20')
cometicpriceFrame.grid(row=0, column=0, padx=10, pady=9, sticky=W)
cometicpriceEntry = Entry(billmenuFrame,font=('Arial', 15, 'bold'),width=10, bd=5)
cometicpriceEntry.grid(row=0, column=1 ,padx=10, pady=9)

groceryFrame = Label(billmenuFrame, text='Grocery Price',font=('Arial', 15, 'bold'),fg='white', bg='gray20')
groceryFrame.grid(row=1, column=0, padx=10, pady=9, sticky=W)
groceryEntry = Entry(billmenuFrame,font=('Arial', 15, 'bold'),width=10, bd=5)
groceryEntry.grid(row=1, column=1 ,padx=10, pady=9)

drinkFrame = Label(billmenuFrame, text='Cold Drink Price',font=('Arial', 15, 'bold'),fg='white', bg='gray20')
drinkFrame.grid(row=2, column=0, padx=10, pady=9, sticky=W)
drinkEntry = Entry(billmenuFrame,font=('Arial', 15, 'bold'),width=10, bd=5)
drinkEntry.grid(row=2, column=1 ,padx=10, pady=9)

CosmetictaxFrame = Label(billmenuFrame, text='Cosmetic tax',font=('Arial', 15, 'bold'),fg='white', bg='gray20')
CosmetictaxFrame.grid(row=0, column=2, padx=10, pady=9, sticky=W)
CosmetictaxEntry = Entry(billmenuFrame,font=('Arial', 15, 'bold'),width=10, bd=5)
CosmetictaxEntry.grid(row=0, column=3 ,padx=10, pady=9)

grocerytaxFrame = Label(billmenuFrame, text='Grocery tax',font=('Arial', 15, 'bold'),fg='white', bg='gray20')
grocerytaxFrame.grid(row=1, column=2, padx=10, pady=9, sticky=W)
grocerytaxEntry = Entry(billmenuFrame,font=('Arial', 15, 'bold'),width=10, bd=5)
grocerytaxEntry.grid(row=1, column=3 ,padx=10, pady=9)

drinktaxFrame = Label(billmenuFrame, text='Cold Drink tax',font=('Arial', 15, 'bold'),fg='white', bg='gray20')
drinktaxFrame.grid(row=2, column=2, padx=10, pady=9, sticky=W)
drinktaxEntry = Entry(billmenuFrame,font=('Arial', 15, 'bold'),width=10, bd=5)
drinktaxEntry.grid(row=2, column=3 ,padx=10, pady=9)

#--------------------------------#
buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE, bg='white')
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total' ,font=('Arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=30, padx=10)

billButton = Button(buttonFrame, text='Bill' ,font=('Arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=30, padx=10)

emailButton = Button(buttonFrame, text='Email' ,font=('Arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10)
emailButton.grid(row=0, column=2, pady=30, padx=10)

printButton = Button(buttonFrame, text='Print' ,font=('Arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10)
printButton.grid(row=0, column=3, pady=30, padx=10)

clearButton = Button(buttonFrame, text='Clear' ,font=('Arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10)
clearButton.grid(row=0, column=4, pady=30, padx=10)

    





root.mainloop()