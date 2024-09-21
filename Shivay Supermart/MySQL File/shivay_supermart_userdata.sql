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
-- Table structure for table `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userdata` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `account_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdata`
--

LOCK TABLES `userdata` WRITE;
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
INSERT INTO `userdata` VALUES (1,'aryansharma@gmail.com','ArySha','Ar789','Admin'),(2,'priyapatil@yahoo.com','PriPat','Pr456','Seller'),(3,'rahulkumar@gmail.com','RahKum','Ra789','Admin'),(4,'snehasingh@gmail.com','SneSin','Sn234','Seller'),(5,'rajatmishra@gmail.com','RajMis','Ra567','Admin'),(6,'shwetagupta@gmail.com','ShwGup','Sh234','Seller'),(7,'ankitjoshi@gmail.com','AnkJos','An567','Admin'),(8,'poojaverna@gmail.com','PooVer','Po123','Seller'),(9,'vikramyadav@gmail.com','VikYad','Vi456','Admin'),(10,'nehashah@gmail.com','NehSha','Ne789','Seller'),(11,'akashpandey@gmail.com','AkaPan','Ak234','Admin'),(12,'monajain@yahoo.com','MonJai','Mo567','Seller'),(13,'rohitsingh@gmail.com','RohSin','Ro123','Admin'),(14,'aishwaryarao@yahoo.com','AisRao','Ai456','Seller'),(15,'deepaknair@gmail.com','DeeNai','De789','Admin'),(16,'anushkasharma@gmail.com','AnuSha','An234','Seller'),(17,'ravithakur@yahoo.com','RavTha','Ra567','Admin'),(18,'divyamehra@gmail.com','DivMeh','Di123','Seller'),(19,'kunalgupta@gmail.com','KunGup','Ku456','Admin'),(20,'sarajkhan@yahoo.com','SarKha','Sa789','Seller'),(21,'rahulyadav@gmail.com','RahYad','Ra234','Admin'),(22,'anitasingh@gmail.com','AniSin','An567','Seller'),(23,'arjunverma@yahoo.com','ArjVer','Ar123','Admin'),(24,'nehakapoor@gmail.com','NehKap','Ne456','Seller'),(25,'vivekshah@gmail.com','VivSha','Vi789','Admin'),(26,'radhikarajput@yahoo.com','RadRaj','Ra234','Seller'),(27,'rajatkhanna@gmail.com','RajKha','Ra567','Admin'),(28,'simransingh@gmail.com','SimSin','Si123','Seller'),(29,'amitsharma@yahoo.com','AmiSha','Am456','Admin'),(30,'sureshverma@gmail.com','SurVer','Su567','Seller'),(31,'shivagr1367@gmail.com','ShiAgr','Sh1367','Admin'),(32,'decoderguy99@gmail.com','AnsAgr','An1367','Seller'),(57,'abcd@gmail.com','abcd','ab1234','Admin');
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-06 14:55:16
