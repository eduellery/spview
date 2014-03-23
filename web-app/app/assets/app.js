$('#camadas-menu').sidebar();
$('.ui.checkbox').checkbox();
$('.ui.dropdown').dropdown();

$('#camadas-button').click(function() {
  $('#camadas-menu').sidebar('toggle');
});

var map = new google.maps.Map(document.getElementById('map'), {
    center: new google.maps.LatLng(-23.546523, -46.633407),
    zoom: 10,
    mapTypeControl:false,
    minZoom:1,
    scaleControl: false,
    streetViewControl: false,
    overviewMapControl: false,
});

var map_style = {};
map_style.google_maps_customization_style = [ { "featureType": "landscape", "stylers": [ { "visibility": "off" } ] },{ "stylers": [ { "lightness": -16 }, { "saturation": 1 }, { "gamma": 0.84 } ] } ];
map.setOptions({styles:map_style.google_maps_customization_style});

var torqueLayer = new torque.GMapsTorqueLayer({
  provider: 'sql_api',
  user : 'ellery',
  table : 'lentidao_sumario_semanal6',
  column : 'timestr',
  countby : 'max(extensao)',
  resolution: 1,
  steps: 1024,
  blendmode : 'lighter',
  animationDuration: 60,
  map: map
});

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

torqueLayer.setCartoCSS(DEFAULT_CARTOCSS);
torqueLayer.setMap(map);
torqueLayer.play()