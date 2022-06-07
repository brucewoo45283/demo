-- Retrieving the last row for each group in a table
https://www.youtube.com/watch?v=VJZpPgxd3zw&list=PLdHV54DK_E84O8Qe0X2cDpBmvjHuRn5Ee&index=1
CREATE TABLE tblHouseprices (
    PriceDate date NOT NULL,
 Region varchar(20) NOT NULL,
    price int NOT NULL);


INSERT INTO tblHouseprices 
VALUES
 ('2022-06-01', 'Greater Manchester', 346251),
 ('2022-07-01', 'East Midlands', 312289),
 ('2022-07-01', 'West Midlands', 365274),
 ('2022-08-01', 'East Midlands', 328072),
 ('2022-08-01', 'Greater Manchester', 353617),
 ('2022-09-01', 'East Midlands', 339697),
 ('2022-09-01', 'West Midlands', 370206),
 ('2022-09-01', 'Greater Manchester', 358902),
 ('2022-10-01', 'West Midlands', 376596),
 ('2022-10-01', 'Greater Manchester', 357744),
 ('2022-11-01', 'West Midlands', 371699);
 
 -- 內外表子查詢
 select * 
 from tblHouseprices as t
 where PriceDate=
     (select MAX(PriceDate)
	 from tblHouseprices as t1
	 where t.Region=t1.Region
	 )
;

-- 使用聚合函數，再self join結果到原表
select max(PriceDate) as MaxPriceDate, Region
from tblHouseprices
group by Region; -- 沒有顯示price欄位

select t.* 
from tblHouseprices as t
join 
(select max(PriceDate) as MaxPriceDate, Region
from tblHouseprices
group by Region) t1 on t.Region=t1.Region and t.PriceDate=t1.MaxPriceDate ;

-- ROW_NUMBER()
select * 
from tb1HousePrices
order by Region, PriceDate DESC; -- 將資料表排序


SELECT *, 
       ROW_NUMBER() OVER(PARTITION BY Region ORDER BY PriceDate DESC) AS MyRowNumber 
-- 整併Region欄位相同的為同一小組，再依組內PriceDate由大到小排序，將流水號塞入流水號欄位MyRowNumber
FROM tblHouseprices as t
--where ROW_NUMBER() OVER(PARTITION BY Region ORDER BY PriceDate DESC)=1 -- 取每組流水編號是1【即最大日期】← 不能直接取，要用CTE暫存寫法
ORDER BY Region, PriceDate DESC;


-- ROW_NUMBER() 搭配CTE，取出資料
WITH /*暫存表名稱*/ LHP AS
(
	SELECT *, 
	   ROW_NUMBER() OVER(PARTITION BY Region ORDER BY PriceDate DESC) AS MyRowNumber 
	FROM tblHouseprices 
)
SELECT * 
FROM LHP
WHERE MyRowNumber=1 -- 取出每組流水號是1的資料
ORDER BY Region, PriceDate DESC
;