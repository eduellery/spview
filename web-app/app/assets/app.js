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

cartodb.createLayer(map, 'http://oesgalha.cartodb.com/api/v2/viz/4a933b04-b1bf-11e3-8f25-0e230854a1cb/viz.json')
.addTo(map)
.on('done', function(layer) {
  var sublayer = layer.getSubLayer(0);
  sublayer.on('featureOver', function(e, pos, latlng, data) {
    cartodb.log.log(e, pos, latlng, data);
  });

  sublayer.on('error', function(err) {
    cartodb.log.log('error: ' + err);
  });

})
.on('error', function() {
  cartodb.log.log("some error occurred");
});