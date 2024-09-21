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
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `EmployeeID` char(4) NOT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `gender` char(6) DEFAULT NULL,
  `HireDate` date DEFAULT NULL,
  `JobTitle` varchar(100) DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('E825','Rashika ','Tiwari','RasTiw','Ra2608','2006-10-30','None','2024-01-06','Admin',80000.00,'rashikatiwari626@gmail.com','9016477236','Imarti Road , Mirzapur'),('E001','Aryan','Sharma','ArySha','Ar123','1990-05-15','Male','2022-01-01','Admin',50000.00,'aryansharma@gmail.com','9876543210','123, Main Street, Delhi'),('E002','Priya','Patil','PriPat','Pr456','1992-08-22','Female','2022-02-15','Seller',40000.00,'priyapatil@yahoo.com','8765432109','456, Market Street, Mumbai'),('E003','Rahul','Kumar','RahKum','Ra789','1995-03-10','Male','2022-03-20','Admin',55000.00,'rahulkumar@gmail.com','7654321098','789, Lane Street, Bangalore'),('E004','Sneha','Singh','SneSin','Sn234','1988-12-05','Female','2022-04-10','Seller',48000.00,'snehasingh@gmail.com','9087654321','567, Garden Road, Kolkata'),('E005','Rajat','Mishra','RajMis','Ra567','1991-06-18','Male','2022-05-15','Admin',60000.00,'rajatmishra@yahoo.com','7890123456','890, Hill Street, Chennai'),('E006','Shweta','Gupta','ShwGup','Sh234','1989-11-30','Female','2022-06-20','Seller',45000.00,'shwetagupta@gmail.com','9876543211','234, River View, Pune'),('E007','Ankit','Joshi','AnkJos','An567','1994-02-25','Male','2022-07-25','Admin',52000.00,'ankitjoshi@yahoo.com','8765432102','345, Skyline Avenue, Jaipur'),('E008','Pooja','Verma','PooVer','Po123','1993-09-15','Female','2022-08-30','Seller',48000.00,'poojaverma@gmail.com','7654321099','456, Harmony Street, Chandigarh'),('E009','Vikram','Yadav','VikYad','Vi456','1990-04-12','Male','2022-09-10','Admin',58000.00,'vikramyadav@yahoo.com','8901234567','567, Green Lane, Lucknow'),('E010','Neha','Shah','NehSha','Ne789','1988-07-08','Female','2022-10-15','Seller',47000.00,'nehashah@gmail.com','9012345678','678, Serenity Road, Ahmedabad'),('E011','Akash','Pandey','AkaPan','Ak234','1991-01-20','Male','2022-11-20','Admin',54000.00,'akashpandey@gmail.com','9876543213','789, Sunrise Street, Bhopal'),('E012','Mona','Jain','MonJai','Mo567','1994-06-05','Female','2022-12-25','Seller',46000.00,'monajain@yahoo.com','8765432103','890, Ocean View, Kolkata'),('E013','Rohit','Singh','RohSin','Ro123','1989-03-18','Male','2023-01-01','Admin',56000.00,'rohitsingh@gmail.com','7654321100','123, Royal Avenue, Jaipur'),('E014','Aishwarya','Rao','AisRao','Ai456','1993-08-22','Female','2023-02-05','Seller',49000.00,'aishwaryarao@yahoo.com','8901234569','234, Tranquil Street, Mumbai'),('E015','Deepak','Nair','DeeNai','De789','1990-11-15','Male','2023-03-10','Admin',59000.00,'deepaknair@gmail.com','9012345679','345, Harmony Lane, Delhi'),('E016','Anushka','Sharma','AnuSha','An234','1988-04-30','Female','2023-04-15','Seller',48000.00,'anushkasharma@gmail.com','9876543214','456, Sunset Road, Chennai'),('E017','Ravi','Thakur','RavTha','Ra567','1992-09-25','Male','2023-05-20','Admin',57000.00,'ravithakur@yahoo.com','8765432104','567, Park View, Pune'),('E018','Divya','Mehra','DivMeh','Di123','1991-12-10','Female','2023-06-25','Seller',46000.00,'divyamehra@gmail.com','8901234578','678, Maple Street, Bangalore'),('E019','Kunal','Gupta','KunGup','Ku456','1993-07-18','Male','2023-07-30','Admin',55000.00,'kunalgupta@gmail.com','9012345680','789, River Bank, Kolkata'),('E020','Sara','Khan','SarKha','Sa789','1989-02-20','Female','2023-08-05','Seller',47000.00,'sarajkhan@yahoo.com','9876543215','890, Bliss Street, Jaipur'),('E021','Rahul','Yadav','RahYad','Ra234','1994-05-15','Male','2023-09-10','Admin',56000.00,'rahulyadav@gmail.com','8765432105','123, Serene Lane, Mumbai'),('E022','Anita','Singh','AniSin','An567','1990-10-30','Female','2023-10-15','Seller',48000.00,'anitasingh@gmail.com','8901234579','234, Tranquil Street, Delhi'),('E023','Arjun','Verma','ArjVer','Ar123','1991-03-18','Male','2023-11-20','Admin',57000.00,'arjunverma@yahoo.com','9012345681','345, Sunset Road, Bangalore'),('E024','Neha','Kapoor','NehKap','Ne456','1993-06-05','Female','2023-12-25','Seller',49000.00,'nehakapoor@gmail.com','9876543216','456, Harmony Lane, Pune'),('E025','Vivek','Shah','VivSha','Vi789','1988-09-18','Male','2024-01-01','Admin',58000.00,'vivekshah@gmail.com','8765432106','567, Park View, Chennai'),('E026','Radhika','Rajput','RadRaj','Ra234','1990-02-15','Female','2024-02-05','Seller',47000.00,'radhikarajput@yahoo.com','8901234580','678, Maple Street, Mumbai'),('E027','Rajat','Khanna','RajKha','Ra567','1992-07-08','Male','2024-03-10','Admin',56000.00,'rajatkhanna@gmail.com','9012345682','789, River Bank, Pune'),('E028','Simran','Singh','SimSin','Si123','1993-04-12','Female','2024-04-15','Seller',48000.00,'simransingh@gmail.com','9876543217','890, Bliss Street, Kolkata'),('E029','Amit','Sharma','AmiSha','Am456','1995-01-20','Male','2024-05-20','Admin',57000.00,'amitsharma@yahoo.com','8765432107','123, Serene Lane, Delhi'),('E030','Suresh','Verma','SurVer','Su567','1987-07-28','Male','2022-10-20','Seller',47000.00,'sureshverma@gmail.com','8765432190','890, Mountain View, Chandigarh'),('E031','Shivansh','Agrahari','ShiAgr','Sh1367','2007-06-13','Male','2023-01-06','Admin',70000.00,'shivagr1367@gmail.com','8299639765','18 , Siddhi Vinayak Colony , Mirzapur , Uttar Pradesh'),('E032','Ansh','Agrahari','AnsAgr','An1367','2007-06-13','Male','2023-01-06','Seller',40000.00,'decoderguy99@gmail.com','7080620446','18 , Siddhi Vinayak Colony , Mirzapur');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
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
