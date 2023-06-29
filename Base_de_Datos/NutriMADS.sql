CREATE TABLE `ALIMENTO`  (
  `ID` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(25) NOT NULL,
  `Grupo_alimenticio` enum('Frutas','Verduras','Cereales','Leguminosas','Origen animal') NOT NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `COMPONENTE`  (
  `ID` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Cantidad` float(15) NOT NULL,
  `Unidad_medida` enum('g', 'µg', 'mg', 'UI', 'cal', 'kcal', 'ml') NOT NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `CRITERIO`  (
  `ID` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `Estatus` enum('Saludable', 'No saludable') NOT NULL,
  `Calificacion` float(10) NULL,
  `Unidad_medida` int NULL,
  `Comentario` varchar(300) NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `FACTOR`  (
  `ID` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Estatus` enum('Temprano', 'Estable', 'Grave') NOT NULL,
  PRIMARY KEY (`ID`)
);

ALTER TABLE `COMPONENTE` ADD CONSTRAINT `fk_Componente_Alimento` FOREIGN KEY (`ID`) REFERENCES `ALIMENTO` (`ID`);

