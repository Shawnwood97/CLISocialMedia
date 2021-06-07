-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: 34.134.120.57    Database: cli_social_media
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.18-MariaDB-1:10.4.18+maria~stretch

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exploits`
--

DROP TABLE IF EXISTS `exploits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exploits` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `hacker_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exploits_FK` (`hacker_id`),
  CONSTRAINT `exploits_FK` FOREIGN KEY (`hacker_id`) REFERENCES `hackers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exploits`
--

LOCK TABLES `exploits` WRITE;
/*!40000 ALTER TABLE `exploits` DISABLE KEYS */;
INSERT INTO `exploits` VALUES (1,'My dad once told me, laugh and the world laughs with you, Cry, and I\'ll give you something to cry about you little bastard! I was part of something special. God creates dinosaurs. God destroys dinosaurs. God creates Man. Man destroys God. Man creates Dinosaurs.',2),(2,'This thing comes fully loaded. AM/FM radio, reclining bucket seats, and... power windows. Remind me to thank John for a lovely weekend. Checkmate... Do you have any idea how long it takes those cups to decompose. Hey, take a look at the earthlings. Goodbye!',3),(3,'So you two dig up, dig up dinosaurs? You really think you can fly that thing? Remind me to thank John for a lovely weekend. You know what? It is beets. I\'ve crashed into a beet truck. I gave it a cold? I gave it a virus. A computer virus. Life finds a way.',4),(4,'God creates dinosaurs. God destroys dinosaurs. God creates Man. Man destroys God. Man creates Dinosaurs. Must go faster... go, go, go, go, go! Hey, take a look at the earthlings. Goodbye! Remind me to thank John for a lovely weekend. Remind me to thank John for a lovely weekend.',1),(5,'Eventually, you do plan to have dinosaurs on your dinosaur tour, right? Checkmate... We gotta burn the rain forest, dump toxic waste, pollute the air, and rip up the OZONE! \'Cause maybe if we screw up this planet enough, they won\'t want it anymore! Is this my espresso machine? Wh-what is-h-how did you get my espresso machine?',5),(6,'Checkmate... I gave it a cold? I gave it a virus. A computer virus. Is this my espresso machine? Wh-what is-h-how did you get my espresso machine? Hey, you know how I\'m, like, always trying to save the planet? Here\'s my chance. What do they got in there? King Kong?',4),(7,'So you two dig up, dig up dinosaurs? You\'re a very talented young man, with your own clever thoughts and ideas. Do you need a manager? Did he just throw my cat out of the window? So you two dig up, dig up dinosaurs? Hey, take a look at the earthlings. Goodbye!',5),(8,'I was part of something special. Yeah, but your scientists were so preoccupied with whether or not they could, they didn\'t stop to think if they should. Yeah, but John, if The Pirates of the Caribbean breaks down, the pirates don’t eat the tourists. My dad once told me, laugh and the world laughs with you, Cry, and I\'ll give you something to cry about you little bastard!',6),(9,'Forget the fat lady! You\'re obsessed with the fat lady! Drive us out of here! Do you have any idea how long it takes those cups to decompose. Checkmate... Remind me to thank John for a lovely weekend. Hey, take a look at the earthlings. Goodbye! Life finds a way.',5),(10,'Hey, take a look at the earthlings. Goodbye! Hey, take a look at the earthlings. Goodbye! Do you have any idea how long it takes those cups to decompose. Life finds a way. Do you have any idea how long it takes those cups to decompose. Yeah, but your scientists were so preoccupied with whether or not they could, they didn\'t stop to think if they should.',2),(11,'I gave it a cold? I gave it a virus. A computer virus. Life finds a way. You know what? It is beets. I\'ve crashed into a beet truck. You really think you can fly that thing? They\'re using our own satellites against us. And the clock is ticking. God help us, we\'re in the hands of engineers.',4),(12,'Checkmate... Life finds a way. Yes, Yes, without the oops! Do you have any idea how long it takes those cups to decompose. Yeah, but your scientists were so preoccupied with whether or not they could, they didn\'t stop to think if they should. Just my luck, no ice.',1),(13,'Did he just throw my cat out of the window? Yeah, but John, if The Pirates of the Caribbean breaks down, the pirates don’t eat the tourists. Is this my espresso machine? Wh-what is-h-how did you get my espresso machine? Just my luck, no ice. I gave it a cold? I gave it a virus. A computer virus.',2),(14,'Hey, take a look at the earthlings. Goodbye! I gave it a cold? I gave it a virus. A computer virus. Yes, Yes, without the oops! Eventually, you do plan to have dinosaurs on your dinosaur tour, right? Must go faster... go, go, go, go, go! You really think you can fly that thing?',1),(15,'I gave it a cold? I gave it a virus. A computer virus. God creates dinosaurs. God destroys dinosaurs. God creates Man. Man destroys God. Man creates Dinosaurs. Must go faster... go, go, go, go, go! Hey, you know how I\'m, like, always trying to save the planet? Here\'s my chance.',4),(16,'God help us, we\'re in the hands of engineers. You\'re a very talented young man, with your own clever thoughts and ideas. Do you need a manager? Checkmate... Yeah, but your scientists were so preoccupied with whether or not they could, they didn\'t stop to think if they should.',3),(17,'You know what? It is beets. I\'ve crashed into a beet truck. Do you have any idea how long it takes those cups to decompose. God help us, we\'re in the hands of engineers. Hey, you know how I\'m, like, always trying to save the planet? Here\'s my chance.',3),(18,'Remind me to thank John for a lovely weekend. Remind me to thank John for a lovely weekend. Jaguar shark! So tell me - does it really exist? Did he just throw my cat out of the window? Life finds a way. You really think you can fly that thing? We gotta burn the rain forest, dump toxic waste, pollute the air, and rip up the OZONE! \'Cause maybe if we screw up this planet enough, they won\'t want it anymore!',4),(19,'Is this my espresso machine? Wh-what is-h-how did you get my espresso machine? Hey, you know how I\'m, like, always trying to save the planet? Here\'s my chance. I gave it a cold? I gave it a virus. A computer virus. My dad once told me, laugh and the world laughs with you, Cry, and I\'ll give you something to cry about you little bastard!',5),(20,'You know what? It is beets. I\'ve crashed into a beet truck. They\'re using our own satellites against us. And the clock is ticking. You know what? It is beets. I\'ve crashed into a beet truck. Must go faster... go, go, go, go, go! What do they got in there? King Kong?',2),(21,'Hey this is a post',2),(24,'This is an exploit!',1),(25,'This is another exploit!',1);
/*!40000 ALTER TABLE `exploits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hackers`
--

DROP TABLE IF EXISTS `hackers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hackers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `alias` varchar(35) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hackers_UN` (`alias`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackers`
--

LOCK TABLES `hackers` WRITE;
/*!40000 ALTER TABLE `hackers` DISABLE KEYS */;
INSERT INTO `hackers` VALUES (1,'Fury','password1'),(2,'Beta','password2'),(3,'Omega','password3'),(4,'Prankster','password4'),(5,'Boggle','password5'),(6,'Chief','password6');
/*!40000 ALTER TABLE `hackers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'cli_social_media'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-07 12:05:50
