-- Create database and tables for alx_book_store

CREATE DATABASE IF NOT EXISTS `alx_book_store`;
USE `alx_book_store`;

CREATE TABLE IF NOT EXISTS `authors` (
  `author_id` INT PRIMARY KEY AUTO_INCREMENT,
  `author_name` VARCHAR(215) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `books` (
  `book_id` INT PRIMARY KEY AUTO_INCREMENT,
  `title` VARCHAR(130) NOT NULL,
  `author_id` INT,
  `price` DOUBLE,
  `publication_date` DATE,
  FOREIGN KEY (`author_id`) REFERENCES `authors`(`author_id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `customers` (
  `customer_id` INT PRIMARY KEY,
  `customer_name` VARCHAR(215) NOT NULL,
  `email` VARCHAR(215),
  `address` TEXT
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` INT PRIMARY KEY AUTO_INCREMENT,
  `customer_id` INT,
  `order_date` DATE,
  FOREIGN KEY (`customer_id`) REFERENCES `customers`(`customer_id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `order_details` (
  `orderdetailid` INT PRIMARY KEY AUTO_INCREMENT,
  `order_id` INT,
  `book_id` INT,
  `quantity` DOUBLE,
  FOREIGN KEY (`order_id`) REFERENCES `orders`(`order_id`),
  FOREIGN KEY (`book_id`) REFERENCES `books`(`book_id`)
) ENGINE=InnoDB;
