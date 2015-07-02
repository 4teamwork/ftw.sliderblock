$(document).on('onBeforeClose', '.overlay', function(){
  ftwSliderInit();
});

$(document).on('sortstop', '.sl-column', function(){
  ftwSliderInit();
});
