-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2024 at 07:22 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jailmanage`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `email`, `password`) VALUES
('Group 3', 'sameer@gmail.com', '93a5086d4a0f21b634c2518c249523247ebba14f0cabf5ae5bee54bfd5588556');

-- --------------------------------------------------------

-- Table structure for table `needs`
--

CREATE TABLE `needs` (
  `id` int(11) NOT NULL,
  `needs` varchar(500) NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `needs`
--

INSERT INTO `needs` (`id`, `needs`, `status`) VALUES
(1, 'Book', 'accepted'),
(2, 'Chicken Tanduri', 'accepted');

-- --------------------------------------------------------

-- Table structure for table `prisoner`
--

CREATE TABLE `prisoner` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `age` int(11) NOT NULL,
  `birth` date NOT NULL,
  `record` varchar(50) NOT NULL,
  `cell` varchar(50) NOT NULL,
  `year` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- Dumping data for table `prisoner`
--

INSERT INTO `prisoner` (`id`, `name`, `age`, `birth`, `record`, `cell`, `year`) VALUES
(8, 'Kala Manik', 45, '1993-07-12', 'Drug Dealing', '2A', '5 years'),
(12, 'Alison Burger', 45, '1995-07-11', 'Robbery', '1B', '2 years'),
(14, 'Ted Bundy', 40, '1970-07-05', 'Serial Killer', '2B', 'Death Sentence');


--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `email` varchar(200) NOT NULL,
  `shift` varchar(200) NOT NULL,
  `reason` varchar(1000) NOT NULL,
  `role` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- --------------------------------------------------------

--
-- Table structure for table `schedule`
--

CREATE TABLE `schedule` (
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  `shift` varchar(200) NOT NULL,
  `time` varchar(20) NOT NULL,
  `role` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--

-- Dumping data for table `schedule`
--

INSERT INTO `schedule` (`name`, `email`, `type`, `shift`, `time`, `role`) VALUES
('Shariful Alam', 'sam@gmail.com', 'Special', 'Night', '9PM - 12AM', 'Cleaner'),
('Shafin Mufdi', 'shafin@gmail.com', 'Special', 'Day', '8AM - 3PM', 'Police'),
('Shadman Shakib', 'shakib@gmail.com', 'Wash Dish', 'Night', '9PM - 12AM', 'Chef');

-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `role` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `role`, `email`, `password`) VALUES
(32, 'Shariful Alam', 'Cleaner', 'sam@gmail.com', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f'),
(33, 'Shafin Mufdi', 'Police', 'shafin@gmail.com', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f'),
(35, 'Shadman Shakib', 'Chef', 'shakib@gmail.com', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

-- Indexes for table `needs`
--
ALTER TABLE `needs`
  ADD PRIMARY KEY (`id`);

-- Indexes for table `prisoner`
--
ALTER TABLE `prisoner`
  ADD PRIMARY KEY (`id`);
--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `schedule`
--
ALTER TABLE `schedule`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

-- AUTO_INCREMENT for table `needs`
--
ALTER TABLE `needs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

-- AUTO_INCREMENT for table `prisoner`
--
ALTER TABLE `prisoner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
  
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
