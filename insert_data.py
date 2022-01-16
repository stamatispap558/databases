import mysql.connector
import pandas as pd
from datetime import datetime
from dateutil import parser

PATH = "C:/Users/Anastasia/Documents/ECE Upatras/Semester 7/database/"
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="efood_team27",
  database="ifood",
  port=3306
)
cursor = mydb.cursor()

#INSERT CUSTOMER DATA
customer_data = pd.read_csv(PATH+"customer_data.csv",sep=';' )
customer_df=pd.DataFrame(customer_data)
for row in customer_df.itertuples():
    cursor.execute('''
                INSERT INTO ifood.customer(phone_number,firstname,lastname,email,password,street,street_number,zip)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ''',
                (
                row.phone_number,
                row.first_name,
                row.last_name,
                row.email,
                row.password,
                row.street,
                row.street_number,
                row.zip,
               
                )                  
                )
mydb.commit()

#INSERT SHOP DATA
shop_data = pd.read_csv(PATH+"shop_data.csv",sep=';' )
shop_df=pd.DataFrame(shop_data)
for row in shop_df.itertuples():
   cursor.execute('''
                INSERT INTO ifood.shop(TIN,shop_name,min_price,zip,street,street_number,opening_time,owner_name,closing_time)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''',
                (row.TIN,
                row.shop_name,
                row.min_price,
                row.zip,
                row.street,
                row.street_number,
                row.opening_time,
                row.owner_name,
                row.closing_time                              
                )                  
                )
mydb.commit()

#INSERT DRIVER DATA
driver_data = pd.read_csv(PATH+"driver_data.csv",sep=';' )
driver_df=pd.DataFrame(driver_data)
for row in driver_df.itertuples():
   cursor.execute('''
                INSERT INTO ifood.driver(driver_id,firstname,lastname,phone_number)
                VALUES (%s,%s,%s,%s)
                ''',
                ( 
                   row. driver_id,
                   row.firstname,
                   row.lastname,
                   row.phone_number                           
                )                  
                )
mydb.commit()

#INSERT CATEGORY DATA
category_data = pd.read_csv(PATH+"category_data.csv",sep=';' )
category_df=pd.DataFrame(category_data)
for row in category_df.itertuples():
   cursor.execute('''
                INSERT INTO ifood.category(category_id,name)
                VALUES (%s,%s)
                ''',
                ( 
                   row. category_id,
                   row.name,
                                     
                )                  
                )
mydb.commit()

#INSERT PRODUCT DATA
product_data = pd.read_csv(PATH+"product_data.csv",sep=';' )
product_df=pd.DataFrame(product_data)
for row in product_df.itertuples():
    cursor.execute('''
                INSERT INTO ifood.product(product_id,product_name,price,TIN,category_id)
                VALUES (%s,%s,%s,%s,%s)
                ''',
                (
                row.product_id,
                row.product_name,
                row.price,
                row.TIN,
                row.category_id                                     
                )                  
                )
mydb.commit()

#INSERT ORDER DATA
order_data = pd.read_csv(PATH+"order_data.csv",sep=';' )
order_df=pd.DataFrame(order_data)

for row in order_df.itertuples():
    cursor.execute('''
                INSERT INTO ifood.order(order_num,order_status,price,order_time,driver_id,phone_number)
                VALUES (%s,%s,%s,%s,%s,%s)
                ''',
                (
                row.order_num,
                row.order_status,
                row.price,
                parser.parse(row.order_time),
                row.driver_id,               
                row.phone_number                                      
                )                  
                )
mydb.commit()

#INSERT DETAILS DATA
details_data = pd.read_csv(PATH+"details_data.csv",sep=';' )
details_df=pd.DataFrame(details_data)
for row in details_df.itertuples():
    cursor.execute('''
                INSERT INTO ifood.details(order_num,product_id,TIN,quantity)
                VALUES (%s,%s,%s,%s)
                ''',
                (
                row.order_num,
                row.product_id,
                row.TIN,
                row.quantity                                     
                )                  
                )
mydb.commit()

#INSERT RATING DATA
rating_data = pd.read_csv(PATH+"rating_data.csv",sep=';' )
rating_df=pd.DataFrame(rating_data)
for row in rating_df.itertuples():
    cursor.execute('''
                INSERT INTO ifood.rating(rating_id,rating,order_num)
                VALUES (%s,%s,%s)
                ''',
                (
                row.rating_id,
                row.rating,
                row.order_num                                                     
                )                  
                )
mydb.commit()

#INSERT PAYMENT DATA
payment_data = pd.read_csv(PATH+"payment_data.csv",sep=';' )
payment_df=pd.DataFrame(payment_data)
for row in payment_df.itertuples():
    cursor.execute('''
                INSERT INTO ifood.payment(payment_id,amount,card_num,cvv,card_name,order_num)
                VALUES (%s,%s,%s,%s,%s,%s)
                ''',
                (
                row.payment_id,
                row.amount,
                row.card_num,
                row.cvv,
                row.card_name,
                row.order_num                                                  
                )                  
                )
mydb.commit()