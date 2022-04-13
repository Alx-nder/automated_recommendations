<?php
session_start();

session_destroy();

header('location:/virtualTourWebsite/listings.php');

?>