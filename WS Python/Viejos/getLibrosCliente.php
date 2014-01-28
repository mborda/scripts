<?php

include("wsLeere.class.php");
$ws = new wsLeere($argv[1]);
print_R($ws);
$s = $ws->getLibrosCliente();
echo $s;

?>
