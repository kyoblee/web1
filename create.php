<?php
  require_once('lib/print.php');
  require_once('view/top.php');
 ?>
    <!-- <a href="create.php">create</a> -->
    <form action="create_process.php" method="post">
      <p>
        <input type="text" name="title" size="30" placeholder="Write Title Here">
      </p>
      <p>
        <textarea name="description" rows="5" cols="70" placeholder="Write Description"></textarea>
      </p>
      <p>
        <input type="submit" value="SUBMIT">
      </p>
    </form>

<?php
  require('view/bottom.php');
 ?>
