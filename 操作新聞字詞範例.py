#讀檔
with open("news.txt", "r", encoding="utf-8") as d:
    news = d.read()

#提到多少個台灣
news.count("台灣")   