<?php

$pyscript = "py\\mainClassica.py";
$python = "C:\\Users\\FCAMARA884\\Anaconda3\\python.exe";
$data = 'XQF131';
$cmd = "$python $pyscript $data";

//EXECUTA LEITURA DO SCRIPT EM PYTHON
exec("$cmd", $result);
var_dump($result);