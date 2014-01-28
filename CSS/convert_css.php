<?php
/*
 * Conversor de unidades CSS
 */


function pt2em ($basesize=12){
    return function ($el) use($basesize){
        $medida = (float) $el[1];
        $resultado = $medida / $basesize;
        $texto = ":$resultado" . "em";
        return $texto;
    };
}

function cm2em ($el){
    $medida = (float) $el[1];
    $resultado = $medida * 2;
    $texto = ":$resultado" . "em";
    return $texto;
}

if (count($argv)<4){
    echo "\n\nModo de uso:\n     php convert_css.php css_entrada css_salida tamaño_base_fuente\n\n\n";
    die();
}

$filename = $argv[1];
$filename_out = $argv[2];
$basesize = $argv[3];

$texto = file_get_contents($filename);
$res1 = preg_replace_callback("/:(\d+)pt/", pt2em($basesize), $texto);
$res2 = preg_replace_callback("/:(\d+\.?\d*)cm/", 'cm2em', $res1);
file_put_contents($filename_out, $res2);


?>
