# #course 0719(2) 16分20秒
# #彭彭: https://www.youtube.com/watch?v=C4OkV6DrVRs&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=13
# #開檔、讀檔、關檔
# #example1
# fid=open("test.txt","w") #開檔  檔名為test
# fid.write("hellow\nword") #讀檔、操作
# fid.close() #關檔:才能釋放資源


# #最佳實務 : 自動關檔
# #開啟模式: 讀取r 寫入w 增加新資料a
# #寫檔
# #with open("檔案路徑","開啟模式") as 檔案物件:
# #    fid.write("this is a test")

# with open("test.txt",mode="w", encoding="utf-8") as fid:
#     fid.write('''（一）現審定人事行政職系，具有5年以上人事工作經驗。
# （二）大學以上學歷，高等考試或相當等級之考試人事行政類科及格，最近5年年終考績至少4年考列甲等。
# （三）無限制調任情事且無公務人員任用法第28條及公務人員陞遷法第12條各款情事之一者''')

# #增加資料a
# # a => append
# fid = open('test.txt', 'a', encoding="utf-8")
# fid.write('''\n（四）考不上啦
# 1. 學歷：具中華民國國籍及教育部認可之國內外醫學院畢業。
# 2. 證照：具外科專科醫師證書。
# 3. 消極條件：無公務人員任用法第28條及公務人員陞遷法第12條所定不得任用及陞遷情事。
# 附註: 依國軍退除役官兵輔導條例第6條規定，條件相等而為因公致身心障礙退除役官兵及一般退除役官兵者，依序優先錄用。''')
# fid.close()

# # example 3 讀檔
# with open("test.txt", "r", encoding="utf-8") as fid:
#     for line in fid:   #for 迴圈 line:一行一行讀取
#         print(line.strip()) #strip把多餘的空白拿掉

# # example 4 讀檔加入判斷條件，讀取特定字串
# with open("test.txt", "r", encoding="utf-8") as fid:
#     for line in fid:
#             if "學歷" in line: #判斷條件，篩選，把學歷撈出   
#                 print(line.strip()) 

# # example 5 讀檔，並計算總合
# with open("data.text",mode="w", encoding="utf-8") as file:
#     file.write('''3
#                   20
#                   90''')
# sum=0
# with open("data.text", "r", encoding="utf-8") as file:
#     for line in file:
#         sum+=int(line) #把讀到的資料轉成數字，加到sum裡面
# print(sum)