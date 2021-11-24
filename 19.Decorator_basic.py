# https://www.youtube.com/watch?v=qc8hsxAK270&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=35
# 1. 什麼是裝飾器?
# 1.1 裝飾器本質上，是一個"特殊設計"的函式
# 1.2 裝飾器用來"輔助"其他函式運作，例如作為一個共同重複利用的運算邏輯

# 2. 裝飾器的實作
# 2.1 定義裝飾器
# 2.2 使用裝飾器
# 2.3 呼叫帶有裝飾器函式的運作流程

# 3. 裝飾器的範例：定義一個計算 1+2+...+ 50 總合的裝飾器
# 流程架構
# # 裝飾器架構
# def 裝飾器名稱(回呼函式名稱):
#     def 內部函式名稱():
#         # 撰寫裝飾器內部程式碼
#         回呼函式名稱()  #呼叫回呼函式
#     return 內部函式名稱

# #使用裝飾器
# @裝飾器名稱
# def 函式名稱():
#     # 函式內部程式碼

# 函式名稱() 
# 1.呼叫"帶有裝飾器"的函式 → 會先執行裝飾器內部的程式碼，再執行本來的程式碼

# # example1
# def testDecorator(callback): #定義一個裝飾器testDecorator，參數為回呼函式callback
#     def innerFunc():         #定義內部函式innerFunc，會印出回呼函式callback
#         print("裝飾器")      
#         callback(3)          #呼叫回呼函式，其實就是呼叫decoratedFunc，3會傳遞到data
#     return innerFunc         #回傳內部函式innerFunc結果

# @testDecorator
# def decoratedFunc(data):
#     print("普通函式", data)

# decoratedFunc()            #呼叫decoratedFunc，會先執行裝飾器testDecorator
#                            #把decoratedFunc()丟進參數callback，先執行innerFunc()，再呼叫回呼函式callback
#                            #最後才呼叫本來的普通函式，印出普通函式

# example2
def myDeco(cb):
    def run():
        print("印出裝飾器內的程式碼")
        cb()
    return run

@myDeco
def test():
    print("印出普通函式內的程式碼")

test()

# example3
def myDeco(cb):
    def run():
        print("印出裝飾器內的程式碼")
        cb(3) #此回呼函數cb，其實就是被裝飾的普通函式test
    return run

@myDeco
def test(n):
    print("印出普通函式內的程式碼", n)

test()

# 應用情境:定義一個計算 1+2+...+ 50 總合的裝飾器
def cal(cb):
    def run():
        # 撰寫裝飾器想要執行的程式碼
        res=0
        for i in range(51):
            res=res+i
        # 把計算結果透過參數cb傳到被裝飾的show()
        cb(res)
    return run

@cal
def show(n):
    print("計算結果:", n)

@cal
def Englishshow(n):
    print("Ans:", n)

show()
Englishshow()

# output 計算結果: 1275 , Ans: 1275

