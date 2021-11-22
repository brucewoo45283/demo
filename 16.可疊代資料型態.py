# https://www.youtube.com/watch?v=VEQ4UBfLbdc&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=32
# 1. Q:什麼是可疊代 Iterable
# 1.1 A:可以分開、逐一取出內部資料

# 2. 可疊代的資料型態
# 2.1 字串:是，"hello"可以把 h e l l o逐一取出
# 2.2 列表:是，list, tuple都是
# 2.3 集合:是，{100,12,20}
# 2.4 字典:是，key值可以分開且逐一取出

# 3. 運用情境
# 3.1 搭配 for 迴圈使用
# 3.2 內建函式, ex1.使用 max(放入可疊代資料)，函式回傳最大值
# 3.3 內建函式, ex2.使用 sorted(可疊代資料)，函式回傳排序後的列表

##for 迴圈: for 變數名稱 in 任何的可疊代資料，迴圈會將可疊代的資料逐一分開，取出 
for i in range(0,11):
    print(i)

for i in "Hello":
    print(i)

for i in {"Hello", 100}:
    print(i)  #集合沒有順序性

for i in {"a":10, "b":100}:
    print(i)   #印出a, b，只會對key做動作

##如果我要取字典的值
dic={"a":10, "b":100}     #先宣告字典為dic變數
for i in dic:
    print(dic[i])

##內建函式
result=max("abcd")
print(result)

result=max({"a":10, "b":100})
print(result)  #比較key值大小