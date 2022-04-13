<?php
session_start();

//to destroy guest session
session_destroy();

session_start();
$con = mysqli_connect('localhost','root','');
mysqli_select_db($con, 'virttour');

$email = $_POST['email'];
$pass = $_POST['password'];

$check = "select * from users where email= '$email' && password='$pass'";

$result = mysqli_query($con, $check);

$num = mysqli_num_rows($result);

if($num==1){
    $_SESSION['email']=$email;
    header('location:/virtualTourWebsite/listings.php');
}
else{
    header('location:/virtualTourWebsite/login.php');
}

?>
