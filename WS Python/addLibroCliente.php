<?php

include("wsLeere.class.php");
$ws = new wsLeere($argv[1]);
$s = $ws->addLibroCliente($argv[2],$argv[3],$argv[4]);
echo $s;

?>
