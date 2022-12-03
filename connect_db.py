# 安裝套件: pip install mysql-connector-python

#連線到mysql
import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="paulpierce34",
    host="localhost",
    database="mydb",
    auth_plugin='mysql_native_password'
)
print("db連線成功")
#關閉資料庫連線
#con.close()

# 下SQL以新增資料 : 建立crusor物件
#並且建立變數到sql指令  用tuple (%s,%s)
productID=6
productName="奶綠_from_py"
cursor=con.cursor()
cursor.execute("insert into product(id,name) values(%s,%s)",(productID,productName))
con.commit()  #確定執行
con.close()


