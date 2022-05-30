DROP TABLE IF EXISTS Invoices;
CREATE TABLE Invoices
(InvoiceDate date,
InvoiceAmount int);
INSERT INTO Invoices
VALUES
('2022-12-01', 1), ('2023-02-01', 1), ('2023-02-15', 1),
('2023-03-01', 3), ('2023-04-01', 2), ('2023-04-15', 2),
('2023-05-01', 5), ('2023-06-01', 3), ('2023-06-15', 3), ('2023-08-01', 8);

--取得資料表最小日期
select MIN(InvoiceDate) FROM Invoices; -- '2022-12-01'

-- 取得資料範圍，最小日期與日期欄位的時間間隔【即差了幾個月？】，指定兩個指定日期之間的時間間隔數目 DATEDIFF
-- 產生新欄位DifferenceInMonths
SELECT *, DATEDIFF(MONTH, (select MIN(InvoiceDate) FROM Invoices), InvoiceDate) as DifferenceInMonths
FROM Invoices;

-- 轉換InvoiceDate日期格式，把值都轉成年月就好，且預設日期為每個月的第一天【sql server 使用DATEFROMPARTS】
-- 效果：2023-02-15 轉成 2023-02-01
SELECT *, 
       DATEDIFF(MONTH, 
               (select MIN(InvoiceDate) FROM Invoices), 
			    InvoiceDate)     as DifferenceInMonths,
		 DATEFROMPARTS(YEAR(InvoiceDate), MONTH(InvoiceDate), 1)as StartOfMonth			  
FROM Invoices;

-- 使用CTE查詢 【6:35】
-- https://www.youtube.com/watch?v=6-y7OAf_VVc
WITH Invoices1 AS (
SELECT *, 
       DATEDIFF(MONTH, 
               (select MIN(InvoiceDate) FROM Invoices), 
			    InvoiceDate)     as DifferenceInMonths,
		 DATEFROMPARTS(YEAR(InvoiceDate), MONTH(InvoiceDate), 1)as StartOfMonth			  
FROM Invoices),
Invoices2 AS(
SELECT DifferenceInMonths, -- 這裡選處理好的欄位、我要的欄位
       StartOfMonth, 
	   SUM(InvoiceAmount) AS Total_InvoiceAmount -- 並處理我要的結果【依 DifferenceInMonths, StartOfMonth來分組計算InvoiceAmount】
FROM Invoices1
GROUP BY DifferenceInMonths, StartOfMonth)
SELECT StartOfMonth,
       DifferenceInMonths, 
	   Total_InvoiceAmount,
	   (SELECT SUM(Total_InvoiceAmount) 
	    FROM Invoices2 AS t1
		WHERE t1.DifferenceInMonths BETWEEN t2.DifferenceInMonths-2 AND t2.DifferenceInMonths) AS Running_3Month_Total 
      -- SUM(Total_InvoiceAmount) AS Running_3Month_Total 
FROM Invoices2 AS t2;

-- self join寫法
WITH InvoiceList AS (
SELECT Year(InvoiceDate) as YearID, 
	   Month(InvoiceDate) as MonthID,
	   SUM(InvoiceAmount) as Total_InvoiceAmount,
       Year(InvoiceDate)*12+Month(InvoiceDate)as YearMonth	   
FROM Invoices
GROUP BY Year(InvoiceDate), Month(InvoiceDate))
SELECT I1.YearID, I1.MonthID,I1.YearMonth, SUM(I2.Total_InvoiceAmount) AS InvoiceAmount
FROM InvoiceList as I1
LEFT JOIN InvoiceList AS I2
    ON I1.YearMonth >= i2.YearMonth and I1.YearMonth <= i2.YearMonth+2
GROUP BY I1.YearID, I1.MonthID, I1.YearMonth
ORDER BY I1.YearID, I1.MonthID, I1.YearMonth
;


, SUM(InvoiceAmount)as Total_InvoiceAmount