<?php
	if(isset($_POST['start'])) {
		shell_exec('sudo /etc/init.d/tempLogger start');
	}
	if(isset($_POST['stop'])) {
		shell_exec('sudo /etc/init.d/tempLogger stop');
	}
?>

<html>
<head>
<script type="text/javascript"
	src="dygraph-combined.js"></script>
</head>
<body>
	<div id="graphdiv" style="width:500px; height:300px;"></div>
	<script type="text/javascript">
	  var g2 = new Dygraph(document.getElementById("graphdiv"), "tempData.csv", {});
	</script>

	<?php
		$str = shell_exec('ps aux | grep lcd');
		if (strpos($str, 'lcd start') !== false) echo 'running';
		else echo 'not running';
	?>

	<form action="<?=$_SERVER['PHP_SELF'];?>" method="post">
		<input type="submit" name="start" value="start">
	</form>

	<form action="<?=$_SERVER['PHP_SELF'];?>" method="post">
		<input type="submit" name="stop" value="stop">
	</form>

	<a href="tempData.csv">Data</a>

</body>
</html>
