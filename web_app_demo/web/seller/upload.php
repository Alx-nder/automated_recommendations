<?php
session_start();   
$conn = mysqli_connect('localhost','root','');
mysqli_select_db($conn, 'virttour');
$user=$_SESSION['email'];

if (isset($_POST['upload'])){
    ##### house details
    $living_space=$_POST['living_space'];
	$bathrooms=$_POST['bathrooms'];
	$bedrooms=$_POST['bedrooms'];
	$building_class=$_POST['building_class'];
	$land=$_POST['land'];
	$age=$_POST['age'];
	$price=$_POST['price'];
	$house_location=$_POST['house_location'];
	$description=$_POST['description'];
    
	$image = $_FILES['image'];

	# get the image info and store them in var
	$image_name = $_FILES['image']['name'];
	$tmp_name   = $_FILES['image']['tmp_name'];
	$error      = $_FILES['image']['error'];
	$size		= $_FILES['image']['size'];

	$image_extension= explode('.', $image_name);
	$image_extension=strtolower(end($image_extension));

	$allowed_extensions	= array('jpg','jpeg','gif','png');
	
	if(in_array($image_extension,$allowed_extensions)){
		if($error===0){
			// size in kbs
			if($size<100000000){
				$new_img_name= uniqid('',true).'.'.$image_extension;
				$file_destination='uploads/'.$new_img_name;
				move_uploaded_file($tmp_name,$file_destination);
				$file_destination='http://localhost/virtualTourWebsite/seller/uploads/'.$new_img_name;
				$sql="INSERT INTO listings (house_location,posted,house_description,price,image_src,tour_link,living_space,bathrooms,bedrooms,building_class,age,land,posted_by) VALUES ('$house_location','','$description','$price','$file_destination','$file_destination','$living_space','$bathrooms','$bedrooms','$building_class','$age','$land','$user')";
				mysqli_query($conn,$sql);
				header("Location: sell.php?uploaded");
			}else{
				echo "image too large";
			}
		}else{
			echo "Error. Please try again";
		}
	}else{
		echo 'wrong file type';
	}
}
?>