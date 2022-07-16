#Python Selenium 快速開始、網頁截圖
#載入selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#設定chrome selenium 執行擋路徑(copy path)
options=Options()
options.chrome_executable_path="D:\python專案\基礎\課程基礎\chromedriver.exe"
#建立driver 物件實體 用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
driver.maximize_window() #先視窗最大化 再截圖
driver.get("https://www.youtube.com/watch?v=gdtetu4nnZcs")
driver.save_screenshot("screenshot.png") #網頁截圖
driver.close()