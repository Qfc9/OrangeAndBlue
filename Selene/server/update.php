<?php
header("Content-Type: application/json; charset=UTF-8");
header('Access-Control-Allow-Origin: *'); 

$myObj->version = "0.1.0";
$myObj->link = "https://eos.secretservice.app/update.zip";
$myObj->restart = true;

$myJSON = json_encode($myObj);

echo $myJSON;
?>