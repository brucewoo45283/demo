-- https://www.youtube.com/watch?v=gvRXjsrpCHw
CREATE DATABASE `sql_demo1`;
SHOW DATABASES;
USE `sql_demo1`;

-- 建立資料表綱要
CREATE TABLE `student`(
`student_id` INT PRIMARY KEY,
`name` VARCHAR(20),     /*VARCHAR(20):20個字的字串*/
`major` VARCHAR(20)
);

DESCRIBE `student`;
-- 新增表格屬性
/*DECIMAL(總共有3位數,小數點後面有2位)*/;
ALTER TABLE `student` ADD gpa DECIMAL(3,2);

-- 刪掉表格屬性
ALTER TABLE `student` DROP COLUMN gpa;

-- 塞入資料
INSERT INTO `student` VALUES(1, "鳴人", "九尾妖狐");
INSERT INTO `student` VALUES(2, "佐助", "血輪眼");

-- 依自訂順序塞入資料
INSERT INTO `student`(`name`, `major`, `student_id`) VALUES("卡卡西", "雷切", "3");

-- 篩選資料表所有欄位的資料
SELECT * FROM `student`;

-- constraints 限制 約束*
-- 每次更動，都要drop本來的資料表，再重新創建
DROP TABLE `student`;

CREATE TABLE `student`(
`student_id` INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(20) NOT NULL,           # VARCHAR(20):20個字的字串
`major` VARCHAR(20) DEFAULT "忍者學校" # 細格的，預設值
);
INSERT INTO `student` VALUES(1, "鳴人", "九尾妖狐");
INSERT INTO `student` VALUES(2, "佐助", "血輪眼");
INSERT INTO `student`(`name`, `major`, `student_id`) VALUES("卡卡西", "雷切", "3");
INSERT INTO `student`(`name`) VALUES("寧次");   # AUTO_INCREMENT，所以不用再設ID，自動設序號
SELECT * FROM `student`;

-- 修改、刪除資料
-- 把workbench預設的更新模式給關閉
SET SQL_SAFE_UPDATES = 0;
DROP TABLE `student`;
CREATE TABLE `student`(
`id` INT AUTO_INCREMENT,
`name` VARCHAR(20) NOT NULL,     
`major` VARCHAR(20) DEFAULT "歷史系" ,
`score` INT ,
PRIMARY KEY(`id`)
);
INSERT INTO `student` VALUES(1, "小白", "英文", 50);
INSERT INTO `student` VALUES(2, "小黃", "生物", 90);
INSERT INTO `student` VALUES(3, "小綠", "歷史", 70);
INSERT INTO `student` VALUES(4, "小藍", "英語", 80);
INSERT INTO `student` VALUES(5, "小黑", "化學", 20);
SELECT * FROM `student`;

-- 把資料表內某個值統一修改
UPDATE `student`                             # 更新的資料表名稱
SET `major` = "應用外文系"                   # 修改後的值
WHERE `major` = "英文" OR `major` = "英語";  # 想要更新的值
SELECT * FROM `student`;

-- 把資料表所有值統一修改為特定值
UPDATE `student`                             # 更新的資料表名稱
SET `major` = "死當";                         # 修改後的值
SELECT * FROM `student`;

-- 根據id刪除資料
DELETE FROM `student`
WHERE `id` = 5;
SELECT * FROM `student`;

-- 根據條件刪除資料
DELETE FROM `student`
WHERE `score` <= 60;
SELECT * FROM `student`;

-- 篩選資料
DROP TABLE `student`;
CREATE TABLE `student`(
`id` INT AUTO_INCREMENT,
`name` VARCHAR(20) NOT NULL,     
`major` VARCHAR(20) DEFAULT "歷史系" ,
`score` INT ,
PRIMARY KEY(`id`)
);
INSERT INTO `student` VALUES(1, "小白", "英文", 80);
INSERT INTO `student` VALUES(2, "小黃", "生物", 90);
INSERT INTO `student` VALUES(3, "小綠", "歷史", 70);
INSERT INTO `student` VALUES(4, "小藍", "英語", 80);
INSERT INTO `student` VALUES(5, "小黑", "化學", 20);
INSERT INTO `student` VALUES(6, "館長", "體育", 100);
INSERT INTO `student` VALUES(7, "小施", "體育", 30);
INSERT INTO `student` VALUES(8, "小吳", "生物", 30);
SELECT * FROM `student`;
-- 排序 DESC, ASC 
SELECT * 
FROM `student`
ORDER BY `score` DESC;

-- 多個屬性先後排序 ， 先根據條件一、再根據條件二
SELECT * 
FROM `student`
ORDER BY `score` DESC, `id` DESC
LIMIT 2;     # 只取前兩筆

-- 條件交集
SELECT * 
FROM `student`
WHERE `major`= "英語"and`name`= "小藍";

-- 條件聯集
SELECT * 
FROM `student`
WHERE `major`= "英語"or`name`= "小白";

-- 條件聯集2:撈取同欄位的不同值 
SELECT * 
FROM `student`
WHERE `major` IN("英文", "英語", "體育");




