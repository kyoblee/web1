<?php
  file_put_contents('data/'.$_POST['title'], $_POST['description']);
  # submit 후 빈화면 방지하기 위해 Redirection
  header('Location: index.php?id='.$_POST['title']);
 ?>
