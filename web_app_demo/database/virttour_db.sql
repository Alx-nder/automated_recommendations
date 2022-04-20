-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 20, 2022 at 06:07 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `virttour`
--

-- --------------------------------------------------------

--
-- Table structure for table `building_class`
--

CREATE TABLE `building_class` (
  `no` int(100) NOT NULL,
  `description` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `building_class`
--

INSERT INTO `building_class` (`no`, `description`) VALUES
(1, 'board house flat'),
(3, 'concrete flat'),
(5, 'concrete complex (multi-story)'),
(7, 'villa-type'),
(9, 'mansion');

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `id` int(11) NOT NULL,
  `img_name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`id`, `img_name`, `created_at`) VALUES
(1, 'IMG-6244c30b885ca3.68384862.png', '2022-03-30 15:52:27');

-- --------------------------------------------------------

--
-- Table structure for table `listings`
--

CREATE TABLE `listings` (
  `id` int(11) NOT NULL,
  `house_location` varchar(100) NOT NULL,
  `posted` varchar(11) NOT NULL,
  `house_description` text NOT NULL,
  `price` double NOT NULL,
  `image_src` varchar(255) NOT NULL,
  `tour_link` varchar(255) NOT NULL,
  `living_space` double NOT NULL,
  `bathrooms` double NOT NULL,
  `bedrooms` int(100) NOT NULL,
  `building_class` int(100) NOT NULL,
  `age` double NOT NULL,
  `land` double NOT NULL,
  `posted_by` varchar(255) NOT NULL,
  `listings_interaction` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `listings`
--

INSERT INTO `listings` (`id`, `house_location`, `posted`, `house_description`, `price`, `image_src`, `tour_link`, `living_space`, `bathrooms`, `bedrooms`, `building_class`, `age`, `land`, `posted_by`, `listings_interaction`) VALUES
(1, 'grange', 'January 14 ', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet fugiat rerum consequatur. Eaque delectus voluptates aliquid temporibus quibusdam magni quidem, nesciunt hic atque laborum consequatur fugiat aut sunt dolores quam?', 3125476, 'https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940', 'https://everpano.s3.eu-central-1.amazonaws.com/3d/loft/index.html', 0.5, 2.5, 3, 3, 2, 2.3, 't@y.com', 0),
(2, 'mandeville', 'February 19', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae amet obcaecati facere nam ducimus excepturi eum atque neque perspiciatis, delectus reiciendis tempora voluptas laboriosam consequuntur exercitationem quibusdam, in facilis temporibus.', 2140234, 'https://images.pexels.com/photos/280222/pexels-photo-280222.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500', 'https://everpano.s3.eu-central-1.amazonaws.com/3d/riereta/index.html', 0.6, 3, 4, 3, 10, 0.5, 't@y.com', 0),
(3, 'kingston', 'January 12', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet labore hic fugiat vitae id illum numquam quo voluptate, culpa voluptas nulla ipsa impedit expedita laborum ea corporis repellat? Placeat, illum?', 1052442, 'https://images.unsplash.com/photo-1430285561322-7808604715df?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', 'http://localhost/vtour/tour.html', 0.25, 1, 2, 1, 6, 1.3, 't@y.com', 0),
(4, 'lucea', 'December 30', 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex, quidem eaque? Laudantium cupiditate quibusdam molestias nulla, possimus quae nihil exercitationem temporibus ad atque quasi, error harum eos fuga consequuntur pariatur!', 3524432, 'https://images.pexels.com/photos/206768/pexels-photo-206768.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940', 'http://localhost/krpano_three_js_example/index.html', 0.5, 3.5, 4, 4, 5, 2, 'hello@hi.hey', 0),
(5, 'manchester', 'February 12', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptatibus expedita laboriosam molestiae, nam laudantium minus doloremque, nihil voluptatum aliquam dolor voluptas animi distinctio iure consequuntur ab odit necessitatibus, corrupti quod.', 900000, 'https://cdn.jhmrad.com/wp-content/uploads/properties-sale-egypt-primelocation_25987.jpg', 'https://everpano.s3.eu-central-1.amazonaws.com/3d/iencuentro/index.html', 0.2, 2, 3, 1, 4, 0.25, 'hello@hi.hey', 0),
(6, 'kingston', 'awdawd', 'rhdrggdrggrgdgd', 2500000, 'https://images.unsplash.com/photo-1583608205776-bfd35f0d9f83?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', 'http://localhost/krpano-1.20.11/viewer/krpano.html?xml=examples/hotspot-extract/pool.xml', 1, 2, 2, 2, 2, 2, 't@y.com', 0),
(7, 'grange', '', '', 3741205, 'https://images.unsplash.com/photo-1598228723793-52759bba239c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80', 'https://images.unsplash.com/photo-1598228723793-52759bba239c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80', 0.5, 3, 4, 5, 2, 3, 'info.virttour@gmail.com', 0),
(8, 'lucea', '', '', 997000, 'https://images.unsplash.com/photo-1599427303058-f04cbcf4756f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80', 'http://localhost/krpano-1.20.11/viewer/krpano.html?xml=examples/interactive-area/interactive-area.xml', 0.5, 1.5, 2, 2, 8, 0.7, 'info.virttour@gmail.com', 0),
(9, 'kingston', '', '', 2017504, 'https://images.unsplash.com/photo-1602075432748-82d264e2b463?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', 'https://images.unsplash.com/photo-1602075432748-82d264e2b463?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', 0.6, 3, 2, 8, 4, 1.9, 'info.virttour@gmail.com', 0),
(10, 'mandeville', '', '', 3000000, 'https://images.unsplash.com/photo-1605146768851-eda79da39897?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', 'https://images.unsplash.com/photo-1605146768851-eda79da39897?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', 0.8, 3.5, 4, 5, 2, 1.8, 'info.virttour@gmail.com', 0),
(11, 'kingston', '', '', 3258716, 'https://images.unsplash.com/photo-1623298317883-6b70254edf31?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', 'http://localhost/krpano-1.20.11/viewer/krpano.html?xml=examples/demotour-apartment/tour.xml', 0.8, 3, 4, 5, 5, 2, 'info.virttour@gmail.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `parishes`
--

CREATE TABLE `parishes` (
  `parish_no` int(11) NOT NULL,
  `parish_name` varchar(110) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `parishes`
--

INSERT INTO `parishes` (`parish_no`, `parish_name`) VALUES
(1, 'westmoreland'),
(2, 'hanover'),
(3, 'St James'),
(4, 'St Elizabeth'),
(5, 'Manchester'),
(6, 'Trelawny'),
(7, 'St Ann'),
(8, 'clarendon'),
(9, 'St catherine'),
(10, 'St mary'),
(11, 'portland'),
(12, 'st thomas'),
(13, 'kingston'),
(14, 'st andrew');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(10) NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `email`, `password`) VALUES
(1, 't@y.com', '123'),
(2, 'hello@hi.hey', '123456'),
(3, 'guest', '');

-- --------------------------------------------------------

--
-- Table structure for table `user_pref`
--

CREATE TABLE `user_pref` (
  `username` varchar(110) NOT NULL,
  `price_0` int(11) NOT NULL,
  `price_1` int(11) NOT NULL,
  `price_2` int(11) NOT NULL,
  `lucea` int(11) NOT NULL,
  `manchester` int(11) NOT NULL,
  `kingston` int(11) NOT NULL,
  `grange` int(11) NOT NULL,
  `mandeville` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_pref`
--

INSERT INTO `user_pref` (`username`, `price_0`, `price_1`, `price_2`, `lucea`, `manchester`, `kingston`, `grange`, `mandeville`) VALUES
('guest', 3, 6, 4, 11, 3, 2, 4, 4),
('hello@hi.hey', 7, 6, 7, 2, 11, 10, 5, 0),
('t@y.com', 2, 5, 3, 2, 5, 4, 4, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `building_class`
--
ALTER TABLE `building_class`
  ADD UNIQUE KEY `no` (`no`);

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `listings`
--
ALTER TABLE `listings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `parishes`
--
ALTER TABLE `parishes`
  ADD PRIMARY KEY (`parish_no`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `user_pref`
--
ALTER TABLE `user_pref`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `images`
--
ALTER TABLE `images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `listings`
--
ALTER TABLE `listings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
