-- GROUP DATE DATA INTO QUARTERS, EVERY 2, 4, 6 MONTHS
 DROP TABLE IF EXISTS Invoices;
CREATE TABLE Invoices
(InvoiceDate date,
InvoiceAmount int);
INSERT INTO Invoices
VALUES
('2022-12-01', 1), ('2023-02-01', 1), ('2023-02-15', 1),
('2023-03-01', 3), ('2023-04-01', 2), ('2023-04-15', 2),
('2023-05-01', 5), ('2023-06-01', 3), ('2023-06-15', 3), 
('2023-08-01', 8), ('2023-09-01', 1), ('2023-10-01', 2),
('2023-11-01', 3), ('2023-12-01', 4), ('2024-01-01', 1);
SELECT InvoiceDate, InvoiceAmount
FROM Invoices;
-- 處理date格式，日期轉季度並匯總計算
select YEAR(InvoiceDate) as DateYear,
       datepart(QUARTER, InvoiceDate) as DateQuarter,
	   sum(InvoiceAmount) as Total
FROM Invoices
GROUP BY YEAR(InvoiceDate), datepart(QUARTER, InvoiceDate) 
order by DateYear, DateQuarter
;

-- 合併年欄位跟季欄位，並日期轉字串 DateQuarter
-- 每季1：比較複雜
select convert(varchar(4), YEAR(InvoiceDate))+ 'Q'+
       convert(varchar(4), datepart(QUARTER, InvoiceDate)) as DateQuarter,
	   sum(InvoiceAmount) as Total
FROM Invoices
GROUP BY YEAR(InvoiceDate), datepart(QUARTER, InvoiceDate) 
;

-- 每季2：建議用這個
select YEAR(InvoiceDate) as DateYear,
       month(InvoiceDate) as DateMonth,
	   month(InvoiceDate)/3 as DateQuarter1,
	   (month(InvoiceDate)+2)/3 as DateQuarter,  -- 加2再除3，才是我要的"季"結果
	   sum(InvoiceAmount) as Total
FROM Invoices
GROUP BY YEAR(InvoiceDate),  month(InvoiceDate),month(InvoiceDate)/3, (month(InvoiceDate)+2)/3 
order by DateYear, DateMonth, DateQuarter1,DateQuarter
;

-- 每三個月 (DatePeriod)

select YEAR(InvoiceDate) as DateYear,
	   (month(InvoiceDate)+1)/2 as DatePeriod,  
	   sum(InvoiceAmount) as Total
FROM Invoices
GROUP BY YEAR(InvoiceDate),  (month(InvoiceDate)+1)/2 
order by DateYear, DatePeriod
;