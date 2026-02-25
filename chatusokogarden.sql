-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 25, 2026 at 06:15 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatusokogarden`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` text DEFAULT NULL,
  `product_cost` int(11) DEFAULT NULL,
  `product_photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'Delamere yoghurt', 'strawberry flavour', 150, '<FileStorage: \'cairo.webp\' (\'image/webp\')>'),
(2, 'Delamere yoghurt', 'strawberry flavour', 150, 'cairo.jpeg'),
(3, 'Classic soap', 'Washing powder', 100, 'furniture1.jpeg'),
(4, 'Electric cooker', 'Cheap and affordable', 10000, 'dar.jpeg'),
(5, 'Curtains', 'Home decor', 850, 'decor1.jpg'),
(6, 'Bed', 'White German', 2000, 'bed8.jpg'),
(7, 'Phone', 'Samsung', 15000, 'phone5.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `phone`) VALUES
(1, 'Joy Nyakio', '223344', 'joynyakio789@gmail.com', '+254 711223344'),
(2, 'Meshack Kinywa', '009988', 'meshackkinywa234@gmail.com', '+254 744556677'),
(3, 'Justus Mutie', '778899', 'justusmutie456@gmail.com', '+254 788776655'),
(4, 'John Mburu', '667788', 'johnmburu386@gmail.com', '+254 700998877'),
(5, 'Mary', '1234', 'mary@gmail.com', '0711442235'),
(6, 'Vincent', '2356', 'vincent@gmail.com', '0722553033'),
(7, 'Hellen', '2380', 'hellen@gmail.com', '0711223344'),
(8, 'Maxwell', '9493', 'maxwell@gmail.com', '0715586121'),
(9, 'Yvonne', '9363', 'yvonne@gmail.com', '0720344556'),
(10, 'viane', '9541', 'viane@gmail.com', '0719202345'),
(11, 'Susan', '9488', 'susan@gmail.com', '0716567829'),
(12, 'Getrude', '9388', 'getrude@gmail.com', '0788996056'),
(13, 'Vanessa', '6789', 'vanessa@gmail.com', '0720252030'),
(14, 'Lexsil', '6289', 'lexsil@gmail.com', '0740507896'),
(15, 'Justin', '9056', 'justin@gmail.com', '0704169813'),
(16, 'Sabina', '5608', 'sabina@gmail.com', '0757529542'),
(17, 'Edna', '9389', 'edna@gmail.com', '0723456543'),
(18, 'Patrick', '5070', 'patrick@gmail.com', '0791967830'),
(19, 'Charles', '2010', 'charles@gmail.com', '0712345678'),
(20, 'Antony', '3040', 'antony@gmail.com', '0740438379'),
(21, 'Amos', '7890', 'amos@gmail.com', '0728141420'),
(22, 'Agnes', '9578', 'agnes@gmail.com', '0711400530'),
(23, 'James', '9133', 'james@gmail.com', '0790562010'),
(24, 'Mercy', '9453', 'mercy@gmail.com', '0717219499'),
(25, 'Achieng', '3456', 'achieng@gmail.com', '0710293847'),
(26, 'Pascalia', '2230', 'pascalia@gmail.com', '0722334455'),
(27, 'Celina', '1434', 'celina@gmail.com', '0710203040');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
