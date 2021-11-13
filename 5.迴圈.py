# #for 迴圈:適用於反覆的資料操作
# #example 1 插入print可以看過程
# for i in range(1,11):
#     print(str(i),".伯俊")
#     print(str(i)+".伯俊")


# #example2: 1加到100
# list_num=0 #紀錄累加的結果
# for num in range(1,101): 
#     print(list_num , num) 
#     list_num = list_num + num
# print(list_num)

# #example3: 提取字串
# a="現觀科技是世界領先的海量電信數據分析公司"
# for s in a:
#     print(s)

# #example4: tuple
# l=[(2,4),(6,8),(10,12)]
# for tuple in l:
#     print(l)

# #example5: 拆解tuple
# l=[(2,4),(6,8),(10,12)]
# for t1, t2 in l:
#     print(t2)

# #example5: 把兩個數據集對應起來, zip()
# disease_name = ['侵襲性肺炎鏈球菌感染症', '急性病毒性Ａ型肝炎', '急性病毒性Ｃ型肝炎', '恙蟲病', '流感併發重症', '流行性腮腺炎', '登革熱']
# disease_count = [7,7,10,14,101,12,8]
# zip(disease_name, disease_count)
# for t1,t2 in zip(disease_name, disease_count):
#     print(t1, t2)

# #example6: for迴圈操作字典:把字典的值取出
# dic = {'k1':1, 'k2':2, 'k3':3}
# for item in dic:
#     print(dic.get(item))

# #example7:依據"位置"取值
# li=[2,5,9,79]
# len(li)
# for pos in range(0,len(li)):
#     print(li[pos])


# # while 迴圈，while:布林值判斷
# x = 0 
# while x < 10:
#     x += 1
#     print('current x is ', x)
#     if x==3:
#         print('x==3')
#         break
#     else:
#         print('continuing')
#         continue
#     print('what else')


# # example:while 迴圈做計時器
# import time
# from datetime import datetime
# while True:
#     print(datetime.now())
#     time.sleep(5)

# # example:while 迴圈做機器人
# while True:
#     answer = input()
#     if answer == 'DONE':
#         break
#     else:
#         print('Hi Hi', answer)

# #break範例
# n=0
# while n<5:
#     if n==3:
#         break  #當n為3，直接強制結束
#     print(n)
#     n=n+1
#  print("最後的n:", n)

#選起來、一次註解掉所有程式 crtl+/

#continue範例
# n=0
# for x in [0,1,2,3,4,5]:
#     if x%2==0: #x如果為偶數，會跑continue，忽略下方的程式，直接進入下個迴圈
#         continue  #x如果不為偶數，才會跑下面兩行
#     print(x)
#     n+=1
# print("最後的n:", n)

#else範例
# sum=0
# for n in range(11):
#     sum+=n #sum為0+1+....10
# else:
#         print(sum)

#example建立一個把"整數"開根號的計算機
# n=int(input("請在此輸入一個整數:"))
# for i in range(n): #我輸入9(n)、i為0到8
#     if i*i==n:     #下一個條件判斷,當i的平方為我輸入的n時
#         print("整數平方根", i) 
#         break    #用break來強制結束迴圈，else會被忽略   
# else:
#     print("沒有")











