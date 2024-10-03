
def test (n1, n2):
  return n1+n2


test (1,3)

# 改用匿名函式改寫
## lambda 參數 : 回傳值
## 變數name = lambda 參數 : 回傳值
test2= lambda n1, n2 : n1+n2 

test2(1,3)


## 參數 *ns >> 參數個數可為不固定
def test(*ns):
  max(ns)*2
  
 ## 改寫 
 test1=lambda *ns:max(ns)*2 
 res1=test1(-1,-10,0,-2)  # 找出(-1,-10,0,-2)的最大值並乘2
 
 
 ## 搭配filter
 data=[1,5,-2,10,-5]
 data1=list(filter(lambda n:n>0, data))
 
 ## 搭配map >> [2, 10, -4, 20, -10]
 data2=list(map(lambda n:n*2, data))
 
 
 
 # 實務練習日期操作
 from datetime import datetime
 def now():
   return datetime.now()
   
 now()
 
## 改用匿名函式改寫
now= lambda : datetime.now()
print(now())
 
 
# 篩選大於等於 18 歲的年齡
ages=[5,20,18.30,100,12,4,37]

##filter(篩選規則,資料)
list(filter(lambda a:a>=18,ages))




# 使用映射函式統一將價格打 8 折
prices=[100,20,309,45]
list(map(lambda p:p*0.8,prices))