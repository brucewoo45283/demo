# https://www.youtube.com/watch?v=F4hWr87ZcSc&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=35
# 1.  什麼是裝飾器工廠
# 1.1 裝飾器工廠用來產生裝飾器
# 1.2 裝飾器工廠是一個函式
# 1.3 裝飾器工廠接受額外的參數
#     目的:給裝飾器彈性

# 2. 裝飾器工廠的實作
# 2.1 定義裝飾器工廠和參數
# 2.2 裝飾器工廠內部定義裝飾器
# 2.3 三層函式結構
# 2.4 呼叫帶有裝飾器函式的運作流程

# 3. 裝飾器工廠的範例：定義一個計算 1+2+...+max 總合的裝飾器工廠

# #裝飾器工廠結構
# def 裝飾器工廠名稱(參數名稱, ...):
#     [def 裝飾器名稱(回呼函式名稱):
#         def 內部函式名稱():
#             # 撰寫裝飾器內部的程式碼
#             回呼函式名稱()
#         return 內部函式名稱
#     return 裝飾器名稱]
# []內其實就是裝飾器

# #使用裝飾器工場
# @裝飾器工場名稱(參數資料, ...)
# def 函式名稱():
#     # 函式內部的程式碼

# # 呼叫帶有裝飾器的函式
# 函式名稱()

# example1
def testFactory(base): #裝飾器工廠testFactory(參數base)
    def testDecorator(callback): #裝飾器testDecorator
        def innerFunc(): #裝飾器內部innerFunc函式
            result=base*3
            callback(result)
        return innerFunc
    return testDecorator

@ testFactory(3)
def decoratedFunc(result):
    print("普通函式", result)

decoratedFunc()

#output: 普通函式 9

# example2:先寫出裝飾器，再包進裝飾器工廠，段落縮排選起來按TAB
def myFactory(base):
    def myDeco(cb):
        def run():
            print("裝飾器內的程式:", base)
            result=base*2
            cb(result)
        return run
    return myDeco

@myFactory(5)
def test(result):
    print("普統函式的函式:", result)

test()

# example3:建造一個有彈性的裝飾器，可以從1加到無限，不要只能1加到50
def calFactory(max):
    def cal(cb):
        def run():
            total=0
            for n in range(max+1):
                total+=n
            cb(total)
        return(run)
    return cal #記得要回傳裝飾器名稱

@calFactory(100) #我想要一加到100，選擇用中文印出
def show(result):
    print("結果是:", result)

@calFactory(10) #我想要一加到10，用英文印出
def showEnglish(result):
    print("Result is:", result)

show()
showEnglish()