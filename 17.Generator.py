# https://www.youtube.com/watch?v=x6MNOSRY5EM&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=32
# 1. Q:什麼是生成器
# 1.1 A:可"動態產生"的可疊代資料，搭配 for 迴圈使用， for 變數名稱 in 生成器

# 2. 建立生成器
# 2.1 在函式中使用 yield 語法
# 2.2 呼叫函式回傳生成器

# 3. 搭配 for 迴圈使用
# 3.1 生成器是一個可疊代的資料
# 3.2 利用 for 迴圈取得 yield 產生的資料

# 建立生成器函式
def test():
    print("階段一")
    yield 3
    print("階段二")
    yield 5

# 呼叫函式，把生成器存入變數gen
# 若函式中使用yield語法，呼叫函式會建立生成器，暫時不會執行裡面的程式碼
gen=test()
print(gen)

#<generator object test at 0x000002178BA606D0>

#搭配for迴圈，程式碼才會動起來
for i in gen:
    print(i)

#利用生成器產生某個數值以下的偶數
def generateEven(maxNumber):
    number=0
    while number<=maxNumber:
        yield number
        number+=2

evenGenerator=generateEven(21)
for data in evenGenerator:
    print(data)











