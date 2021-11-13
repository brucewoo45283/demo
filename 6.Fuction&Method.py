#course 0719(2) 01:33:09
#https://www.youtube.com/watch?v=7qKFvUVpQXg&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=9
import sys
help(sys)
dir(sys)
#如何查詢"內建函式"
a=[2,4,9,90]
dir(a)
#如何查詢"說明文件"
help(a.count)

#自訂函式、呼叫函式
#example 1
def add_num(n1, n2): #def 函式名稱(參數):
    res=n1+n2       #程式碼內部運行
    return(res)    #回傳值:return 資料
add_num(100, 20)     

#example 2:程式的包裝；當你發現重複的事一直做
sum=0
for i in range(11):
    sum=sum+i
    print(sum)

sum=0
for i in range(11,21):
    sum=sum+i
    print(sum)
#包裝過程之一:把重複做的程式碼"縮排"進入自訂函式
def cal():
    sum=0
    for i in range(11):
        sum=sum+i
    print(sum)
cal() #直接呼叫自訂函式
#包裝過程之二:設定參數
def cal(k1, k2): #帶入自設參數
    sum=0
    for i in range(k1, k2):
        sum=sum+i
    print(sum)
cal(15, 20)

# example 3:參數任一個，使用tuple做包裝，例如參數是1加到n
#:0719第二堂 1:42:37
def addall(x, *args): #x對應2，3,4,5,8,10以*args包裝成tuple
    res=x
    for y in args:#y的for迴圈，把x以外的參數依序丟入以下的運算
        print(x, y)
        res = res+y #res變數與y變數相加
    return(res)
    
addall(2,3,4,5,8,10)

#example 3:做一個計算平均數的函式(邏輯有問題)
def avg(x, *args):
    res=x
    for y in args:
        res=res+y
        print(res,y, len(str(res)))
    return(res/len(str(x)))
    
avg(10,15,20)

#example 4:把無限參數包裝成字典
def make_two_lists(**kwargs):
    keys, values = [],[]
    for k, v in kwargs.items():
        keys.append(k)
        values.append(v) #把字典拆成兩個list
    return([keys,values])

make_two_lists(david='M', marry='F', John= 'M')


#匿名函式:當函式過於簡單時適用、spark、dataFrame也常用
def square(x):
    return(x*x)
square(3)
#等價於
square2=lambda x:x*x
square2(10)


#example1 判斷偶數
even=lambda e:e%2==0
even(21)
#example2 取字串的第一個元素
first=lambda f:f[0]
first("櫻木")

#example3 字串倒排
rev=lambda r:r[::-1]
rev("櫻木")

#example4 字串相加
add=lambda a, b:a+b
add("櫻木","灌籃")

#Nested Statement and Scope 巢狀陳述與範圍

x = 25 #x在函式外
def printer():
    x = 50 #x在函式內
    return(x)

print(x)
print(printer()) #x在函式內，x=50
print(x) #x為25，兩個x互不影響

#範圍搜尋順序:LEGB規則，Local, Enclosing functions, Global, Built in
#2:25:39
name = 'This is a global name' 

def greet(): 
    # Enclosing function 
    #print(name)
    name = 'Sammy'  # Enclosing function locals
    def hello(): 
        print('Hello '+name )

    hello() 

greet()
