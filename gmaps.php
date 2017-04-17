<?php
$key = 'AIzaSyC5wyAhlPFnEheBiT8i-XjpAajZ7i93eVQ';
//CARREGANDO BIBLIOTECA SCRIPT DO GOOGLE
echo '<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key='.$key.'&libraries=geometry"></script>';
echo '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>';
echo '<script type="text/javascript" src="js/gmapsController.js"></script>';

// $pyscript = "C:\\Users\\Flaviomt\\Dropbox\\MACHINE_LEARNING\\PSO-GoogleMaps\\main.py";
// $python = "C:\\Users\\Flaviomt\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe";
if (isset($_POST['RETORNO'])) {
    $pyscript = "py\\main.py";
    $python = "C:\\Users\\FCAMARA884\\Anaconda3\\python.exe";
    $coord = $_POST['coord'];
    $cmd = "$python $pyscript ".$coord;

    //EXECUTA LEITURA DO SCRIPT EM PYTHON
    exec("$cmd", $result);    
    #$result = Array();
    #array_push($result, '{"pontos": {"0": {"lat": -23.9680457, "lng": -46.3442721}, "1": {"lat": -23.9637878, "lng": -46.3323495}, "2": {"lat": -23.9710268, "lng": -46.3227091}, "3": {"lat": -23.9723503, "lng": -46.3208786}, "4": {"lat": -23.9699659, "lng": -46.3108729}, "5": {"lat": -23.9897934, "lng": -46.299768}}, "gbest": {"distTotal": 15307, "caminho": [4, 5, 0, 1, 2, 3, 4]}}');
    $path = array(); $locais = '';
    //DECODIFICANDO JSON RESULTANTE DO SCRIPT
    $json = json_decode($result['0']);

    for ($i = 0; $i < count($json->gbest->caminho) - 1; $i++) {
        $ini = $json->gbest->caminho[$i];
        $fim = $json->gbest->caminho[$i+1];        

        //ACHANDO OS PATHS DE LIGAÇÃO PARA CADA PONTO
        $origem = (string)$json->pontos->{$ini}->lat.', '.(string)$json->pontos->{$ini}->lng;
        $destino = (string)$json->pontos->{$fim}->lat.', '.(string)$json->pontos->{$fim}->lng;    
        $url = 'https://maps.googleapis.com/maps/api/directions/json?origin='.urlencode($origem).'&destination='.urlencode($destino).'&key='.urlencode($key).'';    
        $json_path = file_get_contents($url);   //OBJETO EM JSON PEGO DA URL
        $obj = json_decode($json_path); //JSON DECODIFICADO
        $nr_steps = count($obj->routes[0]->legs[0]->steps); //NÚMERO DE STEPS USADOS PARA O PATH
        
        //MONTANDO ARRAY DE LOCAIS
        $locais .= '|'.$origem;
        //FOREACH PARA CADA LIGAÇÃO DE PONTOS GERANDO UM PATH ÚNICO
        $flg = false;    //IDENTIFICANDO PRIMEIRO ITEM DO PATH
        foreach($obj->routes[0]->legs[0]->steps as $item) {
            if ($flg == false) { array_push($path, $item->start_location); $flg = true; }
            array_push($path, $item->end_location);    
        }    
    }
    echo '<script> var pathPHP = '.json_encode($path).'; var locais = '.json_encode($locais).' </script>';
    echo '<script>codificaPath();</script>';

} else {
    ?>
    <html>
    <body>
        <div id="map-canvas" style="height: 30%; width: 30%;"></div>
        <input type="submit" class="button" id="calc_rota" onClick="envioCoord()" value="Calcular rota">
        <div>
            <img id="mapa" src="#"></img>
        </div>
    </body>
    </html>


    <?php
    //ENVIANDO ARRAY RESULTANTE PARA O SCRIPT
    
    echo '<script>mostraGrafico();</script>';        
    
}
?>





