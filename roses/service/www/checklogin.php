<?php

$md5='12345';

$password=$_POST['password']; 

if($password == $md5) {
	$url = 'flaggy.php';
} else {
	$url = '404.html';
}

header("Location: $url");
exit();
?>