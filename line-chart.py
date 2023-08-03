import matplotlib.pyplot as plt
# 設定中文字型
plt.rc('font', family='Microsoft JhengHei')
# 一組資料點 (1,2) (2,4) (3,6)
#plt.plot([1,2,3],[2,4,6])
#plt.show()

#2組資料  (1,2) (2,4) (3,6) / (1,1) (2,2) (3,3)
#plt.plot([1,2,3],[[2,1],[4,2],[6,3]])
#plt.show()

# 使用legend方法產生圖例
#plt.plot([1,2,3],[[2,1],[4,2],[6,3]], label=["team1","team2"])
#plt.legend()
#plt.show

# 匯入csv並畫折線圖
import csv
file=open('data.csv', encoding='utf-8')
reader=csv.reader(file)
header=next(reader) #讀標題
print('標題', header)
x=[]
y=[]

for r in reader:
    print("每列資料", r)
    x.append(int(r[0]))       
    y.append([int(r[1]),int(r[2])]) 

plt.plot(x,y,label=header[1:3])   #取得第二筆~第三筆的資料，當標頭
plt.legend()
plt.xlabel(header[0])
plt.ylabel('薪資')
plt.show()



