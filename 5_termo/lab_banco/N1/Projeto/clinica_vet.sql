CREATE DATABASE  IF NOT EXISTS `clinica_vet` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `clinica_vet`;
-- MySQL dump 10.13  Distrib 8.0.38, for Linux (x86_64)
--
-- Host: 172.17.0.2    Database: clinica_vet
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `agendamento`
--

DROP TABLE IF EXISTS `agendamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agendamento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_medico` int NOT NULL,
  `id_animal` int NOT NULL,
  `data_hora` datetime NOT NULL,
  `compareceu` char(1) NOT NULL,
  `concluido` char(1) NOT NULL,
  `valor` float NOT NULL,
  `pago` char(1) NOT NULL,
  `procedimento` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_animal` (`id_animal`),
  KEY `id_medico` (`id_medico`),
  CONSTRAINT `agendamento_ibfk_1` FOREIGN KEY (`id_animal`) REFERENCES `animal` (`id`),
  CONSTRAINT `agendamento_ibfk_2` FOREIGN KEY (`id_medico`) REFERENCES `medico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agendamento`
--

LOCK TABLES `agendamento` WRITE;
/*!40000 ALTER TABLE `agendamento` DISABLE KEYS */;
INSERT INTO `agendamento` VALUES (1,1,1,'2024-09-20 10:30:00','S','S',150,'S','Consulta de rotina'),(2,1,2,'2024-09-21 09:00:00','S','S',200,'S','Vacinação'),(3,2,3,'2024-09-21 14:00:00','N','N',250,'N','Exame de sangue'),(4,2,4,'2024-09-22 16:00:00','S','S',180,'S','Consulta de rotina'),(5,3,5,'2024-09-23 11:30:00','S','S',220,'S','Check-up'),(6,3,6,'2024-09-24 08:00:00','S','S',180,'S','Vacinação'),(7,1,7,'2024-09-25 13:30:00','S','S',150,'S','Consulta de rotina'),(8,2,8,'2024-09-26 09:45:00','N','N',200,'N','Exame de imagem'),(9,3,9,'2024-09-27 15:00:00','S','S',300,'S','Cirurgia de castração'),(10,1,10,'2024-09-28 17:00:00','S','S',120,'S','Consulta de rotina');
/*!40000 ALTER TABLE `agendamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `animal`
--

DROP TABLE IF EXISTS `animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(80) NOT NULL,
  `sexo` char(1) NOT NULL,
  `peso` float NOT NULL,
  `especie` varchar(60) NOT NULL,
  `raca` varchar(60) NOT NULL,
  `data_nascimento` date DEFAULT NULL,
  `id_cliente` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `animal_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal`
--

LOCK TABLES `animal` WRITE;
/*!40000 ALTER TABLE `animal` DISABLE KEYS */;
INSERT INTO `animal` VALUES (1,'Rex','M',25.5,'Cão','Labrador','2020-05-01',1),(2,'Bella','F',5.2,'Gato','Persa','2021-08-12',1),(3,'Thor','M',30,'Cão','Pastor Alemão','2019-11-22',2),(4,'Luna','F',3.8,'Gato','Siamês','2020-02-17',2),(5,'Max','M',18.4,'Cão','Beagle','2018-07-14',3),(6,'Mia','F',6.5,'Gato','Maine Coon','2022-03-11',3),(7,'Buddy','M',12,'Cão','Bulldog','2021-04-09',4),(8,'Sasha','F',4.2,'Gato','Bengal','2022-06-20',4),(9,'Charlie','M',22.5,'Cão','Golden Retriever','2019-09-15',5),(10,'Lola','F',4.7,'Gato','Sphynx','2021-11-03',5);
/*!40000 ALTER TABLE `animal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `endereco` varchar(150) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Denis Tofel','Denis@gmail.com','Rua: M','98745632105'),(2,'Laura Fitos','Laura@gmail.com','Rua: F','46145632805'),(3,'Saulo Drago','Saulo@gmail.com','Rua: T','95346319105'),(4,'Vitor West','VitorW@gmail.com','Rua: X','64755432105'),(5,'Brenda','Brenda@gmail.com','Rua: J','94608632705');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medico`
--

DROP TABLE IF EXISTS `medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medico` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `endereco` varchar(150) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `registro_profissional` varchar(20) DEFAULT NULL,
  `especialidade` varchar(100) NOT NULL,
  `carga_horaria_semanal` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medico`
--

LOCK TABLES `medico` WRITE;
/*!40000 ALTER TABLE `medico` DISABLE KEYS */;
INSERT INTO `medico` VALUES (1,'Carlos Petros','CarlosP@gmail.com','Rua: Y','12345678901','51790-3','Patologia',40),(2,'Pedro Tolp','Pedro_T@gmail.com','Rua: X','52645648501','65791-7','Oncologia',35),(3,'João Vils','JoãoVs@gmail.com','Rua: H','24348678300','21610-2','Nutrição',45),(4,'Vitor Edge','Vit_ed@gmail.com','Rua: W','16084346789','76115-7','Cardiologia',30);
/*!40000 ALTER TABLE `medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tel_cliente`
--

DROP TABLE IF EXISTS `tel_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tel_cliente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `telefone` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `tel_cliente_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tel_cliente`
--

LOCK TABLES `tel_cliente` WRITE;
/*!40000 ALTER TABLE `tel_cliente` DISABLE KEYS */;
INSERT INTO `tel_cliente` VALUES (1,1,'(14)5412-5101'),(2,2,'(14)1612-5150'),(3,3,'(14)4602-4181'),(4,4,'(14)7412-4191'),(5,5,'(14)4402-6701');
/*!40000 ALTER TABLE `tel_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tel_medico`
--

DROP TABLE IF EXISTS `tel_medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tel_medico` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_medico` int NOT NULL,
  `telefone` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_medico` (`id_medico`),
  CONSTRAINT `tel_medico_ibfk_1` FOREIGN KEY (`id_medico`) REFERENCES `medico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tel_medico`
--

LOCK TABLES `tel_medico` WRITE;
/*!40000 ALTER TABLE `tel_medico` DISABLE KEYS */;
INSERT INTO `tel_medico` VALUES (1,1,'(14)3468-1064'),(2,2,'(14)3668-1154'),(3,3,'(14)3766-1367'),(4,4,'(14)7468-1268');
/*!40000 ALTER TABLE `tel_medico` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-25 13:00:06
