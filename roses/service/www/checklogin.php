<?php

$md5='51acad5071aab26de09e45c6c5516c58';

$password=$_POST['password']; 

if($password == $md5) {
	$url = 'flaggy.php';
} else {
	$url = '404.html';
}

header("Location: $url");
exit();
?>