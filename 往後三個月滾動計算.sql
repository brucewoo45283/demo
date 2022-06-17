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

--【題目：2022年12月、2023年1月、2023年2月 三個月加總、往後三個月滾動計算】

-- 提取年、月
select YEAR(InvoiceDate) as InvYear,
       MONTH(InvoiceDate) as InvMonth,
	   InvoiceAmount
from Invoices;

-- 把年月處理產生新年月欄位InvCalc【解決跨年加減問題】
select YEAR(InvoiceDate) as InvYear,
       MONTH(InvoiceDate) as InvMonth,
	   InvoiceAmount,
	   YEAR(InvoiceDate)*12+MONTH(InvoiceDate) as InvCalc
from Invoices;

-- CTE
WITH Monthly AS
(
select YEAR(InvoiceDate) as InvYear,
       MONTH(InvoiceDate) as InvMonth,
	   InvoiceAmount,
	   YEAR(InvoiceDate)*12+MONTH(InvoiceDate) as InvCalc
from Invoices
)
select * from Monthly
where InvCalc between 24276 and 24278 -- 卡條件 2022/12月 ~ 2023/2月
;

-- 使用子查詢呈現結果 【滾動三個月欄位Three_Month_Total】
WITH Monthly AS -- 外表 Monthly t1
(
select YEAR(InvoiceDate) as InvYear,
       MONTH(InvoiceDate) as InvMonth,
	   InvoiceAmount,
	   YEAR(InvoiceDate)*12+MONTH(InvoiceDate) as InvCalc
from Invoices
)
select * ,
       (select sum(InvoiceAmount) 
	    from Monthly as t2 -- 內表取名t2
		where t2.InvCalc between t1.InvCalc and t1.InvCalc+2) as Three_Month_Total
from Monthly as t1
;

-- 不要select *
WITH Monthly AS -- 外表 Monthly t1
(
select YEAR(InvoiceDate) as InvYear,
       MONTH(InvoiceDate) as InvMonth,
	   InvoiceAmount,
	   YEAR(InvoiceDate)*12+MONTH(InvoiceDate) as InvCalc
from Invoices
)
select distinct InvYear, 
                InvMonth, 
				InvCalc,
			   (select sum(InvoiceAmount) 
				from Monthly as t2      -- 內表取名t2
				where t2.InvCalc between t1.InvCalc and t1.InvCalc+2) as Three_Month_Total
from Monthly as t1
;

-- ROW_NUMBER & 還原年分
WITH Monthly AS 
(
select YEAR(InvoiceDate) as InvYear,
       MONTH(InvoiceDate) as InvMonth,
	   InvoiceAmount,
	   YEAR(InvoiceDate)*12+MONTH(InvoiceDate) as InvCalc
from Invoices
),
MonthNumbers as
(SELECT ROW_NUMBER() OVER(ORDER BY InvoiceDate)+24275 as InvCalc from Invoices)
select  InvCalc,
         (InvCalc-1)/12 as NewYear,
		 ((InvCalc-1)%12)+1 as NewMonth,
		   (select sum(InvoiceAmount) 
			from Monthly as t2      -- 內表取名t2
			where t2.InvCalc between t1.InvCalc and t1.InvCalc+2) as Three_Month_Total
from MonthNumbers as t1
where (
    select sum(InvoiceAmount) 
	from Monthly as t2
	where t2.InvCalc between t1.InvCalc and t1.InvCalc+2
) IS NOT NULL
;
