-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: shivay_supermart
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `Product_ID` char(5) NOT NULL,
  `Category` varchar(50) DEFAULT NULL,
  `Product_Company` varchar(30) DEFAULT NULL,
  `Product_Name` varchar(40) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `product_status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('P001','Vegetables','FarmFresh','Carrots',50,100,'Available'),('P002','Fruits','OrchardDelight','Apples',120,150,'Available'),('P003','Snacks','Haldiram','Bhujia',30,200,'Available'),('P004','Snacks','Parle','Biscuits',20,150,'Available'),('P005','Snacks','Lays','Masala Chips',15,100,'Available'),('P006','Snacks','Britannia','Good Day Cookies',25,120,'Available'),('P007','Snacks','Kurkure','Spicy Twist',10,180,'Available'),('P008','Snacks','Amul','Butter Cookies',30,130,'Available'),('P009','Snacks','Maggi','Masala Noodles',20,250,'Available'),('P010','Snacks','Parle Agro','Frooti',15,300,'Available'),('P011','Snacks','Cadbury','Dairy Milk Silk',50,50,'Available'),('P012','Snacks','Tata','Tea Bags',40,100,'Available'),('P013','Personal Care','Dove','Body Wash',120,80,'Available'),('P014','Personal Care','Pantene','Shampoo',150,60,'Available'),('P015','Personal Care','Colgate','Toothpaste',50,100,'Available'),('P016','Personal Care','Nivea','Face Cream',180,40,'Available'),('P017','Personal Care','Garnier','Hair Conditioner',200,50,'Available'),('P018','Sanitation','Dettol','Hand Sanitizer',80,100,'Available'),('P019','Sanitation','Lifebuoy','Soap Bar',20,150,'Available'),('P020','Sanitation','Harpic','Toilet Cleaner',40,80,'Available'),('P021','Sanitation','Pears','Liquid Hand Wash',30,120,'Available'),('P022','Sanitation','Cif','Surface Cleaner',60,90,'Available'),('P023','Sanitation','Domex','Bathroom Cleaner',45,70,'Available'),('P024','Sanitation','Vim','Dishwashing Liquid',25,110,'Available'),('P025','Dairy','Amul','Milk',25,50,'Available'),('P026','Dairy','Mother Dairy','Curd',30,40,'Available'),('P027','Dairy','Gowardhan','Paneer',90,20,'Available'),('P028','Dairy','Nestle','Yogurt',15,60,'Available'),('P029','Dairy','Britannia','Cheese',80,30,'Available'),('P030','Dairy','Amul','Butter',50,45,'Available'),('P031','Dairy','Mother Dairy','Ice Cream',120,25,'Available');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-06 14:55:17
