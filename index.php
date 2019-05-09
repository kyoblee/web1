<!-- 2019.5 web2 php 완료 -->
<?php
  require_once('lib/print.php');
  require_once('view/top.php');
 ?>

    <a href="create.php">create</a>
    <?php if(isset($_GET['id'])){?>
    <!-- 인자로 들어오는 값이 있는지 확인하는 isset. 아래는 id값이 있어야지 보여짐-->
    <a href="update.php?id=<?=$_GET['id']?>">update</a>
    <!-- 물음표 php echo 부분은 = 로 대체할 수 있음. 뒤에 ;도 없음 -->
    <form action="delete_process.php" method="post">
      <input type="hidden" name="id" value="<?=$_GET['id']?>">
      <input type="submit" value="delete">
    </form>
  <?php } ?>
    <h2>
      <?php
        print_title();
      ?>
    </h2>
    <?php
        print_description();
    ?>
<?php
  require('view/bottom.php');
 ?>
