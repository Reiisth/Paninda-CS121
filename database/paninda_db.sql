-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2024 at 09:47 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `paninda_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `classifications`
--

CREATE TABLE `classifications` (
  `ClassID` varchar(3) NOT NULL,
  `ClassName` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `classifications`
--

INSERT INTO `classifications` (`ClassID`, `ClassName`) VALUES
('BEV', 'Beverages'),
('CAN', 'Canned Goods'),
('CBS', 'Cookies/Biscuits'),
('CKG', 'Cooking Ingredients'),
('CLN', 'Cleaning/Laundry Supplies'),
('CND', 'Candies/Sweets'),
('FRO', 'Frozen Goods'),
('HGN', 'Hygiene Products'),
('NDL', 'Instant Noodles'),
('SCH', 'School Supplies'),
('SNK', 'Snacks'),
('UNC', 'Unclassified');

-- --------------------------------------------------------

--
-- Stand-in structure for view `expired_stock`
-- (See below for the actual view)
--
CREATE TABLE `expired_stock` (
`ProductID` int(11)
,`ProductName` varchar(50)
,`ExpDate` date
,`Quantity` int(11)
,`UserID` int(5)
);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `ProductID` int(11) NOT NULL,
  `ProductName` varchar(50) NOT NULL,
  `ClassID` varchar(3) NOT NULL,
  `SupplierID` int(5) NOT NULL,
  `UserID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`ProductID`, `ProductName`, `ClassID`, `SupplierID`, `UserID`) VALUES
(1, 'Coke Mismo', 'BEV', 1, 1),
(2, 'Hansel Crackers', 'CBS', 6, 1),
(3, 'Argentina Corned Beef 450g', 'CAN', 6, 1),
(4, 'Star Margarine 500g', 'CKG', 4, 1),
(5, 'Jessa\'s Peanut Butter', 'CKG', 6, 1),
(6, 'Chuckie 250mL', 'BEV', 1, 1),
(7, 'LuckyMe! Pancit Canton Sweet & Spicy', 'NDL', 7, 1),
(10, 'Modess Regular Non-wing', 'HGN', 4, 1),
(11, 'Sprite Mismo', 'BEV', 1, 1),
(12, 'Tender Juicy Hotdog Classic', 'FRO', 4, 1),
(13, 'Mongol No.2 Pencils', 'SCH', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `ProductID` int(11) NOT NULL,
  `ExpDate` date NOT NULL,
  `Quantity` int(11) NOT NULL,
  `UserID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`ProductID`, `ExpDate`, `Quantity`, `UserID`) VALUES
(1, '2025-07-09', 15, 1),
(2, '2024-12-07', 24, 1),
(2, '2025-08-09', 24, 1),
(2, '2025-09-12', 36, 1),
(3, '2026-08-28', 4, 1),
(5, '2024-05-04', 5, 1),
(6, '2024-06-01', 8, 1),
(10, '2026-07-19', 12, 1),
(11, '2024-08-01', 12, 1),
(13, '2028-08-28', 100, 1);

-- --------------------------------------------------------

--
-- Stand-in structure for view `stock_with_names`
-- (See below for the actual view)
--
CREATE TABLE `stock_with_names` (
`ProductID` int(11)
,`ProductName` varchar(50)
,`ExpDate` date
,`Quantity` int(11)
,`UserID` int(5)
);

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `SupplierID` int(11) NOT NULL,
  `SupplierName` varchar(50) NOT NULL,
  `SupplierContact` varchar(50) NOT NULL,
  `SupplierAddress` varchar(50) DEFAULT NULL,
  `UserID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`SupplierID`, `SupplierName`, `SupplierContact`, `SupplierAddress`, `UserID`) VALUES
(1, 'Royal Sales Marketing Corp.', '09633586161', 'Sampaga Centro, 4200 Batangas City, Batangas', 1),
(4, 'Salesforce One Marketing Inc.', '0434621678', 'Sambat, Balayan, Batangas', 1),
(5, 'JT International Inc.', '09171799805', 'Balintawak, Lipa City, Batangas', 1),
(6, 'Alvarez Supermarket', '09578594668', 'Illustre Ave. Lemery, Batangas', 1),
(7, 'JE Distributors Inc.', '09437566380', 'Hi-Wood Ave. Mataas na Kahoy, Batangas', 1),
(8, 'Mealvine Marketing Corp.', '09561562648', 'Poblacion, Calaca City, Batangas', 1),
(9, 'Sunkist Family Mart', '09468597312', 'Dayapan, Lemery, Batangas', 1),
(10, 'Law & Renz School and Office Supplies', '09561638768', 'Tambo, LIpa City, Batangas', 1),
(11, 'Xylo Gemini Distributors Inc.', '0431864987', 'Poblacion, Taal, Batangas', 1),
(12, 'Weiyan Marketing LLC', '0431033112', 'Sta. Rosa Business Park, Sta. Rosa, Laguna', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UserID` int(5) NOT NULL,
  `UserName` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UserID`, `UserName`, `Password`) VALUES
(1, 'admin', 'jasjas');

-- --------------------------------------------------------

--
-- Structure for view `expired_stock`
--
DROP TABLE IF EXISTS `expired_stock`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `expired_stock`  AS SELECT `s`.`ProductID` AS `ProductID`, `p`.`ProductName` AS `ProductName`, `s`.`ExpDate` AS `ExpDate`, `s`.`Quantity` AS `Quantity`, `s`.`UserID` AS `UserID` FROM (`stock` `s` join `products` `p` on(`s`.`ProductID` = `p`.`ProductID`)) WHERE `s`.`ExpDate` < curdate() ;

-- --------------------------------------------------------

--
-- Structure for view `stock_with_names`
--
DROP TABLE IF EXISTS `stock_with_names`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `stock_with_names`  AS SELECT `s`.`ProductID` AS `ProductID`, `p`.`ProductName` AS `ProductName`, `s`.`ExpDate` AS `ExpDate`, `s`.`Quantity` AS `Quantity`, `p`.`UserID` AS `UserID` FROM (`stock` `s` join `products` `p` on(`s`.`ProductID` = `p`.`ProductID`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `classifications`
--
ALTER TABLE `classifications`
  ADD PRIMARY KEY (`ClassID`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`ProductID`,`UserID`),
  ADD KEY `ClassID` (`ClassID`),
  ADD KEY `SupplierID` (`SupplierID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`ProductID`,`ExpDate`,`UserID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`SupplierID`,`UserID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `unique_UserName` (`UserName`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `ProductID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `SupplierID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `UserID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`ClassID`) REFERENCES `classifications` (`ClassID`),
  ADD CONSTRAINT `products_ibfk_2` FOREIGN KEY (`SupplierID`) REFERENCES `suppliers` (`SupplierID`),
  ADD CONSTRAINT `products_ibfk_3` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`);

--
-- Constraints for table `stock`
--
ALTER TABLE `stock`
  ADD CONSTRAINT `stock_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `products` (`ProductID`),
  ADD CONSTRAINT `stock_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`);

--
-- Constraints for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD CONSTRAINT `suppliers_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
