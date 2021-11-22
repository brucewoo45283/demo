# https://www.youtube.com/watch?v=YQboCnlOb6Y&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=30
# 0. 發送電子郵件的基本流程。

# 1. 準備訊息物件與相關內容
# 1.1 載入 email.message 模組
# 1.2 建立訊息物件 email.message.EmailMessage
# 1.3 設定寄件人、收件人和信件主題
# 1.4 設定純文字的內容
# 1.5 設定 HTML 網頁格式內容

# 2. 連接伺服器並寄送信件
# 2.1 寄送電子郵件的基本觀念
# 2.2 載入 smtplib 模組
# 2.3 連接 SMTP 伺服器
# 2.4 驗證寄件人身份
# 2.5 寄出信件

# 3. Gmail 驗證身份的注意事項
# 3.1 打開低安全性應用程式存取權(重要!)
# 3.2 二階段認證：產生並使用應用程式密碼登入，會跑出一組Windows 電腦專用的應用程式密碼，來當作登入密碼

##準備訊息物件msg
import email.message
msg=email.message.EmailMessage()
msg["From"]="brucewoo45283@gmail.com"
msg["To"]="shunchipeng@gmail.com"
msg["Subject"]="測試"

##如果我要寄送"純文字"
##msg.set_content("我一定要成功")

##如果我要寄送"html"
msg.add_alternative("<h3>恭禧</h3>卡卡西當上火影", subtype="html")

##連線到 gmail的SMTP 伺服器(可以到網路上搜尋gmail的server)，驗證寄件人身分並發送郵件
import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com", 465) #連線到gmail主機，寄件人一定要是gmail帳戶
server.login("brucewoo45283@gmail.com", "mlgyqaipbielpmpd") #windows電腦產生"應用程式專用密碼"
server.send_message(msg)
server.close()