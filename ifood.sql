DROP  DATABASE IF EXISTS IFOOD;
CREATE DATABASE IF NOT EXISTS IFOOD;
use IFOOD;
CREATE TABLE `CUSTOMER` (
	`phone_number` varchar(13) NOT NULL,
	`firstname` varchar(20) NOT NULL,
	`lastname` varchar(20) NOT NULL,
	`email` varchar(40) NOT NULL,
	`password` varchar(30) NOT NULL,
	`street` varchar(50) DEFAULT 'NULL',
	`street_number` INT(3),
	`zip` INT(5) NOT NULL DEFAULT '0',
	PRIMARY KEY (`phone_number`)
);

CREATE TABLE `RATING` (
	`rating_id` INT NOT NULL AUTO_INCREMENT,
	`rating` INT(1),
	`order_num` INT NOT NULL,
	PRIMARY KEY (`rating_id`)
);

CREATE TABLE `SHOP` (
	`TIN` INT(9) NOT NULL AUTO_INCREMENT,
	`shop_name` varchar(50) NOT NULL,
	`min_price` FLOAT DEFAULT '0',
	`zip` INT(5) DEFAULT '0',
	`street` varchar(50) DEFAULT '' '',
	`street_number` INT(3),
	`opening_time` TIME,
	`owner_name` varchar(50) DEFAULT 'NULL',
	`closing_time` TIME,
	PRIMARY KEY (`TIN`)
);

CREATE TABLE `PRODUCT` (
	`product_id` INT NOT NULL AUTO_INCREMENT,
	`product_name` varchar(20) NOT NULL,
	`price` FLOAT(4) NOT NULL,
	`TIN` INT(10) NOT NULL,
	`category_id` INT NOT NULL,
	PRIMARY KEY (`product_id`)
);

CREATE TABLE `CATEGORY` (
	`category_id` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(50) NOT NULL,
	PRIMARY KEY (`category_id`)
);

CREATE TABLE `ORDER` (
	`order_num` INT(50) NOT NULL AUTO_INCREMENT,
	`order_status` BOOLEAN NOT NULL,
	`price` FLOAT,
	`order_time` DATETIME NOT NULL,	
	`driver_id` INT NOT NULL,
	`phone_number` varchar(13) NOT NULL,
	PRIMARY KEY (`order_num`)
);

CREATE TABLE `DETAILS` (
	`order_num` INT NOT NULL ,
	`product_id` INT NOT NULL,
	`TIN` INT(9) NOT NULL,
	`quantity` INT NOT NULL,
	PRIMARY KEY (`order_num`,`product_id`)
);

CREATE TABLE `PAYMENT` (
	`payment_id` INT NOT NULL,
	`amount` FLOAT NOT NULL,
	`card_num` varchar(16) NOT NULL,
	`cvv` INT(3) NOT NULL,
	`card_name` varchar(50) NOT NULL,
	`coupon` varchar(10) DEFAULT 'NULL',
	`order_num` INT(16) NOT NULL,
	PRIMARY KEY (`payment_id`)
);

CREATE TABLE `DRIVER` (
	`driver_id` INT NOT NULL,
	`firstname` varchar(20) NOT NULL,
	`lastname` varchar(20) NOT NULL,
	`phone_number` varchar(12) NOT NULL,
	PRIMARY KEY (`driver_id`)
);

ALTER TABLE `RATING` ADD CONSTRAINT `RATING_fk0` FOREIGN KEY (`order_num`) REFERENCES `ORDER`(`order_num`);

ALTER TABLE `PRODUCT` ADD CONSTRAINT `PRODUCT_fk0` FOREIGN KEY (`TIN`) REFERENCES `SHOP`(`TIN`);

ALTER TABLE `PRODUCT` ADD CONSTRAINT `PRODUCT_fk1` FOREIGN KEY (`category_id`) REFERENCES `CATEGORY`(`category_id`);

ALTER TABLE `ORDER` ADD CONSTRAINT `ORDER_fk0` FOREIGN KEY (`driver_id`) REFERENCES `DRIVER`(`driver_id`);

ALTER TABLE `ORDER` ADD CONSTRAINT `ORDER_fk1` FOREIGN KEY (`phone_number`) REFERENCES `CUSTOMER`(`phone_number`);

ALTER TABLE `DETAILS` ADD CONSTRAINT `DETAILS_fk0` FOREIGN KEY (`order_num`) REFERENCES `ORDER`(`order_num`);

ALTER TABLE `DETAILS` ADD CONSTRAINT `DETAILS_fk1` FOREIGN KEY (`product_id`) REFERENCES `PRODUCT`(`product_id`);

ALTER TABLE `DETAILS` ADD CONSTRAINT `DETAILS_fk2` FOREIGN KEY (`TIN`) REFERENCES `SHOP`(`TIN`);

ALTER TABLE `PAYMENT` ADD CONSTRAINT `PAYMENT_fk0` FOREIGN KEY (`order_num`) REFERENCES `ORDER`(`order_num`);











SELECT @@GLOBAL.sql_mode global, @@SESSION.sql_mode session;
SET sql_mode = '';
SET GLOBAL sql_mode = '';
































