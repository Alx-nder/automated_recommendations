<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <link rel="stylesheet" href="style.css">
    <title>Virtual tour</title>
  </head>
  <body class="video-container" >

  <video  autoplay muted loop poster="https://images.pexels.com/photos/1115804/pexels-photo-1115804.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940">
    <source type="video/mp4" src="https://assets.mixkit.co/videos/preview/mixkit-minimalist-room-with-gray-sofa-3110-large.mp4">
    <!-- pic credit https://images.pexels.com/photos/1115804/pexels-photo-1115804.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940 -->
    <!-- vid credit https://assets.mixkit.co/videos/preview/mixkit-minimalist-room-with-gray-sofa-3110-large.mp4 -->
    </video>


        <form action="validation.php" class="text-center rounded login_tag" method="post">
          <div class="mb-3 border-bottom">
            <input type="email" name="email" class="form-control border-0 bg-transparent" placeholder="Email" id="exampleInputEmail1" aria-describedby="emailHelp" required>
          </div>
          <div class="mb-3 border-bottom">
            <input type="password" name="password" class="form-control border-0 bg-transparent" placeholder="Password" id="exampleInputPassword1" required>
          </div>
          <button type="submit" class="btn border bg-transparent">Log In</button>
        </form>   
      
  <?php 
  echo "";
  ?>

    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

  </body>
</html>