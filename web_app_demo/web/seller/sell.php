<?php
    session_start();   
    $con = mysqli_connect('localhost','root','');
    mysqli_select_db($con, 'virttour');

    if(!$con)
    {
        die("Connection failed: " . mysqli_connect_error());
    }

    if(!isset($_SESSION['email']))
    {
        header('location:/virtualTourWebsite/login.php');
    } 
    if($_SESSION['email']=='guest'){
      header('location:/virtualTourWebsite/login.php');
    }
?>

<!DOCTYPE html>
<html lang="en"  >
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" rel="stylesheet" media="all">
  </head>
<body style="background-color: #7f9497!important;" class="container-fluid text-dark">
    <!-- navbar -->
  <nav class="navbar pt-3 navbar-expand-lg navbar-light ">
    <div class="container-fluid">
    <a href="http://localhost/virtualTourWebsite/listings.php"><img class="mx-3" srcset="http://localhost/virtualTourWebsite/logo.png 3x" alt=""></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse justify-content-center navbar-collapse" id="navbarTogglerDemo02">
        <ul class="navbar-nav  mb-2 justify-content-center mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="http://localhost/recommendalgo/web_app_demo/web/index/listings.php">Buy</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Sell</a>
          </li>
          <li class="nav-item">
            <a class="nav-link "  href="http://localhost/recommendalgo/web_app_demo/web/metaVerse/metaverse.php"  >METAverse</a>
          </li>
          <li>
            <a class="nav-link" id="logout" href="http://localhost/recommendalgo/web_app_demo/validations/logout.php">Logout</a>
          </li>
        </ul>      
      </div>
    </div>
  </nav>

    <main>
    <form  action="upload.php" method="POST" enctype="multipart/form-data">

    <div class="container py-4 mt-5 px-4" style="background-color: #ffffff57!important;">
        <div class=" rounded my-3 row align-self-center">    
          <div class="card col bg-transparent border-0">
           <div>
             <img srcset="https://cdn.pixabay.com/photo/2018/11/13/21/43/instagram-3814049_960_720.png 5x"  alt="user">
           </div> 
            <!-- pic from https://pixabay.com/vectors/instagram-insta-user-instagram-icon-3814049/ -->
            <div class="card-body">
                <h5 class="card-title" id="user_id" >Hi <?php echo $_SESSION['email'];?>!</h5>
            </div>
            <div class="card-body">
                <p class="card-title" id="user_id" >Use this page to upload a listing you plan to sell. You can also use the estimate button to see what the prices are like based on the details you provide.</p>
            </div>
          </div>
          
          <div class="col">
              <div class="input-group mb-3">
                <input type="text" class="form-control house_details" name="living_space" placeholder="acres of living space" required>
              </div>
              <div class="input-group mb-3">
                <input type="text" class="form-control house_details" name="bathrooms" placeholder="no. of bathrooms"required>
              </div>
              <div class="input-group mb-3">
                <input type="text" class="form-control house_details" name="bedrooms" placeholder="no. of bedrooms"required>
              </div>
              <div class="input-group mb-3">
                <select class="form-select" name="building_class" aria-label="Default select example" required>
                  <option selected>Building class</option>
                  <option value="1">board house flat</option>
                  <option value="3">concrete flat</option>
                  <option value="5">concrete complex (multi-story)</option>
                  <option value="7">villa-type</option>
                  <option value="9">mansion</option>
                </select>  
              </div>

              <div class="input-group mb-3">
                <input type="text" class="form-control house_details" name="land" placeholder="acres of land"required>
              </div>
              <div class="input-group mb-3">
                <input type="text" class="form-control house_details" name="age" placeholder="age in years"required>
              </div>
              <ul class="list-group list-group-horizontal">
                <a class="btn border bg-transparent submit">Estimate</a>
                <input type="text"  id="the_estimate" disabled placeholder="">
              </ul>
            </div>

            <div class="col">
            <div class="input-group mb-3">
                <input type="text" class="form-control house_details" name="description" placeholder="Extra deatil/ Description">
              </div>
              <div class="input-group mb-3">
                <input type="text" class="form-control house_details" name="price" placeholder="Asking price"required>
              </div>
              <div class="input-group mb-3">
                <input type="text" class="form-control house_details" name="house_location" placeholder="location"required>
              </div>
              <div class="input-group pt-3 mb-2">
                 <label >Upload pictute of the listing</label>
              </div>
              <div class="input-group mb-3">
                <input type="file" class="form-control house_details" name="image" required>
              </div>
              <button type="submit" class="btn border bg-transparent submit" name="upload">Upload</button>
            </div>
          </div>
        </div>
      </form>
  </main>

<!-- chatbot -->
  <div class="px-4 my-3" style="position: fixed; right: 0; bottom: 0; z-index: 1030; ">
    <div class="rounded " style="background-color:#ffffffd0">
      <div class="rounded py-3" id="response_area" style="background-color:#ffffffd0">
        <p class="px-2 text-start"  style="background-color:#ffffffd0" >Hi! <?php echo $_SESSION['email'];?></p>
      </div>
        <div class="" id="chat_controls">
        <ul class="list-group list-group-horizontal">  
        <input id="user_chat" type="text" name="chat" class="form-control border-0 bg-light" placeholder="Enter message">
          <button class="send  btn-primary">Send</button>
          </ul>
        </div>
    </div>
    <img id="chat_trigger" class="float-end" srcset="http://localhost/recommendalgo/web_app_demo/web/images/chatbot.png 9x" style="cursor: pointer;" alt="">
  </div>
    
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script  type = "text/javascript" src="sell.js"></script>
  <script src="http://localhost/recommendalgo/web_app_demo/chatbot_module/chatbot.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"crossorigin="anonymous"></script>

</body>
</html>

