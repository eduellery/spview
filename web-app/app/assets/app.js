$('#camadas-menu').sidebar();
$('.ui.checkbox').checkbox();

$('#camadas-button').click(function() {
  $('#camadas-menu').sidebar('toggle');
});

var mapOptions = {
  zoom: 10,
  center: new google.maps.LatLng(-23.546523, -46.633407)
};

var map = new google.maps.Map(document.getElementById('map'), mapOptions);

var sublayers = [];

cartodb.createLayer(map, 'http://oesgalha.cartodb.com/api/v2/viz/4a933b04-b1bf-11e3-8f25-0e230854a1cb/viz.json')
.addTo(map)
.on('done', function(layer) {
  // change the query for the first layer
  var subLayerOptions = {
    sql: "SELECT * FROM table_2013_acidentes_1o_semestre WHERE vit_morta = 0",
    cartocss: "#table_2013_acidentes_1o_semestre{marker-opacity: 0.9;marker-line-color: #FFF;marker-line-width: 1.5;marker-line-opacity: 1;marker-placement: point;marker-multi-policy: largest;marker-type: ellipse;marker-fill: #FF5C00;marker-allow-overlap: true;marker-clip: false;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 23] {marker-width: 25.0;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 11] {marker-width: 23.3;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 9] {marker-width: 21.7;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 8] {marker-width: 20.0;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 7] {marker-width: 18.3;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 6] {marker-width: 16.7;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 4] {marker-width: 15.0;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 3] {marker-width: 13.3;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 2] {marker-width: 11.7;}#table_2013_acidentes_1o_semestre [ vit_ferida <= 1] {marker-width: 10.0;}"
  }

  var sublayer = layer.getSubLayer(0);

  sublayer.set(subLayerOptions);

  sublayers.push(sublayer);

 subLayerOptions = {
    sql: "SELECT * FROM table_2013_acidentes_1o_semestre WHERE vit_morta >= 1",
    cartocss: "#table_2013_acidentes_1o_semestre{marker-opacity: 0.9;marker-line-color: #FFF;marker-line-width: 1.5;marker-line-opacity: 1;marker-placement: point;marker-multi-policy: largest;marker-type: ellipse;marker-fill: #B40903;marker-allow-overlap: true;marker-clip: false;}#table_2013_acidentes_1o_semestre [ vit_morta <= 3] {marker-width: 25.0;}#table_2013_acidentes_1o_semestre [ vit_morta <= 3] {marker-width: 23.3;}#table_2013_acidentes_1o_semestre [ vit_morta <= 2] {marker-width: 21.7;}#table_2013_acidentes_1o_semestre [ vit_morta <= 2] {marker-width: 20.0;}#table_2013_acidentes_1o_semestre [ vit_morta <= 2] {marker-width: 18.3;}#table_2013_acidentes_1o_semestre [ vit_morta <= 2] {marker-width: 16.7;}#table_2013_acidentes_1o_semestre [ vit_morta <= 1] {marker-width: 15.0;}#table_2013_acidentes_1o_semestre [ vit_morta <= 1] {marker-width: 13.3;}#table_2013_acidentes_1o_semestre [ vit_morta <= 1] {marker-width: 11.7;}#table_2013_acidentes_1o_semestre [ vit_morta <= 0] {marker-width: 10.0;}"
  }

  sublayer = layer.getSubLayer(1);

  sublayer.set(subLayerOptions);

  sublayers.push(sublayer);

}).on('error', function() {
  //log the error
});

$('.camadas-control').change(function() {
  if ($(this).is(':checked')) {
    LayersShowAction[$(this).attr('name')]();
  } else {
    LayersHideAction[$(this).attr('name')]();
  }
});

var LayersShowAction = {
  acidentes: function(){
    sublayers[0].show();
    return true;
  },
  acidentes_letais: function(){
    sublayers[1].show();
    return true;
  }
}

var LayersHideAction = {
  acidentes: function(){
    sublayers[0].hide();
    return true;
  },
  acidentes_letais: function(){
    sublayers[1].hide();
    return true;
  }
}