-- 創建資料庫
SHOW DATABASES;
USE `sql_demo1`;

-- 員工
CREATE TABLE `employee`(
	`emp_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `birth_date` DATE,
    `sex` VARCHAR(1),
    `salary` INT,
    `branch_id` INT,
    `sup_id` INT
);


-- 部門(研發、行政、資訊)
CREATE TABLE `branch`(
	`branch_id` INT PRIMARY KEY,
    `branch_name` VARCHAR(20),
    `manager_id` INT,
    FOREIGN KEY (`manager_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL  # ON DELETE SET NULL → 如果`emp_id`被刪掉，我就把另一個關聯到的資料表`manager_id`欄位設為NULL
);


-- 創好部門資料表後，才能回頭在員工`employee`表格進行`branch_id`欄位與`sup_id`欄位之FOREIGN KEY設定
ALTER TABLE `employee`
ADD FOREIGN KEY(`branch_id`)     # 新增`branch_id`之FOREIGN KEY
REFERENCES `branch`(`branch_id`) # 對應在branch資料表的某欄位
ON DELETE SET NULL;

ALTER TABLE `employee`  
ADD FOREIGN KEY(`sup_id`)            # 新增`sup_id`之FOREIGN KEY
REFERENCES `employee`(`emp_id`)      # 對應在employee資料表的某欄位
ON DELETE SET NULL;


-- 創客戶表格
CREATE TABLE `client`(
	`client_id` INT PRIMARY KEY,
    `client_name` VARCHAR(20),
    `phone` VARCHAR(20)
);


-- 創資料表works_with`，設定`emp_id`, `client_id`為primary key，同時也是FOREIGN KEY
CREATE TABLE `works_with`(
	`emp_id` INT,
    `client_id` INT,
    `total_sales` INT,
    PRIMARY KEY(`emp_id`, `client_id`),
    FOREIGN KEY (`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
    FOREIGN KEY (`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
);


-- 插入`branch`資料
INSERT INTO `branch` VALUES(1, '研發', NULL);
INSERT INTO `branch` VALUES(2, '行政', NULL);
INSERT INTO `branch` VALUES(3, '資訊', NULL);

-- 插入`employee`資料
INSERT INTO `employee` VALUES(206, '小黃', '1998-10-08', 'F', 50000, 1, NULL);
INSERT INTO `employee` VALUES(207, '小綠', '1985-09-16', 'M', 29000, 2, 206);
INSERT INTO `employee` VALUES(208, '小黑', '2000-12-19', 'M', 35000, 3, 206);
INSERT INTO `employee` VALUES(209, '小白', '1997-01-22', 'F', 39000, 3, 207);
INSERT INTO `employee` VALUES(210, '小蘭', '1925-11-10', 'F', 84000, 1, 207);
INSERT INTO `employee` VALUES(211, '鳴人', '1994-11-10', 'M', 84000, 2, 208);
INSERT INTO `employee` VALUES(212, '佐助', '1998-10-08', 'M', 89000, 1, 207);


UPDATE `branch`
SET `manager_id` = 206
WHERE `branch_id` = 1;

UPDATE `branch`
SET `manager_id` = 207
WHERE `branch_id` = 2;

UPDATE `branch`
SET `manager_id` = 208
WHERE `branch_id` = 3;


INSERT INTO `client` VALUES(400, '阿狗', '254354335');
INSERT INTO `client` VALUES(401, '阿貓', '25633899');
INSERT INTO `client` VALUES(402, '旺來', '45354345');
INSERT INTO `client` VALUES(403, '露西', '54354365');
INSERT INTO `client` VALUES(404, '艾瑞克', '18783783');


INSERT INTO `works_with` VALUES(206, 400, 70000);
INSERT INTO `works_with` VALUES(207, 401, 24000);
INSERT INTO `works_with` VALUES(208, 402, 9800);
INSERT INTO `works_with` VALUES(208, 403, 24000);
INSERT INTO `works_with` VALUES(210, 404, 87940);

SELECT * FROM `employee`;
SELECT * FROM `branch`;
SELECT * FROM `client`;
SELECT * FROM `works_with`;

-- 刪除所有表的 SQL 查詢
-- https://www.delftstack.com/zh-tw/howto/mysql/how-to-drop-all-tables-in-mysql/#%E5%88%AA%E9%99%A4%E6%89%80%E6%9C%89%E8%A1%A8%E7%9A%84-sql-%E6%9F%A5%E8%A9%A2
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE `employee`;
DROP TABLE `branch`;
DROP TABLE `client`;
DROP TABLE `works_with`;
SET FOREIGN_KEY_CHECKS = 1;

-- 取得所有員工資料
SELECT * FROM `employee`;

-- 取得所有客戶資料
SELECT * FROM `client`;

-- 按薪水高低取得員工資料
SELECT * 
FROM `employee`
ORDER BY `salary` DESC;

-- 取得薪水前三高的員工
SELECT * 
FROM `employee`
ORDER BY `salary` DESC
LIMIT 3; 

-- 取得種類
SELECT DISTINCT `sex` FROM `employee`;

-- 聚合函數aggregate functions
-- 1.取得員工人數 COUNT(*)
SELECT COUNT(*) FROM `employee`;

-- 2.依條件取出筆數:
-- 出生於1970-1-1以後的女性員工有幾人?
SELECT COUNT(*) # 篩選 
FROM `employee` # 哪個表格
WHERE `birth_date` > "1970-01-01" AND `sex` = "F";   #取的條件

-- 3.員工的平均薪水 AVG(`欄位`)
SELECT AVG(`salary`) FROM `employee`;

-- 4.員工的薪水總和 SUM(`欄位`)
SELECT SUM(`salary`) FROM `employee`;

-- 5.薪水最高vs最低的員工 MAX(`欄位`) MIN(`欄位`)
SELECT MAX(`salary`) FROM `employee`;
SELECT MIN(`salary`) FROM `employee`;

-- 萬用字元 wildcards: 類似正規表達法
# %表多個字元， _ 代表一個字元
-- 1. 取得電話號碼尾數是335的客戶
-- EX1
SELECT *
FROM `client`
WHERE `phone` LIKE "%335";
-- EX2
SELECT *
FROM `client`
WHERE `phone` LIKE "%354%";

-- 2. 取得姓艾的客戶
SELECT *
FROM `client`
WHERE `client_name` LIKE "艾%";

-- 3. 取得生日在12月的員工 
# 觀察birth_date欄位：五個字元、接月份、後面任意多個字元
SELECT *
FROM `employee`
WHERE `birth_date` LIKE "_____12%"; # 五個底線

-- union 聯集：目的為合併查詢結果

-- 1. 合併客戶名字、員工名字之搜尋結果(資料型態要一樣)
SELECT `name`
FROM `employee`
UNION
SELECT `client_name`
FROM `client`;

-- 2. [員工id + 員工名字] 合併  [客戶id + 客戶名字] ，並自己命名新欄位
SELECT `emp_id` AS `new_id`, `name` AS `new_name`
FROM `employee`
UNION
SELECT `client_id`, `client_name`
FROM `client`;

-- 3. 員工薪水 合併 銷售金額
SELECT `salary` AS `new_money`
FROM `employee`
UNION
SELECT `total_sales`
FROM `works_with`;

-- join : 串聯兩個表格
INSERT INTO `branch` VALUES(4, "偷懶", NULL);
-- 取得所有部門經理的名字、串聯員工表格、客戶表格
SELECT *
FROM `employee`
LEFT JOIN `branch`              #左邊的表格全部回傳
ON `employee`.`emp_id` = `branch`.`manager_id`;  #屬性的前面要加上表格名稱，避免合併後有兩個一樣的欄位名稱

-- subquery 子查詢

-- 1. 找出研發部門的經理名字
# 我必須要先在部門表格查出經理id，再利用此查詢結果去員工表格反查出結果
# 先寫子查詢、再縮排進主查詢
SELECT `name`
FROM `employee`
WHERE `emp_id`
 = (
SELECT `manager_id`
FROM `branch`
WHERE `branch_name`= "研發"
);

-- 2. 單一客戶銷售>50000的員工?
SELECT `name`
FROM `employee`
WHERE `emp_id` IN(
	SELECT `emp_id`
	FROM `workS_with`
	WHERE `total_sales`> 50000
);




