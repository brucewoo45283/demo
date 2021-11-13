s1 = {2,10,90}
s2={10,90,1000}
#判斷集合內有沒有某元素
print(3 in s1)
#交集
s3=s1&s2
s3
#聯集
s4=s1|s2
print(s4)
#差集
s5=s2-s1
print(s5)
#反交集:"取不重疊的元素"
s6=s1^s2
print(s6)
#把字串拆解成集合 set()
print(set("brucewoo"))
#字典運算
dic={"a":"帥哥","b":"美女"}
print(dic["a"])

#刪除字典鍵值
del dic["a"]
dic
#把列表轉換成字典鍵值
dic={x:x*2 for x in [3,4,5]}
print(dic)





