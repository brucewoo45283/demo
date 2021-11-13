#所有物件都有ID, TYPE, VALUE
#https://www.youtube.com/watch?v=uPKgQ3FoVtY&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=16
#https://www.youtube.com/watch?v=Lr5N2r1rmtM&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=17
#https://www.youtube.com/watch?v=MZtTClJ74NU&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=18
a = 'Hello World'
id(a)   #編號 a, 1都是物件
type(a)
a = 1
print(type(1))
print(type([]))
print(type({}))
print(type(()))
#檢視屬性、方法
print(dir(a))
#可變性
a = [1,2,3]
b = [1,2,3]
print(id(a), id(b))
a = 1
b = 1
print(id(a), id(b))

#定義類別(class):用class來建立一個模板，用模板來產生大量物件
#類別的"屬性":封裝的函式or變數
#物件 = 屬性attribute + 方法method
#example 1
class Sample(object): #class 類別名稱(object)
    pass
x = Sample()    #創物件
type(x)

#example 2
class Dog(object):             #class 類別名稱(object)
    def __init__(self, breed): # 定義封裝的變數: def 建構子(內部屬性, 參數)
        self.breed = breed     # 定義封裝的函式: 內部屬性.參數=參數

sam = Dog(breed = 'Lab')      #創一個物件sam     
frank = Dog(breed = 'Huskie') #創一個物件frank
dir(sam)
sam.breed

#example 3
class Dog(object):
    species = 'mammal'    #類別屬性，是公開的，類別以外的地方也可存取
    def __init__(self, breed, name):
        self.breed   = breed
        self.name    = name
sam = Dog('Lab', 'Sam')
sam.breed
sam.name
sam.species
Dog.species

#example 4
#定義類別、類別屬性(封裝在類別中的變數與函式)

class IO: #定義一個類別IO
    supportedSrcs=["console", "file"]   #屬性supportedSrcs
    def read(src):                     #屬性read
        print("read from", src)

#操作類別
IO.supportedSrcs

#呼叫函式
IO.read("file")

#example 5
class IO:
    supportedSrcs=["console", "file"]   
    def read(src):                     
        if src not in IO.supportedSrcs:
            print("不支援")
        else:
            print("read from", src)

IO.read("internet")

#example 6









