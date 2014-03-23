$('.ui.checkbox').checkbox();
$('.ui.dropdown').dropdown();

var amountSteps =  256;
var animationDuration = 15;
var animationSpeed = (amountSteps / animationDuration);
var currentStep = 0;

var DEFAULT_CARTOCSS = [
'#layer {',
" marker-width: 5; ",
' marker-fill: ; #B10026;',
' [value > 10] { marker-fill: #E31A1C; }',
' [value > 50] { marker-fill: #FC4E2A; }',
' [value > 100] { marker-fill: #FD8D3C; }',
' [value > 250] { marker-fill: #FEB24C; }',
' [value > 500] { marker-fill: #FED976; }',
' [value > 1000] { marker-fill: #FFFFB2; }',
' [frame-offset = 1] {  marker-width: 6; marker-fill-opacity: 0.9;}',
' [frame-offset = 2] {  marker-width: 7; marker-fill-opacity: 0.8;}',
' [frame-offset = 3] {  marker-width: 8; marker-fill-opacity: 0.7;}',
' [frame-offset = 4] {  marker-width: 9; marker-fill-opacity: 0.6;}',
' [frame-offset = 5] {  marker-width: 10; marker-fill-opacity: 0.5;}',
' [frame-offset = 6] {  marker-width: 11; marker-fill-opacity: 0.4;}',
' [frame-offset = 7] {  marker-width: 12; marker-fill-opacity: 0.3;}',
' [frame-offset = 8] {  marker-width: 13; marker-fill-opacity: 0.2;}',
'}'
].join('\n');

var map = new google.maps.Map(document.getElementById('map'), {
    center: new google.maps.LatLng(-23.546523, -46.633407),
    zoom: 10,
    mapTypeControl:false,
    minZoom:1,
    scaleControl: false,
    streetViewControl: false,
    overviewMapControl: false,
    styles: [ { "featureType": "landscape", "stylers": [ { "visibility": "off" } ] },{ "stylers": [ { "lightness": -16 }, { "saturation": 1 }, { "gamma": 0.84 } ] } ]
});
var torqueLayer = new torque.GMapsTorqueLayer({
  provider: 'sql_api',
  user : 'ellery',
  table : 'lentidao_sumario_semanal',
  column : 'timestr',
  countby : 'max(extensao)',
  resolution: 1,
  steps: amountSteps,
  blendmode : 'lighter',
  animationDuration: animationDuration,
  sql: "SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '0'",
  cartocss: DEFAULT_CARTOCSS,
  map: map
});
torqueLayer.setMap(map);
torqueLayer.play();

var map2 = new google.maps.Map(document.getElementById('map2'), {
    center: new google.maps.LatLng(-23.546523, -46.633407),
    zoom: 10,
    mapTypeControl:false,
    minZoom:1,
    scaleControl: false,
    streetViewControl: false,
    overviewMapControl: false,
    draggable: false,
    zoomControl: false,
    scrollwheel: false,
    panControl: false,
    disableDoubleClickZoom: true,
    styles: [ { "featureType": "landscape", "stylers": [ { "visibility": "off" } ] },{ "stylers": [ { "lightness": -16 }, { "saturation": 1 }, { "gamma": 0.84 } ] } ]
});
var torqueLayer2 = new torque.GMapsTorqueLayer({
  provider: 'sql_api',
  user : 'ellery',
  table : 'lentidao_sumario_semanal',
  column : 'timestr',
  countby : 'max(extensao)',
  resolution: 1,
  steps: amountSteps,
  blendmode : 'lighter',
  animationDuration: animationDuration,
  sql: "SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '1'",
  cartocss: DEFAULT_CARTOCSS,
  map: map2
});
torqueLayer2.setMap(map2);
torqueLayer2.play();

var syncMap = function() {
  map2.fitBounds(map.getBounds());
  map2.setZoom(map.getZoom());
}

google.maps.event.addListener(map, 'center_changed', syncMap);
google.maps.event.addListener(map, 'zoom_changed', syncMap);


// Filtro por dia da semana
$('.map1-weekday').click(function() {
  $('#map1-title').text('Mapa de Lentidão (' + $(this).text() + ')');
  FiltrarMapa[$(this).data('week')](torqueLayer);
});

$('.map2-weekday').click(function() {
  $('#map2-title').text('Mapa de Lentidão (' + $(this).text() + ')');
  FiltrarMapa[$(this).data('week')](torqueLayer2);
});


var FiltrarMapa = {
  dom: function(layer) {
    layer.setSQL("SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '0'");
    return true;
  },
  seg: function(layer) {
    layer.setSQL("SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '1'");
    return true;
  },
  ter: function(layer) {
    layer.setSQL("SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '2'");
    return true;
  },
  qua: function(layer) {
    layer.setSQL("SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '3'");
    return true;
  },
  qui: function(layer) {
    layer.setSQL("SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '4'");
    return true;
  },
  sex: function(layer) {
    layer.setSQL("SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '5'");
    return true;
  },
  sab: function(layer) {
    layer.setSQL("SELECT * FROM lentidao_sumario_semanal WHERE semana LIKE '6'");
    return true;
  }
}


torqueLayer.on('change:time', function(changes) {
  currentStep = changes.step;
  if (changes.time.getHours) {
    $('#map-time').text((changes.time.getHours() + 2) % 24 + ':' + changes.time.getMinutes());
  }
  torqueLayer2.setStep(currentStep);
});

var timeoutFlowButton;

$('#map-backward').mousedown(function(){
    timeoutFlowButton = setInterval(function(){
        torqueLayer.pause();
        torqueLayer2.pause();
        torqueLayer.setStep(currentStep - animationSpeed);
        torqueLayer2.setStep(currentStep - animationSpeed);
    }, 100);

    return false;
});

$('#map-forward').mousedown(function(){
    timeoutFlowButton = setInterval(function(){
        torqueLayer.pause();
        torqueLayer2.pause();
        torqueLayer.setStep(currentStep + animationSpeed);
        torqueLayer2.setStep(currentStep + animationSpeed);
    }, 100);

    return false;
});

$(document).mouseup(function(){
    if (timeoutFlowButton) {
      if (! $('#map-stop').hasClass('active')) {
        torqueLayer.play();
        torqueLayer2.play();
      }
    }
    clearInterval(timeoutFlowButton);
    timeoutFlowButton = false;
    return false;
});

$('.maps-control').click(function() {
  if (! $(this).hasClass('active')) {
    torqueLayer.toggle();
    torqueLayer2.toggle();
    $('.maps-control').toggleClass('active');
  }
});


