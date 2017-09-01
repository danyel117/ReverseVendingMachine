
<html>
<body>

Welcome <?php echo $_GET["name"]; ?><br>
Your email address is: <?php echo $_GET["email"]; ?>

<?php
	
																   
	$myfile = fopen("comunicacion.txt", "w") or die("Unable to open file!");
	if ($_GET["name"]=="d"){
		$txt = "Daniel\n";
		fwrite($myfile, $txt);
	}
	
	if ($_GET["name"]=="a"){
		$txt = "Alejandro\n";
		fwrite($myfile, $txt);
	}

	fclose($myfile);
	$url = 'http://localhost/RVM/GUI/GUI.html'; // this can be set based on whatever
	header( "Location: $url" );

?> 

</body>
</html>
