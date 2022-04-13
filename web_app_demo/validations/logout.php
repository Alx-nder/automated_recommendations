<?php
session_start();

session_destroy();

header('location:/recommendAlgo/web_app_demo/web/index/listings.php');

?>