# 載入模組 建立writer物件， 存放進變數writer
#import csv
#with open("data.csv", mode="w", newline="") as file:
#    writer=csv.writer(file)
#    writer.writerow([1,2,3])
#    writer.writerow([4,5,6])
#    writer.writerow([7,8,9])

# 讀取檔名data.csv , 放進變數file, 建立reader物件

#import csv
#with open("data.csv", mode="r", newline="") as file:
#    reader=csv.reader(file)
    # 用for loop 逐列讀取資料, row會是list, 讀出來會是字串格式
#    for row in reader:
#        print(row)

# 把9個變數來做加總
import csv
with open("data.csv", mode="r", newline="") as file:
    reader=csv.reader(file)
    # 用for loop 逐列讀取資料, row會是list, 讀出來會是字串格式
    total=0
    for row in reader:
        # 再寫一層for loop
        for data in row:
            total=total+int(data) # data變數記得轉整數 再相加
        print(total)