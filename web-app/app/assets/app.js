$('#camadas-menu').sidebar();
$('.ui.checkbox').checkbox();

$('#camadas-button').click(function() {
  $('#camadas-menu').sidebar('toggle');
});