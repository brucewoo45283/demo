#隨機選取
import random

random.sample([1,4,9,10,5000,24,45], 3) #從列表中取3個

#隨機亂數
random.uniform(0.0, 11.0)
#常態分配亂數
random.normalvariate(100, 10) #取得平均100, 標準差10 常態分配亂數

#計算平均數
import statistics
statistics.mean([1, 4, 6, 9]) #計算列表中的平均數

#計算標準差
statistics.stdev([1, 4, 6, 9])