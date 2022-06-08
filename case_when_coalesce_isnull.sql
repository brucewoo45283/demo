https://www.youtube.com/watch?v=EwVMA36g9GQ&list=PLdHV54DK_E84O8Qe0X2cDpBmvjHuRn5Ee&index=3
-- join 兩張資料表時，用三種方法來處理null值
CREATE VIEW view1 as 
SELECT object_id, name, create_date, schema_id
FROM sys.objects
WHERE object_ID BETWEEN 1 AND 9
GO

CREATE VIEW view2 AS 
SELECT object_id, name, modify_date, schema_id
FROM sys.objects
WHERE object_ID BETWEEN 6 AND 17
GO

-- 不能用union，因為兩張表有不同欄位
-- left join
 select * from view1 as t1
 left join view2 as t2 on t1.object_id=t2.object_id;
 
 -- full join
  select * from view1 as t1
 full join view2 as t2 on t1.object_id=t2.object_id;
 
 -- 把object_id是null的資料刪掉
 -- 用case when, coalesce, isnull, isnull
 -- http://sharedderrick.blogspot.com/2012/06/t-sql-coalesce.html  coalesce函數
 select case when t1.object_id is null then t2.object_id
        else t1.object_id end as object_id,
		coalesce(t1.name, t2.name) as [name]
		isnull(t1.schema_id, t2.schema_id) as [schema_id]
		create_date,
		modify_date
 from view1 as t1
     full join view2 as t2
   on t1.object_id=t2.object_id
 ;