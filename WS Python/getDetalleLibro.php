<?php

include("wsLeere.class.php");
$ws = new wsLeere();
$s = $ws->getDetalleLibro($argv[1], $argv[2]);
echo $s;

?>
