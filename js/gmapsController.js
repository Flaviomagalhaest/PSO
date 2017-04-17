function codificaPath() {
    var pathJS = Array();
    pathPHP.forEach(function(path) {
        var a = new google.maps.LatLng(path.lat, path.lng);
        pathJS.push(a);
    }, this);
    var pathEncode = google.maps.geometry.encoding.encodePath(pathJS);
    var origem = '|'+pathJS[0].lat().toString()+','+pathJS[0].lng().toString();
    var destino = '|'+pathJS[pathJS.length - 1].lat().toString()+','+pathJS[pathJS.length - 1].lng().toString();
    var url = 'https://maps.googleapis.com/maps/api/staticmap?size=512x512&path=weight:3|color:red|enc:'+pathEncode+'&maptype=roadmap\&markers=size:mid|color:red'+locais+'&key=AIzaSyC5wyAhlPFnEheBiT8i-XjpAajZ7i93eVQ';
    document.getElementById('mapa').src=url;
    console.log(pathJS);
}

var coord = Array();

function mostraGrafico() {
    var myLatlng = new google.maps.LatLng(-23.973705011113726,-46.31132125854492);
    var myOptions = { zoom: 13, center: myLatlng}
    var map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
    google.maps.event.addListener(map, 'click', function(event) { coord.push(event.latLng.toJSON()); console.log(coord); });
}



function envioCoord() {
    $.post("gmaps.php", {
        coord: JSON.stringify(coord),
        RETORNO: true
    }, function(response) {
        console.log(JSON.stringify(coord));
    });

}
