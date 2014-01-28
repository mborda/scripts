<?php

include("wsLeere.class.php");
$ws = new wsLeere();
$s = $ws->login($argv[1]);
echo $s;

?>
