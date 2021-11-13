#0719(2)2:41:08
#使用try except來避免錯誤訊息
#ex1
#錯誤訊息:先讀檔 卻寫檔
with open('test.txt', 'r') as f:
    f.write("Hello World")
#使用TRY EXCEPT:讓程式可以運行
try:
    f=open('test.txt', 'r')
    f.write("Hello World")
except IOError:            #執行例外狀況
    print("錯誤訊息")


#ex2 如果執行是一切正常
try:
    f = open('test.txt', 'w')
    f.write('Hello World')  #執行成功
except IOError:
    print('file is not writable')  #跳過
else:
    print('file write successful')  #執行else
f.close()

#ex3 當分母為0   ZeroDivisionError
5/0
try:
   5/0
except ZeroDivisionError:
    print("無意義")
#ex3 讓使用者自己輸入  ZeroDivisionError
a=input()
b=input()
float(a)/float(b)  #預設是字串、轉成浮點數

try:
    float(a)/float(b)
except ZeroDivisionError as Error: #同時印出錯誤訊息
    print("分母不得為0", Error)

#ex4 一次紀錄"所有例外情形"，缺點是不知道自己犯了那些錯誤
dividend = input()
divisor = input()

try:
    float(dividend) / float(divisor)
except:
    print('ERROR')

#ex5 同時兼顧
dividend = input()
divisor = input()

try:
    float(dividend) / float(divisor)
except ZeroDivisionError as Error: #分母為0 執行這段
    print("分母不得為0", Error)
except:
    print('ERROR')  #其餘情形，例如輸入字串，執行這段

#ex5 最後收尾 finally
dividend = input()
divisor = input()

try:
    float(dividend) / float(divisor)
except ZeroDivisionError as Error: 
    print("分母不得為0", Error)
except:
    print('ERROR')  
finally:
    print("the end")

