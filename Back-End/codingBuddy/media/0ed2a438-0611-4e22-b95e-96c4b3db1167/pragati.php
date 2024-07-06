<form action="" method="POST">
Enter enrollment:
<input type="text" name="enrollment"/><br/>
Enter sub1:
<input type="text" name="Sub1"/><br>
Enter sub2:
<input type="text" name="Sub2"/><br/>
Enter sub3:
<input type="text" name="Sub3"/><br/>
Enter sub4:
<input type="text" name="Sub4"/><br/>
Enter sub5:
<input type="text" name="Sub5"/><br/>
</form>
<?php
$enrollment=$_POST['Enrollment_NO.'];
$sub1=$_POST['Sub1'];
$sub2=$_POST['Sub2'];
$sub3=$_POST['Sub3'];
$sub4=$_POST['Sub4'];
$sub5=$_POST['Sub5'];

$servername="localhost";
$username="username";
$password="password";
$conn=new mysqli($servername,$username,$password);
if($conn->connect_error){
    die("Connection failed: ")
}
$sql="insert into student values('$enrollment','$sub1','$sub2','$sub3','$sub4','$sub5')";

$data=$conn->query($sql);
if($data)
{
    echo "New record inserted sucfessfully";
}
else
{
    echo "error";
}
$conn->close();
?>