--  find all of the orders which includes both hot and cold items

DROP TABLE IF EXISTS Orders
CREATE TABLE Orders
(OrderID int,
OrderType varchar(20),
OrderCost decimal(7,2))
INSERT INTO Orders VALUES
(1, 'Hot', 4.56),
(1, 'Cold', 1.24),
(2, 'Hot', 5.12),
(3, 'Cold', 0.99),
(4, 'Hot', 4.54),
(4, 'Hot', 6.98),
(4, 'Cold', 2.24);

SELECT *
FROM Orders;

-- 我要找出同時有冷飲、熱飲(OrderType)的訂單(OrderID)
-- 取交集 intersect
select OrderID
from Orders
where OrderType='Hot'
intersect
select OrderID
from Orders
where OrderType='Cold'
;      

-- 子查詢
select * from Orders
where OrderID IN
   (select OrderID from Orders
    where OrderType='Hot')
AND OrderID IN
   (select OrderID from Orders
    where OrderType='Cold')
;


-- 樞紐分析 pivot
select OrderID, Hot, Cold
from Orders
PIVOT
(SUM(OrderCost) for OrderType in (Hot, Cold)) as pvt
;

-- 刪掉樞紐分析表中hot欄位、cold欄位是null值的資料
select OrderID, Hot, Cold
from Orders
PIVOT
(SUM(OrderCost) for OrderType in (Hot, Cold)) as pvt
where Hot is not null 
and Cold is not null
;




