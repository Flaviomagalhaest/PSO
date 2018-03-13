//DESENHA O MAPA USANDO WEBSERVICE DO GOOGLE MAPS PARA MAPAS ESTÁTICOS
function codificaPath(pathPHP, locais) {
    var pathJS = Array();
    pathPHP.forEach(function(path) {
        var a = new google.maps.LatLng(path.lat, path.lng);
        pathJS.push(a);
    }, this);
    var pathEncode = google.maps.geometry.encoding.encodePath(pathJS);
    var origem = '|'+pathJS[0].lat().toString()+','+pathJS[0].lng().toString();
    var destino = '|'+pathJS[pathJS.length - 1].lat().toString()+','+pathJS[pathJS.length - 1].lng().toString();
    var url = 'https://maps.googleapis.com/maps/api/staticmap?size=512x512&path=weight:3|color:red|enc:'+pathEncode+'&maptype=roadmap\&markers=size:mid|color:red'+locais+'&key=AIzaSyC5wyAhlPFnEheBiT8i-XjpAajZ7i93eVQ';
    var mapa = document.getElementById('mapa');
    mapa.src=url; mapa.style.display = '';
}

var coord = Array();

function mostraGrafico() {
    var myLatlng = new google.maps.LatLng(-23.973705011113726,-46.31132125854492);
    var myOptions = { zoom: 13, center: myLatlng}
    var map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
    google.maps.event.addListener(map, 'click', function(event) { 
        placeMarker(event.latLng, map);
        coord.push(event.latLng.toJSON());
    });
}

//ADICIONA MARCADORES AO MAPA
function placeMarker(location, map) {
    var marker = new google.maps.Marker({
        position: location, 
        map: map
    });
}


//ENVIA CORDENADAS E RECEBE DE VOLA OS RESULTADOS DA ROTA
function envioCoord() {
    $.post("gmaps.php", {
        coord: JSON.stringify(coord),
        RETORNO: true
    }, function(response) {
        console.log(response);
        var k = response.split(';');
        var pathPHP = JSON.parse(k[0]);
        var locais = JSON.parse(k[1]);
        codificaPath(pathPHP, locais);
    });

}
