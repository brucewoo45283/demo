#https://www.youtube.com/watch?v=sUzR3QVBKIo&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=15
# 下載特定網址資料
import urllib.request as request
with request.urlopen(url="https://www.taoyuan-airport.com/main_ch/index.aspx") as response: #類似檔案操作
    data=response.read().decode("utf-8")
print(data)  #取得桃機的原始碼，即網頁ㄉ前端HTML CSS JS
print("---------------------------------------------------")


# 公開資料串接
# 2.1 使用台北市政府公開資料 (http://data.taipei/)
# 2.2 搜尋並取得資料的串接網址 (API)
# 2.3 測試串接網址，觀察資料格式 json 
# 2.4 撰寫程式，自動連線並且擷取想要的資料
# 3. 儲存資料到檔案中
# 3.1 使用寫入模式開啟檔案
# 3.2 使用 utf-8 編碼處理中文資料

import urllib.request as request
import json
with request.urlopen("https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire") as response: #類似檔案操作
    data1=json.load(response) # 使用 json 模組，解讀 json 資料格式
print(data1)  

#整理抓到的資訊
clist=data1["result"]["results"]
print(clist)
clist
#for迴圈依依印出公司名稱:鍵值對
for company in clist:
    print(company["公司名稱"])

#儲存抓到的資料到檔案中
with open("companyname.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")

   


