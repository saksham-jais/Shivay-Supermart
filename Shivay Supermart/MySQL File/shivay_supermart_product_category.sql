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
-- Table structure for table `product_category`
--

DROP TABLE IF EXISTS `product_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_category` (
  `Serial_Number` char(3) NOT NULL,
  `Category_Name` text,
  `Total_Products` int DEFAULT NULL,
  `Description` text,
  PRIMARY KEY (`Serial_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_category`
--

LOCK TABLES `product_category` WRITE;
/*!40000 ALTER TABLE `product_category` DISABLE KEYS */;
INSERT INTO `product_category` VALUES ('1','Vegetable',1,'Vegetables are nutrient-rich plants, vital for a healthy diet. From leafy greens to root vegetables, they provide essential vitamins and minerals. Versatile and flavorful, vegetables enhance diverse cuisines while promoting overall well-being.'),('2','Fruits',1,'Fruits, natures sweet offerings, are rich in vitamins and antioxidants, supporting a balanced diet. From juicy berries to tropical delights, they provide essential nutrients and delightful flavors, contributing to overall health and wellness.'),('3','Snacks',10,'Convenient and flavorful, snacks offer a variety of tasty options. From crunchy chips to savory cookies, they provide quick indulgence, making snack time enjoyable.'),('4','Personal Care',5,'Essential for hygiene and grooming, personal care products like soaps, shampoos, and lotions contribute to cleanliness and well-being, promoting a healthy lifestyle.'),('5','Sanitation',7,'Sanitation products, such as hand sanitizers, soaps, and cleaners, play a crucial role in maintaining hygiene. Effectively combating germs and ensuring cleanliness, these products contribute to a healthy environment, supporting overall well-being and preventing the spread of infections.'),('6','Dairy',7,'Dairy products, including milk, cheese, and yogurt, are nutrient-rich sources of calcium and protein. Supporting bone health and digestion, they are versatile and delicious additions to a balanced diet.');
/*!40000 ALTER TABLE `product_category` ENABLE KEYS */;
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
