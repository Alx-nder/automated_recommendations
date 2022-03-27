-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 27, 2022 at 03:10 PM
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
-- Table structure for table `listings`
--

CREATE TABLE `listings` (
  `id` int(11) NOT NULL,
  `location` varchar(100) NOT NULL,
  `posted` varchar(11) NOT NULL,
  `description` text NOT NULL,
  `price` double NOT NULL,
  `image_src` varchar(255) NOT NULL,
  `tour_link` varchar(255) NOT NULL,
  `living_space` double NOT NULL,
  `bathrooms` double NOT NULL,
  `bedrooms` int(100) NOT NULL,
  `building_class` int(100) NOT NULL,
  `age` double NOT NULL,
  `land` double NOT NULL,
  `posted_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `listings`
--

INSERT INTO `listings` (`id`, `location`, `posted`, `description`, `price`, `image_src`, `tour_link`, `living_space`, `bathrooms`, `bedrooms`, `building_class`, `age`, `land`, `posted_by`) VALUES
(1, 'grange hill', 'January 14 ', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet fugiat rerum consequatur. Eaque delectus voluptates aliquid temporibus quibusdam magni quidem, nesciunt hic atque laborum consequatur fugiat aut sunt dolores quam?', 3125476, 'https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940', 'https://everpano.s3.eu-central-1.amazonaws.com/3d/loft/index.html', 0.5, 2.5, 3, 3, 2, 2.3, 't@y.com'),
(2, 'Mandeville', 'February 19', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae amet obcaecati facere nam ducimus excepturi eum atque neque perspiciatis, delectus reiciendis tempora voluptas laboriosam consequuntur exercitationem quibusdam, in facilis temporibus.', 2140234, 'https://images.pexels.com/photos/280222/pexels-photo-280222.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500', 'https://everpano.s3.eu-central-1.amazonaws.com/3d/riereta/index.html', 0.6, 3, 4, 3, 10, 0.5, 't@y.com'),
(3, 'Kingston', 'January 12', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet labore hic fugiat vitae id illum numquam quo voluptate, culpa voluptas nulla ipsa impedit expedita laborum ea corporis repellat? Placeat, illum?', 1052442, 'https://images.pexels.com/photos/1974596/pexels-photo-1974596.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940', 'http://localhost/vtour/tour.html', 0.25, 1, 2, 1, 6, 1.3, 't@y.com'),
(4, 'Lucea', 'December 30', 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex, quidem eaque? Laudantium cupiditate quibusdam molestias nulla, possimus quae nihil exercitationem temporibus ad atque quasi, error harum eos fuga consequuntur pariatur!', 3524432, 'https://images.pexels.com/photos/206768/pexels-photo-206768.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940', 'http://localhost/krpano_three_js_example/index.html', 0.5, 3.5, 4, 4, 5, 2, 'hello@hi.hey'),
(75, 'Manchester', 'February 12', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptatibus expedita laboriosam molestiae, nam laudantium minus doloremque, nihil voluptatum aliquam dolor voluptas animi distinctio iure consequuntur ab odit necessitatibus, corrupti quod.', 900000, 'https://cdn.jhmrad.com/wp-content/uploads/properties-sale-egypt-primelocation_25987.jpg', 'https://everpano.s3.eu-central-1.amazonaws.com/3d/iencuentro/index.html', 0.2, 2, 3, 1, 4, 0.25, 'hello@hi.hey');

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
(2, 'hello@hi.hey', '123456');

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
  `grange hill` int(11) NOT NULL,
  `mandeville` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_pref`
--

INSERT INTO `user_pref` (`username`, `price_0`, `price_1`, `price_2`, `lucea`, `manchester`, `kingston`, `grange hill`, `mandeville`) VALUES
('guest', 0, 0, 0, 0, 0, 0, 0, 0),
('hello@hi.hey', 2, 6, 7, 2, 6, 1, 5, 0),
('t@y.com', 2, 4, 1, 2, 4, 3, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `building_class`
--
ALTER TABLE `building_class`
  ADD UNIQUE KEY `no` (`no`);

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
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
