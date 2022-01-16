import tkinter
from datetime import datetime
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from sqlalchemy import create_engine
import tkinter as tk
from tkinter.ttk import *
from decimal import Decimal
from dateutil import parser
from random import seed
import random
from random import randint
host="localhost"
user="root"
password="efood_team27"
database="ifood"
port=3306


global item_rest
global rate_text
global logged_user
#


###################LOGIN#####################

# connecting to the database

connectiondb = mysql.connect(
  host=host,
  user=user,
  password=password,
  database=database,
  port=port
)
cursordb = connectiondb.cursor()
 

def login():
    root.destroy()
    global root2
    root2 = Tk()
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(background="white")

    global username_verification
    global password_verification

    insertLabel = Label(root2, text='Insert login account data', font=('bold', 10))
    insertLabel.place(x=100, y=120)

    username_verification = StringVar()
    password_verification = StringVar()

    mobileLabel = Label(root2, text='Mobile Phone :', font=('bold', 10))
    mobileLabel.place(x=100, y=150)

    user_entry = Entry(root2, textvariable=username_verification)
    user_entry.place(x=100, y=180)

    passLabel = Label(root2, text='Password :', font=('bold', 10))
    passLabel.place(x=100, y=210)

    pass_entry = Entry(root2, textvariable=password_verification, show="*")
    pass_entry.place(x=100, y=240)

    login_button = Button(root2, text='Login', command=login_verification)
    login_button.place(x=100, y=270)


def logged_destroy():
    #logged_message.destroy()
    root2.destroy()


def failed_destroy():
    failed_message.destroy()


def logged():
    # global logged_message
    # logged_message = Tk()
    # logged_message.title("Welcome")
    # logged_message.geometry("500x100")
    # loggedLabel=Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()),font=('bold', 10))
    # loggedLabel.place(x=190, y=120)
    # failed_button=Button(logged_message,text='Logout',command=logged_destroy)
    # failed_button.place(x=190, y=180)
    newOrderApp()


def failed():
    global failed_message
    failed_message = Tk()
    failed_message.title("Error message")
    failed_message.geometry("500x100")
    failed_label = Label(failed_message, text="Invalid phone number or password", font=('bold', 10))
    failed_label.place(x=120, y=120)
    failed_button = Button(root, text='Ok', command=failed_destroy)
    failed_button.place(x=180, y=180)


def login_verification():
    global logged_user
    root2.destroy()
    user_verification = username_verification.get()
    logged_user=user_verification
    pass_verification = password_verification.get()
    sql = "select * from customer where phone_number = %s and password = %s"

    cursordb.execute(sql, [(user_verification), (pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    root.destroy()
    return


def main_display():
    global root
    root = Tk()
    root.config(background="white")
    root.title("Login System")
    root.geometry("500x500")
    main_display_label = Label(root, text='Welcome to Login System', font=('bold', 10))
    main_display_label.place(x=120, y=120)
    login_button = Button(root, text='Log In', command=login)
    login_button.place(x=180, y=150)
    exit_button = Button(root, text='Exit', command=exit)
    exit_button.place(x=180, y=180)
    root.mainloop()


#######################MAIN APP############################

def newOrderApp():
    newOrder = Tk()
    newOrder.geometry("600x500")
    newOrder.title("New Order")

    global item_rest
    item_rest = ''
    item_id = ''
    item_name = ''

    item_price = 0
    item_quantity = 0

    def insertOrder():
        global logged_user
        customer_id = logged_user
        global order_num
        if (customer_id == ""):
            MessageBox.showinfo("Insert Status", "Please login first")
        else:
            con= mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
)           
            curr = con.cursor()

            minutes = randint(0, 39)
            seconds = randint(0, 60)
            order_num = randint(10000,99999)
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            driver_id = [2005219, 4401767, 6311291, 6466139, 7147757]
            d_id = random.choice(driver_id)
            global item_rest
            global totalOrderPrice
            totalOrderPrice = calculateTotal()
            print(totalOrderPrice)
            curr.execute(
                    "Insert Into `ifood`.`order` "
                    "(`order_num`,`order_status`, `price`, `order_time`, `driver_id`, `phone_number`) VALUES "
                    "('"+str(order_num)+"',1, '" + str(calculateTotal()) + "', '" + dt_string + "', '" + str(
                        d_id) + "', '" + str(customer_id) + "')")
            
            for each in tv.get_children():
                    curr.execute("Insert Into `ifood`.`details` (`order_num`, `product_id`, `quantity`,`TIN`) VALUES ('" + str(
                        order_num) + "', '" + str(tv.item(each)['values'][0]) + "', '" + str(tv.item(each)['values'][2]) +"', '"+ str(item_rest)+ "')")

                # print(curr.execute("select order_num from `ifood`.`order` where phone_number="+customer_id))
            curr.execute("commit")

            MessageBox.showinfo("Insert Status", "Inserted Successfully")

            con.close()
                #quit_window()
            newOrder.destroy()
                #rating_window()
            payment_window()
    def payment_window():
        global rate_text
        global wndPayment
        global cardNumber
        global cardCVV
        global cardName
        global cardCoupon

        wndPayment = Tk()
        wndPayment.config(background="white")
        wndPayment.title("Payment")
        wndPayment.geometry("500x500")
        main_display_label = Label(wndPayment, text='Pay for your order', font=('bold', 10))
        main_display_label.place(x=90, y=90)

        text = Text(wndPayment, height=10)
        text.pack()

        lblcardNumber = Label(wndPayment,text="Card no")
        lblcardNumber.place(x=50, y=170)
        cardNumber = Entry(wndPayment)
        cardNumber.pack()
        lblcardCVV = Label(wndPayment,text="CVV")
        lblcardCVV.place(x=50, y=190)
        cardCVV = Entry(wndPayment)
        cardCVV.pack()
        lblcardName = Label(wndPayment,text="Card holder")
        lblcardName.place(x=50, y=210)
        cardName = Entry(wndPayment)
        cardName.pack()
        lblcardCoupon = Label(wndPayment,text="Coupon")
        lblcardCoupon.place(x=50, y=230)
        cardCoupon = Entry(wndPayment)
        cardCoupon.pack()

        insert_button = Button(wndPayment, text='Pay', command=payment_insert)
        insert_button.place(x=200, y=270)
        #update_button = Button(wndPayment, text='Insert rate', command=rate_insert)
        #update_button.place(x=200, y=300)

        wndPayment.mainloop()

    def payment_insert():
        global order_num
        global rate_text
        con= mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
)           
       
    
        curr = con.cursor()
        payment_id = randint(100000,999999)
        global totalOrderPrice
        amount = totalOrderPrice
        print(amount)
        global cardNumber
        global cardCVV
        global cardName
        global cardCoupon
        global order_num
        curr.execute(
            "Insert Into `ifood`.`payment` (`payment_id`,`amount`, `card_num`, `cvv`, `card_name`, `coupon`, `order_num`) VALUES "
            "('" +str(payment_id)+"', '" + str(amount) + "', '" + str(cardNumber.get()) + "',  '" +
            str(cardCVV.get()) + "', '" + str(cardName.get()) + "', '" +
            str(cardCoupon.get()) + "', '" + str(order_num) + "')")

        curr.execute("commit")

        MessageBox.showinfo("Insert Status", "Inserted Successfully")

        con.close()
        wndPayment.destroy()
        rating_window()
            
  
    def callbackFunc2(event):
        rest = event.widget.get()
        restData = rest.split("\t")
        global item_rest
        item_rest = restData[4]

        con= mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
)
        curr = con.cursor()
 
        curr.execute("SELECT product_id, product_name,price FROM product WHERE = " + item_rest)
        rows = curr.fetchall()

        prod_list = []
        for row in rows:
            rowData = str(row[0]) + "\t" + row[1] + "\t" + str(row[2])
            prod_list.append(rowData)
        con.close()

        products['values'] = prod_list

    def callbackFunc(event):
        rest = event.widget.get()
        restData = rest.split("\t")
        global item_rest
        item_rest = restData[4]
        #print(item_rest)

        con= mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
)
        curr = con.cursor()
 
        curr.execute('''SELECT category.category_id, category.name 
        FROM category INNER JOIN product ON category.category_id=product.category_id
        INNER JOIN shop ON shop.TIN=product.TIN 
        WHERE shop.TIN='''+item_rest+" GROUP BY category.category_id,category.name")
        rows = curr.fetchall()

        cat_list = []
        for row in rows:
            rowData = str(row[0]) + "\t" + row[1] 
            cat_list.append(rowData)
        con.close()

        products['values'] = cat_list

    def callbackProd(event):
        cat = event.widget.get()
        catData = cat.split("\t")

        global cat_name
        cat_name = catData[1]
        global cat_id
        cat_id = catData[0]
        #print(cat_name)

        # prod = event.widget.get()
        # prodData = prod.split("\t")

        # global item_name
        # item_name = prodData[1]
        # global item_price
        # item_price = prodData[2]
        # global item_id
        # item_id = prodData[0]
        # print(item_name)

        con= mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
)
        curr = con.cursor()
 
        curr.execute(
        
        '''SELECT product.product_id, product.product_name,product.price FROM product 
        INNER JOIN shop ON product.TIN=shop.TIN 
        WHERE shop.TIN='''+item_rest + " AND product.category_id="+cat_id
        )
        rows = curr.fetchall()

        prod_list = []
        for row in rows:
            rowData = str(row[0]) + "\t" + row[1] + "\t" + str(row[2])
            prod_list.append(rowData)
        con.close()
        #print(prod_list)
        categories['values'] = prod_list

    
    def callbackProd2(event):
        prod = event.widget.get()
        prodData = prod.split("\t")

        global item_name
        item_name = prodData[1]
        global item_price
        item_price = prodData[2]
        global item_id
        item_id = prodData[0]
        #print(item_name)

        # con = mysql.connect(host=host, user=username, password=password, database=database)
        # curr = con.cursor()
        # curr.execute(
        
        # '''"SELECT product_id, product_name,price FROM product 
        # INNER JOIN category ON category.category_id=product.category_id
        # INNER JOIN shop ON shop.TIN=product.TIN  
        # WHERE shop.TIN= '''+item_rest + "and product.category_id="+cat_id

        # )
        # rows = curr.fetchall()

        # prod_list = []
        # for row in rows:
        #     rowData = str(row[0]) + "\t" + row[1] + "\t" + str(row[2])
        #     prod_list.append(rowData)
        # con.close()
    def rating_destroy():
        root3.destroy()
      

    def rating_window():
        global rate_text
        global root3
        global E1
        root3 = Tk()
        root3.config(background="white")
        root3.title("rating")
        root3.geometry("500x500")
        
       
        main_display_label = Label(root3, text='Rate your order', font=('bold', 14))
        main_display_label.place(x=90, y=90)
       

        E1 = Entry(root3)
        
        E1.pack(padx=5, pady=170)
        
        update_button = Button(root3, text='insert rate', command=rate_insert)
        update_button.place(x=200, y=200)
         
        root3.mainloop()
       

    def rate_insert():
        global E1
        global order_num
        global rate_text
        rate_text=E1.get()
        con= mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
)
        rat_id = randint(10000, 99999)
        
        
        curr = con.cursor()
        curr.execute("Insert Into `ifood`.`rating` (`rating_id`, `rating`, `order_num`) VALUES ('" 
            +str(rat_id)+ "',  '"+str(rate_text)+ "', '"+str(order_num) + "')")

      
        curr.execute("commit")

        MessageBox.showinfo("Insert Status", "Inserted Successfully")  
               
        con.close()
        rating_destroy()
            

    def removeItem():
        item_count = len(tv.get_children())
        if item_count > 0:
            if tv.selection():
                selected_item = tv.selection()[0]  ## get selected item
                tv.delete(selected_item)
                txtTotal.delete(0, END)
                txtTotal.insert(0, calculateTotal())

    def calculateTotal():
        global price_order
        totalPrice = 0
        for each in tv.get_children():
            totalPrice += float(tv.item(each)['values'][3])
        price_order=totalPrice
        return totalPrice

    def addToOrder():
        global item_name
        global item_price

        if len(txtQuantity.get()) > 0:
            item_quantity = int(txtQuantity.get())
            global item_id
            if 'item_id' in globals():
                item_total = item_quantity * float(item_price)
                tv.insert('', 'end', text="1", values=(item_id, item_name, item_quantity, item_total))
                txtTotal.delete(0, END)
                txtTotal.insert(0, calculateTotal())
                restaurants['state'] = 'disabled'
            else:
                MessageBox.showinfo(database, "Choose some food before")
        else:
            MessageBox.showinfo(database, "Choose how many items you want")

    restaurants = tkinter.ttk.Combobox(newOrder, width=27)

    lbl_restaurants = tkinter.ttk.Label(newOrder, text="Select restaurant :")
    lbl_restaurants.place(x=10, y=10)
    con= mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
)
    curr = con.cursor()
    curr.execute("SELECT shop_name,  min_price, opening_time, closing_time, TIN FROM ifood.shop")
    rows = curr.fetchall()
    restaurants.current()
    restaurants.bind("<<ComboboxSelected>>", callbackFunc)
    results = ""
    rest_list = []
    for row in rows:
        result = str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4])
        #print(result)
        rest_list.append(result)
        '''
        rowData = list(row)
        rowData[2] = (datetime.min + rowData[2]).time()
        rowData[2] = rowData[2].strftime("%H:%M")
        rowData[3] = (datetime.min + rowData[3]).time()
        rowData[3] = rowData[3].strftime("%H:%M")
        rest_list.append(rowData)
        '''
    con.close()

    restaurants['values'] = rest_list
    restaurants.place(x=10, y=30)

    #Categories list
    products = tkinter.ttk.Combobox(newOrder, width=27)
    lbl_products = tkinter.ttk.Label(newOrder, text="Select category :")
    lbl_products.place(x=250, y=10)
    products.current()
    products.place(x=250, y=30)
    products.bind("<<ComboboxSelected>>", callbackProd)

    #Items list
    categories = tkinter.ttk.Combobox(newOrder, width=27)
    lbl_categories = tkinter.ttk.Label(newOrder, text="Select item :")
    lbl_categories.place(x=250, y=60)
    categories.current()
    categories.place(x=250, y=90)
    categories.bind("<<ComboboxSelected>>", callbackProd2)

    lblQuantity = Label(newOrder, text="No of items:", font=('bold', 10))
    lblQuantity.place(x=190, y=135)
    txtQuantity = Entry()
    txtQuantity.place(x=280, y=135)

    lblTotal = Label(newOrder, text="Order total:", font=('bold', 10))
    lblTotal.place(x=190, y=170)
    txtTotal = Entry()
    txtTotal.place(x=280, y=170)

    

    

    tv = Treeview()
    tv['columns'] = ('prod_id', 'prod_name', 'prod_quantity', 'prod_price')
    # tv.heading("#0", text='Item no', anchor='w')
    tv.column("#0", anchor="w", width=0)
    tv.heading('prod_id', text='Product Id')
    tv.column('prod_id', anchor='w', width=90)
    tv.heading('prod_name', text='Product name')
    tv.column('prod_name', anchor='w', width=180)
    tv.heading('prod_quantity', text='Quantity')
    tv.column('prod_quantity', anchor='e', width=70)
    tv.heading('prod_price', text='Price')
    tv.column('prod_price', anchor='e', width=90)
    # tv.pack(sticky=(N, S, W, E))
    tv.pack()
    newOrder.treeview = tv
    newOrder.grid_rowconfigure(1, weight=1)
    newOrder.grid_columnconfigure(1, weight=1)
    tv.place(relx=0.05, rely=0.4)

    addProduct = Button(newOrder, text="Add to order", command=addToOrder)
    addProduct.place(x=460, y=137)
    removeProduct = Button(newOrder, text="Remove from order", command=removeItem)
    removeProduct.place(x=460, y=172)
    saveOrder = Button(newOrder, text="Send order", command=insertOrder)
    saveOrder.place(x=480, y=390)
    # insert = Button(newOrder, text="Insert", command=insert)
    # insert.place(x=20, y=180)

    newOrder.mainloop()


main_display()
