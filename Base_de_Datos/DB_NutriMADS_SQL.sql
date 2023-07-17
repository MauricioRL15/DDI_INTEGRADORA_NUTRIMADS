CREATE DATABASE  IF NOT EXISTS `bd_nutrimads` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bd_nutrimads`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bd_nutrimads
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `alimento`
--

DROP TABLE IF EXISTS `alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alimento` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(25) NOT NULL,
  `Cantidad` float NOT NULL,
  `Grupo_alimenticio` enum('Fruta','Verdura','Cereal','Leguminosa','Origen_animal') NOT NULL,
  `Estatus` bit(1) NOT NULL DEFAULT b'1',
  `Fecha_Registro` datetime NOT NULL,
  `Fecha_Actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alimento`
--

LOCK TABLES `alimento` WRITE;
/*!40000 ALTER TABLE `alimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alimento_has_criterio`
--

DROP TABLE IF EXISTS `alimento_has_criterio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alimento_has_criterio` (
  `alimento_ID` int unsigned NOT NULL,
  `criterio_ID` int unsigned NOT NULL,
  `Fecha_Inicio` datetime NOT NULL,
  `Fecha_Fin` datetime NOT NULL,
  PRIMARY KEY (`alimento_ID`,`criterio_ID`),
  KEY `fk_alimento_has_criterio_criterio1_idx` (`criterio_ID`),
  KEY `fk_alimento_has_criterio_alimento_idx` (`alimento_ID`),
  CONSTRAINT `fk_alimento_has_criterio_alimento` FOREIGN KEY (`alimento_ID`) REFERENCES `alimento` (`ID`),
  CONSTRAINT `fk_alimento_has_criterio_criterio1` FOREIGN KEY (`criterio_ID`) REFERENCES `criterio` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alimento_has_criterio`
--

LOCK TABLES `alimento_has_criterio` WRITE;
/*!40000 ALTER TABLE `alimento_has_criterio` DISABLE KEYS */;
/*!40000 ALTER TABLE `alimento_has_criterio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `componente`
--

DROP TABLE IF EXISTS `componente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `componente` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Componente_Pradre` int DEFAULT NULL,
  `Unidad_medida` enum('g','µg','mg','UI','cal','kcal','ml') NOT NULL,
  `Estatus` bit(1) NOT NULL DEFAULT b'1',
  `Fecha_Registro` datetime NOT NULL,
  `Fecha_Actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `fk_ComponenteAlimento` FOREIGN KEY (`ID`) REFERENCES `alimento` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `componente`
--

LOCK TABLES `componente` WRITE;
/*!40000 ALTER TABLE `componente` DISABLE KEYS */;
/*!40000 ALTER TABLE `componente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `componente_has_alimento`
--

DROP TABLE IF EXISTS `componente_has_alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `componente_has_alimento` (
  `componente_ID` int unsigned NOT NULL,
  `alimento_ID` int unsigned NOT NULL,
  `Fecha_Inicio` datetime NOT NULL,
  `Fecha_Fin` datetime NOT NULL,
  PRIMARY KEY (`componente_ID`,`alimento_ID`),
  KEY `fk_componente_has_alimento_alimento1_idx` (`alimento_ID`),
  KEY `fk_componente_has_alimento_componente1_idx` (`componente_ID`),
  CONSTRAINT `fk_componente_has_alimento_alimento1` FOREIGN KEY (`alimento_ID`) REFERENCES `alimento` (`ID`),
  CONSTRAINT `fk_componente_has_alimento_componente1` FOREIGN KEY (`componente_ID`) REFERENCES `componente` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `componente_has_alimento`
--

LOCK TABLES `componente_has_alimento` WRITE;
/*!40000 ALTER TABLE `componente_has_alimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `componente_has_alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consumo`
--

DROP TABLE IF EXISTS `consumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumo` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Cantidad` float NOT NULL,
  `Tipo` enum('Consumo_realizado','Consumo_Sugerido') NOT NULL,
  `Estatus` bit(1) NOT NULL DEFAULT b'1',
  `Fecha_Registro` datetime NOT NULL,
  `Fecha_Actualizacion` datetime DEFAULT NULL,
  `Usuario_ID` int unsigned NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_consumo_usuario` (`Usuario_ID`),
  CONSTRAINT `FK_consumo_usuario` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuario` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumo`
--

LOCK TABLES `consumo` WRITE;
/*!40000 ALTER TABLE `consumo` DISABLE KEYS */;
/*!40000 ALTER TABLE `consumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consumo_has_alimento`
--

DROP TABLE IF EXISTS `consumo_has_alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumo_has_alimento` (
  `Consumo_ID` int unsigned NOT NULL,
  `Alimento_ID` int unsigned NOT NULL,
  `Fecha_Inicio` datetime NOT NULL,
  `Fecha_Fin` datetime NOT NULL,
  PRIMARY KEY (`Consumo_ID`,`Alimento_ID`),
  KEY `Alimento_ID` (`Alimento_ID`),
  CONSTRAINT `consumo_has_alimento_ibfk_1` FOREIGN KEY (`Consumo_ID`) REFERENCES `consumo` (`ID`),
  CONSTRAINT `consumo_has_alimento_ibfk_2` FOREIGN KEY (`Alimento_ID`) REFERENCES `alimento` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumo_has_alimento`
--

LOCK TABLES `consumo_has_alimento` WRITE;
/*!40000 ALTER TABLE `consumo_has_alimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `consumo_has_alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `criterio`
--

DROP TABLE IF EXISTS `criterio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `criterio` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(65) NOT NULL,
  `Descripcion` varchar(200) NOT NULL,
  `Valor_Maximo` float NOT NULL,
  `Valor_Minimo` float NOT NULL,
  `Estatus` enum('Saludable','No_saludable') NOT NULL DEFAULT 'Saludable',
  `Fecha_Registro` datetime NOT NULL,
  `Fecha_Actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `criterio`
--

LOCK TABLES `criterio` WRITE;
/*!40000 ALTER TABLE `criterio` DISABLE KEYS */;
/*!40000 ALTER TABLE `criterio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `criterio_has_usuario`
--

DROP TABLE IF EXISTS `criterio_has_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `criterio_has_usuario` (
  `criterio_ID` int unsigned NOT NULL,
  `usuario_ID` int unsigned NOT NULL,
  `Fecha_Inicio` datetime NOT NULL,
  `Fecha_Fin` datetime NOT NULL,
  PRIMARY KEY (`criterio_ID`,`usuario_ID`),
  KEY `fk_criterio_has_usuario_usuario1_idx` (`usuario_ID`),
  KEY `fk_criterio_has_usuario_criterio1_idx` (`criterio_ID`),
  CONSTRAINT `fk_criterio_has_usuario_criterio1` FOREIGN KEY (`criterio_ID`) REFERENCES `criterio` (`ID`),
  CONSTRAINT `fk_criterio_has_usuario_usuario1` FOREIGN KEY (`usuario_ID`) REFERENCES `usuario` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `criterio_has_usuario`
--

LOCK TABLES `criterio_has_usuario` WRITE;
/*!40000 ALTER TABLE `criterio_has_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `criterio_has_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factor`
--

DROP TABLE IF EXISTS `factor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factor` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Estatus` enum('Temprano','Estable','Grave') NOT NULL DEFAULT 'Temprano',
  `Fecha_Registro` datetime NOT NULL,
  `Fecha_Actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factor`
--

LOCK TABLES `factor` WRITE;
/*!40000 ALTER TABLE `factor` DISABLE KEYS */;
/*!40000 ALTER TABLE `factor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factor_has_componente`
--

DROP TABLE IF EXISTS `factor_has_componente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factor_has_componente` (
  `factor_ID` int unsigned NOT NULL,
  `componente_ID` int unsigned NOT NULL,
  `Fecha_Inicio` datetime NOT NULL,
  `Fecha_Fin` datetime NOT NULL,
  PRIMARY KEY (`factor_ID`,`componente_ID`),
  KEY `fk_factor_has_componente_componente1_idx` (`componente_ID`),
  KEY `fk_factor_has_componente_factor1_idx` (`factor_ID`),
  CONSTRAINT `fk_factor_has_componente_componente1` FOREIGN KEY (`componente_ID`) REFERENCES `componente` (`ID`),
  CONSTRAINT `fk_factor_has_componente_factor1` FOREIGN KEY (`factor_ID`) REFERENCES `factor` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factor_has_componente`
--

LOCK TABLES `factor_has_componente` WRITE;
/*!40000 ALTER TABLE `factor_has_componente` DISABLE KEYS */;
/*!40000 ALTER TABLE `factor_has_componente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factor_has_usuario`
--

DROP TABLE IF EXISTS `factor_has_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factor_has_usuario` (
  `factor_ID` int unsigned NOT NULL,
  `usuario_ID` int unsigned NOT NULL,
  `Fecha_Inicio` datetime NOT NULL,
  `Fecha_Fin` datetime NOT NULL,
  PRIMARY KEY (`factor_ID`,`usuario_ID`),
  KEY `fk_factor_has_usuario_usuario1_idx` (`usuario_ID`),
  KEY `fk_factor_has_usuario_factor1_idx` (`factor_ID`),
  CONSTRAINT `fk_factor_has_usuario_factor1` FOREIGN KEY (`factor_ID`) REFERENCES `factor` (`ID`),
  CONSTRAINT `fk_factor_has_usuario_usuario1` FOREIGN KEY (`usuario_ID`) REFERENCES `usuario` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factor_has_usuario`
--

LOCK TABLES `factor_has_usuario` WRITE;
/*!40000 ALTER TABLE `factor_has_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `factor_has_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Descripcion` varchar(150) NOT NULL,
  `Estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `Fecha_Registro` datetime NOT NULL,
  `Fecha_Actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Genero` enum('Femenino','Masculino','No_Binario') NOT NULL,
  `Peso` float NOT NULL,
  `Talla` float NOT NULL,
  `Fecha_Nacimiento` date NOT NULL,
  `Estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `Fecha_Registro` datetime NOT NULL,
  `Fecha_Actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_has_rol`
--

DROP TABLE IF EXISTS `usuario_has_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_has_rol` (
  `usuario_ID` int unsigned NOT NULL,
  `rol_ID` int unsigned NOT NULL,
  `Fecha_Inicio` datetime NOT NULL,
  `Fecha_Fin` datetime NOT NULL,
  PRIMARY KEY (`usuario_ID`,`rol_ID`),
  KEY `fk_usuario_has_rol_rol1_idx` (`rol_ID`),
  KEY `fk_usuario_has_rol_usuario1_idx` (`usuario_ID`),
  CONSTRAINT `fk_usuario_has_rol_rol1` FOREIGN KEY (`rol_ID`) REFERENCES `rol` (`ID`),
  CONSTRAINT `fk_usuario_has_rol_usuario1` FOREIGN KEY (`usuario_ID`) REFERENCES `usuario` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_has_rol`
--

LOCK TABLES `usuario_has_rol` WRITE;
/*!40000 ALTER TABLE `usuario_has_rol` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_has_rol` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-14 19:31:55
