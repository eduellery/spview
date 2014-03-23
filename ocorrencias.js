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

cartodb.createLayer(map, 'http://ellery.cartodb.com/api/v2/viz/6044ad10-b24c-11e3-be2e-0e73339ffa50/viz.json')
.addTo(map)
.on('done', function(layer) {
  // change the query for the first layer
  var subLayerOptions0 = {
    sql: "SELECT * FROM ocorrencias_anual WHERE tipo LIKE '%sem%'",
    cartocss: "#ocorrencias_anual{marker-opacity: 0.9;marker-line-color: #FFF;marker-line-width: 1.5;marker-line-opacity: 1;marker-placement: point;marker-type: ellipse;marker-width: 10;marker-fill: #FF6600;marker-allow-overlap: true;}"
  }

  var sublayer = layer.getSubLayer(0);

  sublayer.set(subLayerOptions0);

  sublayers.push(sublayer);

 var subLayerOptions1 = {
    sql: "SELECT * FROM ocorrencias_anual WHERE tipo LIKE '%com%'",
    cartocss: "#ocorrencias_anual{ marker-opacity: 0.9; marker-line-color: #FFF; marker-line-width: 1.5; marker-line-opacity: 1; marker-placement: point; marker-type: ellipse; marker-width: 10; marker-fill: #850200; marker-allow-overlap: true;}"
  }

  sublayer = layer.getSubLayer(1);

  sublayer.set(subLayerOptions1);

  sublayers.push(sublayer);

 var subLayerOptions2 = {
    sql: "SELECT * FROM ocorrencias_anual WHERE tipo LIKE '%caminh%'",
    cartocss: "#ocorrencias_anual{ marker-opacity: 0.9; marker-line-color: #FFF; marker-line-width: 1.5; marker-line-opacity: 1; marker-placement: point; marker-type: ellipse; marker-width: 10; marker-fill: #CCAA00; marker-allow-overlap: true;}"
  }

  sublayer = layer.getSubLayer(2);

  sublayer.set(subLayerOptions2);

  sublayers.push(sublayer);

 var subLayerOptions3 = {
    sql: "SELECT * FROM ocorrencias_anual WHERE tipo LIKE '%moto%'",
    cartocss: "#ocorrencias_anual{ marker-opacity: 0.9; marker-line-color: #FFF; marker-line-width: 1.5; marker-line-opacity: 1; marker-placement: point; marker-type: ellipse; marker-width: 10; marker-fill: #33FF66; marker-allow-overlap: true;}"
  }

  sublayer = layer.getSubLayer(3);

  sublayer.set(subLayerOptions3);

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
  sem: function(){
    sublayers[0].show();
    return true;
  },
  com: function(){
    sublayers[1].show();
    return true;
  },
  caminh: function(){
    sublayers[2].show();
    return true;
  },
  moto: function(){
    sublayers[3].show();
    return true;
  }
}

var LayersHideAction = {
  sem: function(){
    sublayers[0].hide();
    return true;
  },
  com: function(){
    sublayers[1].hide();
    return true;
  },
  caminh: function(){
    sublayers[2].hide();
    return true;
  },
  moto: function(){
    sublayers[3].hide();
    return true;
  }
}