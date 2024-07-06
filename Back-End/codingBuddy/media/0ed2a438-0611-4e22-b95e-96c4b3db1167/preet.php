<?php
$servername="localhost";
$username="username";
$password="password";
$conn=new mysqli($servername,$username,$password);
$sql="select * from users where username={$userid} and password={$pass}";
$result=mysql_query($conn,$sql);
if(mysql_num_rows($result)>0){
    $output="Login Successfull!"
else
    $output="Login Denied! Invalid Credentials"
echo $output;
}?>