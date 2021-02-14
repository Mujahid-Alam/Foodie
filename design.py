import tkinter
from tkinter import *

root = Tk()
root.geometry("1500x700")
root.title("Foodie")


#   top     #
Top = Frame(root, width=1600,height=200)
Top.pack(side=TOP)


Left = Frame(root,width=900,height=700)
Left.pack(side=LEFT,padx=50)

Right = Frame(root, width=600,height=700)
Right.pack(side=LEFT,padx=50)

brand = Label(Top, text="FOODIE",font=("arial",25,"bold"),fg="steel Blue",anchor="n")
brand.grid(row=0,column=0)

slug = Label(Top, text="Taste the world",font=("arail",15),fg="grey",anchor="n")
slug.grid(row=1,column=0)

############################### work 
totalPrice = 0
gst=0
finalAmount=0

expression=""           #CLEAR BUTTON STARTS HERE

def clearitem():
    global expression
    expression="0"
    eggroll.set(expression)
    chowmin.set(expression)
    momos.set(expression)
    idli.set(expression)
    dosa.set(expression)
    burger.set(expression)
    puha.set(expression)
    roll.set(expression)
    sweeti.set(expression)
    corn.set(expression)
    samosa.set(expression)
    litti.set(expression)       
    totalValue.set(expression)
    taxValue.set(expression)
    orderValue.set(expression)
    finalValue.set(expression)      #CLEAR BUTTON ENDS HERE.

def TotalOrder():
    global totalPrice
    global finalAmount
    global gst
    eggrollTotal = int(eggroll.get()) * 25
    chowminTotal = int(chowmin.get()) * 30
    momosTotal = int(momos.get()) * 40
    idliTotal = int(idli.get()) * 37
    dosaTotal = int(dosa.get()) * 50
    burgerTotal = int(burger.get()) * 55
    puhaTotal = int(puha.get()) * 60
    rollTotal = int(roll.get()) * 70
    sweetiTotal = int(sweeti.get()) * 54
    cornTotal = int(corn.get()) * 44
    samosaTotal = int(samosa.get()) * 11
    littiTotal = int(litti.get()) * 14
  

    totalPrice = eggrollTotal + chowminTotal+momosTotal+idliTotal+dosaTotal+burgerTotal+puhaTotal+rollTotal+sweetiTotal+cornTotal+samosaTotal+littiTotal

    gst = totalPrice * 0.18
    finalAmount = gst + totalPrice
    
    totalValue.set(totalPrice)
    taxValue.set(gst)
    finalValue.set(finalAmount)

def price():
    child=Tk()

    child.geometry("500x400")
    child.title("Recipie Rate List")

    eggroll=Label(child,text="Eggroll")
    eggroll_price=Label(child,text="25/-")

    chowmin=Label(child,text='Chowmin')
    chowmin_price=Label(child,text='30/-')

    idli=Label(child,text='Idli')
    idli_price=Label(child,text='30/-')

    dosa=Label(child,text='Dosa')
    dosa_price=Label(child, text='50/-')

    burger=Label(child,text='Burger')
    burger_price=Label(child,text='40/-')

    puha=Label(child,text='Puha')
    puha_price=Label(child,text='30/-')

    roll=Label(child,text='Roll')
    roll_price=Label(child,text='25/-')

    sweeti=Label(child,text='Sweeti')
    sweeti_price=Label(child,text='20/-')

    corn=Label(child,text='Corn')
    corn_price=Label(child,text='20/-')

    samosa=Label(child,text='Samosa')
    samosa_price=Label(child,text='10/-')

    litti=Label(child,text='Litti')
    litti_price=Label(child,text='8/-')


    eggroll.grid(row=0,column=0)
    eggroll_price.grid(row=0,column=1)

    chowmin.grid(row=1,column=0)
    chowmin_price.grid(row=1,column=1)

    idli.grid(row=2,column=0)
    idli_price.grid(row=2,column=1)

    dosa.grid(row=3,column=0)
    dosa_price.grid(row=3,column=1)

    burger.grid(row=4,column=0)
    burger_price.grid(row=4,column=1)

    puha.grid(row=5,column=0)
    puha_price.grid(row=5,column=1)

    roll.grid(row=6,column=0)
    roll_price.grid(row=6,column=1)

    sweeti.grid(row=7,column=0)
    sweeti_price.grid(row=7,column=1)

    corn.grid(row=8,column=0)
    corn_price.grid(row=8,column=1)

    samosa.grid(row=9,column=0)
    samosa_price.grid(row=9,column=1)

    litti.grid(row=10,column=0)
    litti_price.grid(row=10,column=1)



    
    child.mainloop()



def closeApp():
    root.destroy()
##################  recipie     ############



eggroll = StringVar()
chowmin = StringVar()
momos = StringVar()
idli = StringVar()
dosa = StringVar()
burger = StringVar()
puha = StringVar()
roll = StringVar()
sweeti = StringVar()
corn = StringVar()
samosa = StringVar()
litti =   StringVar()




eggroll.set("0")
chowmin.set("0")
momos.set("0")
idli.set("0")
dosa.set("0")
burger.set("0")
puha.set("0")
roll.set("0")
sweeti.set("0")
corn.set("0")
samosa.set("0")
litti.set("0")

eggroll_label = Label(Left, text="Eng Roll",fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
chowmin_label = Label(Left, text= "Chowmin",fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
momos_label = Label(Left, text = "Momos", fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
idli_label = Label(Left, text="Idli", fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
dosa_label = Label(Left, text="Dosa", fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
burger_label = Label(Left, text="Burger", fg="steel blue",font=("Helvtica",19,"bold"),bd=10)

#
puha_label = Label(Left, text="Puha",fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
roll_label = Label(Left, text= "Roll",fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
sweeti_label = Label(Left, text = "Sweeti", fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
corn_label = Label(Left, text="Corn", fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
samosa_label = Label(Left, text="Samosa", fg="steel blue",font=("Helvtica",19,"bold"),bd=10)
litti_label = Label(Left, text="Litti", fg="steel blue",font=("Helvtica",19,"bold"),bd=10)



eggroll_entry = Entry(Left,font=("arial",16),bd=6,textvariable=eggroll,justify=RIGHT)
chowmin_entry = Entry(Left,font=("arial",16),bd=6,textvariable=chowmin,justify=RIGHT)
momos_entry = Entry(Left,font=("arial",16),bd=6,textvariable=momos,justify=RIGHT)
idli_entry = Entry(Left,font=("arial",16),bd=6,textvariable=idli,justify=RIGHT)
dosa_entry = Entry(Left,font=("arial",16),bd=6,textvariable=dosa,justify=RIGHT)
burger_entry = Entry(Left,font=("arial",16),bd=6,textvariable=burger,justify=RIGHT)

#
puha_entry = Entry(Left,font=("arial",16),bd=6,textvariable=puha,justify=RIGHT)
roll_entry = Entry(Left,font=("arial",16),bd=6,textvariable=roll,justify=RIGHT)
sweeti_entry = Entry(Left,font=("arial",16),bd=6,textvariable=sweeti,justify=RIGHT)
corn_entry = Entry(Left,font=("arial",16),bd=6,textvariable=corn,justify=RIGHT)
samosa_entry = Entry(Left,font=("arial",16),bd=6,textvariable=samosa,justify=RIGHT)
litti_entry = Entry(Left,font=("arial",16),bd=6,textvariable=litti,justify=RIGHT)



eggroll_label.grid(row=0,column=0)
eggroll_entry.grid(row=0,column=1)

chowmin_label.grid(row=0,column=2)
chowmin_entry.grid(row=0,column=3)

momos_label.grid(row=1,column=0)
momos_entry.grid(row=1,column=1)

idli_label.grid(row=1,column=2)
idli_entry.grid(row=1,column=3)

dosa_label.grid(row=2,column=0)
dosa_entry.grid(row=2,column=1)

burger_label.grid(row=2,column=2)
burger_entry.grid(row=2,column=3)
#
puha_label.grid(row=3,column=0)
puha_entry.grid(row=3,column=1)

roll_label.grid(row=3,column=2)
roll_entry.grid(row=3,column=3)

sweeti_label.grid(row=4,column=0)
sweeti_entry.grid(row=4,column=1)

corn_label.grid(row=4,column=2)
corn_entry.grid(row=4,column=3)

samosa_label.grid(row=5,column=0)
samosa_entry.grid(row=5,column=1)

litti_label.grid(row=5,column=2)
litti_entry.grid(row=5,column=3)


##############  Buttons


total = Button(Left, text="Total",font=("comic sans ms",20,"bold"),bg="green",bd=7,width=10,height=1,command = TotalOrder)
total.grid(row=6,column=0)

price = Button(Left, text="Price",font=("comic sans ms",20,"bold"),bg="sky blue",bd=7,width=10,height=1,command=price)
price.grid(row=6,column=1)

clear = Button(Left, text="Clear",font=("comic sans ms",20,"bold"),bg="sky blue",bd=7,width=10,height=1,command=clearitem)
clear.grid(row=6,column=2)

exit = Button(Left, text="Exit",font=("comic sans ms",20,"bold"),bg="blue",bd=7,width=10,height=1,command=closeApp)
exit.grid(row=6,column=3)


########## Right side work
totalValue = StringVar()
taxValue = StringVar()
orderValue = StringVar()
finalValue =StringVar()

totalValue.set("0")
taxValue.set("0")
orderValue.set("0")
finalValue.set("0")


totalEntry = Entry(Right, justify=RIGHT,width=30,bd=7,textvariable = totalValue)
totalLabel = Label(Right, text="Total Amount",anchor="w")

taxEntry = Entry(Right, justify=RIGHT,width=30,bd=7,textvariable = taxValue)
taxLabel = Label(Right, text="TAX GST (18%)",anchor="w")

orderEntry = Entry(Right, justify=RIGHT,width=30,bd=7,textvariable = orderValue)
orderLabel = Label(Right, text="Order No",anchor="w")

finalEntry = Entry(Right, justify=RIGHT,width=30,bd=7,textvariable = finalValue)
finalLabel = Label(Right, text="Payable Amount",anchor="w")

totalLabel.grid(row=0,column=0)
totalEntry.grid(row=1,column=0)

taxLabel.grid(row=2,column=0)
taxEntry.grid(row=3,column=0)

orderLabel.grid(row=4,column=0)
orderEntry.grid(row=5,column=0)

finalLabel.grid(row=6,column=0)
finalEntry.grid(row=7,column=0)
                

#root.attributes("-fullscreen",True)
root.mainloop()
