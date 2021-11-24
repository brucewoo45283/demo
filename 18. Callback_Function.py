# https://www.youtube.com/watch?v=iUrUf5ijiWs&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=33
# 1.  什麼是回呼函式：是一種函式"操作過程"，把一個函式當作參數，丟進另一個函式中跑
# 1.1 函式參數的基本使用
# 1.2 情境：透過"函式參數"，傳遞函式

# 2. 回呼函式的使用
# 2.1 呼叫回呼函式
# 2.2 傳遞參數到回呼函式中
# 2.3 運用回呼函式做彈性的輸出

#ex1
## 建立第一支函式
def test(arg):
    arg()   #在此做"函式呼叫"，可以代入參數



## 建立第二支函數(此函式handle稱為回呼函式)
def handle():
    print(100)

# 呼叫test函式，把第二支函式hadle當參數，傳送到arg

test(handle)
# 輸出:<function handle at 0x000002FC9A5A10D0> 
# 表示arg裝的是一個函式，"函式透過參數，傳遞到另一支函式，此時arg就是handle
# 把handle函式傳遞到參數arg → arg參數呼叫"回呼函式handle"，執行handle函式裡的程式碼，印出結果


#ex2
## 建立第一支函式
def test(arg):
    arg("hello")  #在這邊做控制!!!  

## 建立第二支函數(此函式handle稱為回呼函式)
def handle(da):
    print(da)


test(handle)

# 把handle函式傳遞到參數arg → arg參數呼叫"回呼函式handle"，執行handle函式裡的程式碼(把"hello"傳遞到"da")，印出結果hello

#情境範例:我可以利用設定各種不同的回呼函式，來呈現相同的結果
## 建立add() 函式
def add(n1, n2, cb): #定義一個參數cb，cb我要它能接收一個回呼函式
    cb(n1+n2)

## 建立回呼函式handle1
def handle1(result): #宣告一個參數result
    print("答案揭曉", result)

## 建立回呼函式handle2
def handle2(result): 
    print("my answer is:", result)

#執行
add(3,7, handle1) #把3加7的結果，傳遞到回呼函式handle1的參數result中，印出output"答案揭曉 10"
add(3,7, handle2)