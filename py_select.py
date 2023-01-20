# 更新資料、取得資料
## 只想取得一筆data: fatchone();  多筆 fatchall()
import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="paulpierce34",
    host="localhost",
    database="mydb",
    auth_plugin='mysql_native_password'
)
print("db連線成功")

## python取檔名，不要與python保留字，模塊名等相同，不然運行MySQL庫的時候報錯：AttributeError: module 'MySQLdb' has no attribute 'connect'

## 建立cursor物件
cursor=con.cursor()

# # 更新資料 con.cursor("SQL Statement")
# cursor.execute("UPDATE product SET name='心痛的感覺' where id=1")
# con.commit()

# # SQL STATEMENT用變數 productname, productid
# productname='摩卡'
# productid='3'
# cursor.execute("UPDATE product SET name=%s where id=%s",(productname,productid))
# con.commit()

## 一筆data: fatchone();  多筆 fatchall()
cursor.execute("select * from product where id=3")
data=cursor.fetchone()
print(data[0], data[1], data[2]) # 利用tuple, 分開取得資料

##  多筆 fatchall()
cursor.execute("select * from product where id in (1,3,5) order by price desc")
data=cursor.fetchall()
print(data[0], data[1], data[2]) # 利用tuple, 分開取得資料
con.commit()

## 逐一取得資料
for r in data:
    print(r[0],r[1],r[2])