# 1. 錯誤、例外處理
# 1.1 語法錯誤 Syntax Error
# 1.2 例外 Exception
# 1.3 例外處理的觀念說明

# 2. 例外處理
# 2.1 觀察例外的發生情境
# 2.2 使用 try ... except 語法
# 2.3 針對可能發生例外的程式進行處理，確保程式不會被中斷

# 3. 例外處理的範例
# 3.1 資料型態轉換的例外處理
# 3.2 例外處理搭配迴圈，讓使用者輸入到正確為止的程式邏輯
# https://www.youtube.com/watch?v=V3vHhR1SipU&t=21s&ab_channel=%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B

# 情境：轉換資料型態失敗
while True: # 無窮迴圈
    data=input("請輸入數字：")
    try: 
        number=int(data) # 可能會出錯的區塊
        break # 使用者輸入正確，跳出迴圈，使用者亂搞，我繼續執行except區塊語法
    except Exception:
        print("麻煩你檢查自己輸入的東西")        # 出錯我就把使用者輸入的"東西"變成0

number=number*2
print(number)
