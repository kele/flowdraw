$(document).ready(function(){
  var canvas = document.getElementById("bgCanvas");
  var ctx = canvas.getContext("2d");
  ctx.fillStyle = "red";
  ctx.fillRect(0, 0, 2, 1);
  var data = canvas.toDataURL();
  
  $('.message').css('background-image', 'url(' + data + ')');
  $(".message").css('background-repeat', 'repeat-y');
});