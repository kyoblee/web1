
<?php
// 다음 들을 것 - 23 https://www.youtube.com/watch?v=ExLCGW51mk0&list=PLuHgQVnccGMAMMNByX8Bf1BkVrShBhj1I&index=35

  function print_title(){
      if (isset($_GET['id'])) {
          echo $_GET['id'];
      } else {
          echo "Welcome from print_title()";
      }
  }

  function print_list(){
      $list = scandir('./data');
      $i = 0;
      while ($i<count($list)) {
        if (($list[$i] != '.') && ($list[$i] != '..')) {
         echo "<li><a href=\"index.php?id=$list[$i]\">$list[$i]</a></li>\n";
        }
        $i = $i + 1;
      }
  }

  function print_description(){
      if (isset($_GET['id'])) {
          echo file_get_contents("data/".$_GET['id']);
      } else {
          echo "Hello, PHP from print_description";
      }
  }
?>

<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>
      <?php
        print_title();
      ?>
    </title>
  </head>
  <body>
    <h1><a href="index.php">WEB</a></h1>
    <ol>
      <?php
        print_list();
      ?>
    </ol>
    <h2>
      <?php
        print_title();
      ?>
    </h2>
    <?php
        print_description();
    ?>
  </body>
</html>