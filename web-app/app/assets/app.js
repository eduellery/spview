$('#camadas-menu').sidebar();
$('.ui.checkbox').checkbox();
$('.ui.dropdown').dropdown();

$('#camadas-button').click(function() {
  $('#camadas-menu').sidebar('toggle');
});

var map = new google.maps.Map(document.getElementById('map'), {
    center: new google.maps.LatLng(-23.546523, -46.633407),
    zoom: 2,
    mapTypeId:google.maps.MapTypeId.SATELLITE,
    mapTypeControl:false,
    minZoom:1,
    scaleControl: false,
    streetViewControl: false,
    overviewMapControl: false,
});

var map_style = {};
map_style.google_maps_customization_style = [
    {
        stylers:[
            { invert_lightness: true },
            { weight: 1 },
            { saturation: -100 },
            { lightness: -40 }
        ]
    },
    {
        elementType:"labels",
        stylers:[
            { visibility:"simplified" }
        ]
    }
];

map.setMapTypeId(google.maps.MapTypeId.ROADMAP);
map.setOptions({styles:map_style.google_maps_customization_style});

var torqueLayer = new torque.GMapsTorqueLayer({
  provider: 'sql_api',
  user : 'ellery',
  table : 'lentidao_sumario_semanal3',
  column : 'cartodb_id',
  countby : 'count(extensao)',
  resolution: 1,
  steps: 1024,
  blendmode : 'lighter',
  animationDuration: 60,
  map: map
});

var DEFAULT_CARTOCSS = [
'#layer {',
" marker-width: 3; ",
' marker-fill: #FEE391; ',
' [value > 2] { marker-fill: #FEC44F; }',
' [value > 3] { marker-fill: #FE9929; }',
' [value > 4] { marker-fill: #EC7014; }',
' [value > 5] { marker-fill: #CC4C02; }',
' [value > 6] { marker-fill: #993404; }',
' [value > 7] { marker-fill: #662506; }',
' [frame-offset = 1] { marker-width: 8;marker-fill-opacity: 0.05;}',
' [frame-offset = 2] { marker-width: 20;marker-fill-opacity: 0.02;}',
//' [frame-offset = 1] { marker-width: 25;marker-fill-opacity: 0.01;}',
'}'
].join('\n');

torqueLayer.setCartoCSS(DEFAULT_CARTOCSS);
torqueLayer.setMap(map);
torqueLayer.play()
