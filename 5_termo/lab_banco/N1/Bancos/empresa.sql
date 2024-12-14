CREATE DATABASE  IF NOT EXISTS `empresa` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `empresa`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: empresa
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `departamentos`
--

DROP TABLE IF EXISTS `departamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamentos` (
  `id` int NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `sala` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamentos`
--

LOCK TABLES `departamentos` WRITE;
/*!40000 ALTER TABLE `departamentos` DISABLE KEYS */;
INSERT INTO `departamentos` VALUES (2,'Contabilidade','Sala 5'),(3,'Marketing','Sala 2'),(4,'Pesquisa','Sala 7'),(5,'Desenvolvimento','Sala 6'),(6,'Teste','Sala 3'),(7,'Suporte','Sala 4'),(9,'Recursos Humanos','Sala 9');
/*!40000 ALTER TABLE `departamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `numf` int NOT NULL,
  `depto_id` int NOT NULL,
  `rg` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `cpf` varchar(14) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `nome` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `endereco` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `salario` float DEFAULT NULL,
  `id_supervisor` int DEFAULT NULL,
  PRIMARY KEY (`numf`),
  KEY `depto_id` (`depto_id`),
  KEY `id_supervisor` (`id_supervisor`),
  CONSTRAINT `funcionarios_ibfk_1` FOREIGN KEY (`depto_id`) REFERENCES `departamentos` (`id`),
  CONSTRAINT `funcionarios_ibfk_2` FOREIGN KEY (`id_supervisor`) REFERENCES `funcionarios` (`numf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (3,2,'12345','098765','João Santos','Rua Y',1500,NULL),(4,2,'8709821','878721314','Pedro da Silva','Rua A',1000,3),(5,3,'3532523','54515151','Carlos Matos','Rua tatu',2000,NULL),(6,3,'41545','54178879784','Fabio Tutes','Rua Mirus',1500,5),(7,3,'65618741','78942350','Julio garcia','Rua Torta',1700,5),(8,4,'1511021','45515151','Jonas Melo','Rua K',3000,NULL),(9,4,'51521515','5515151','Dener Visto','Rua Ford',2000,8),(10,4,'415178','96482165','Salu Krap','Rua Apud',1800,8),(11,5,'651152','111150146','Edival Ald','Rua Fabi',4000,NULL),(12,5,'541555','15151515','Lumir Chaves','Rua Fig',2500,11),(13,5,'55215155','155145515','Julia Gomes','Rua Tupi',2200,11),(14,6,'262626','8748474','Fralu Lip','Rua Jop',6000,NULL),(15,6,'87115155','415445515','Carla Nuna','Rua Quad',3500,14),(16,6,'15155155','41598788785','Ana Lopes','Rua Octa',4500,14),(17,7,'251514','551117897','Maria Lua','Rua Host',3500,NULL),(18,7,'47654564','45452100','Oliver Zeb','Rua Oliva',1500,17),(19,7,'7455564','41151100','Tiago Varp','Rua Gold',1700,17),(20,7,'342242','23100994','Fabin Xales','Rua Edge',1200,17),(21,6,'21321312','9938232','Juca Ted','Rua Liba',2000,14);
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telefones`
--

DROP TABLE IF EXISTS `telefones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `telefones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numf` int NOT NULL,
  `telefone` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numf` (`numf`,`telefone`),
  CONSTRAINT `telefones_ibfk_1` FOREIGN KEY (`numf`) REFERENCES `funcionarios` (`numf`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telefones`
--

LOCK TABLES `telefones` WRITE;
/*!40000 ALTER TABLE `telefones` DISABLE KEYS */;
INSERT INTO `telefones` VALUES (1,3,'102030'),(2,4,'541505'),(3,5,'306402'),(4,6,'807050'),(5,7,'106064'),(6,8,'151055'),(7,9,'154410'),(8,10,'151097'),(9,11,'154151'),(10,12,'410858'),(11,13,'151451'),(12,14,'564511'),(13,15,'210454'),(14,16,'346087'),(15,17,'465020'),(16,18,'708050'),(17,19,'304090'),(18,20,'208070'),(19,21,'906040');
/*!40000 ALTER TABLE `telefones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-09 11:02:23
