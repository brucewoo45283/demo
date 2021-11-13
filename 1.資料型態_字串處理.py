#變數與資料型態
#數字與字串
#有序列表，集合、與字典

#資料型態
#有序列表，-list、可以裝載不同類型的元素
grades=[11,23,89,90]
grades[0]=55
grades
#連續刪除list的元素
grades[1:2]=[]
grades
#list串接
grades=grades+[88,99]
grades
#取得列表長度
length=len(grades)
length
#巢狀list
data=[[2,4,5],[7,8,9]]
data[1][0]
#tuple，無法更動資料
c=(8,9,10)
type(c)
c[1]=100

#列出多行文字
text='''前陣子電影【沙丘】話題性非常高，除了宏觀壯麗的場景與劇本外，電影中男主角Timothée Chalamet也成為許多女孩子心目中的新男神
，身為一個髮型師當然還是一直注意到他的髮型真的非常帥氣，剛好也是我自己很喜歡的長髮髮型，但大家都會擔心說東方人到底有沒有辦法做出那種質感。其實是可以的！只要用對方法一樣做得出來，因此今天就來弄給大家看啦！希望大家會喜歡
喜歡我的影片，記得按讚加訂閱，也可以追蹤我們的IG&FB喔！'''
print(text)

#字串索引 跳兩個字選取
t1=text[::2]
print(t1)
#字串索引 反轉字串
t2=text[::-1]
print(t2)

#字串搜關鍵字次數
text.count("髮型")

#字串分割
text.split("，")
#字串轉化(格式化字串)、自動化報表好用
#  %s 若有特殊字元就用%r
x="for 3"
print("lebron james:%s"%(x))
#r"   " 可跳脫字元、repr()
#.format()  字串取代在安排(p)的位置
"one:{p}, two:{p}, three:{p}".format(p="more~")












