
var redraw = function (canvas)
{ 
  var height = canvas.clientHeight;
  var width = canvas.clientWidth;
  
  //console.log(height + " " + width);
  
  var ctx = canvas.getContext("2d");
  ctx.beginPath();
  ctx.clearRect(0, 0, width, height);
  ctx.moveTo(0, 2);
  ctx.lineTo(width - 1, 2);
  ctx.moveTo(width - 1, 2);
  ctx.lineTo(width - 7, 0);
  ctx.moveTo(width - 1, 2);
  ctx.lineTo(width - 7, 4);
  ctx.strokeStyle = "red 2px";
  ctx.stroke();
}
  
var redrawAll = function()
{
  var canvases = document.getElementsByTagName("canvas");
  console.log(canvases);
  for (var i = 0; i < canvases.length; i++)
    redraw(canvases[i]);
}

$(document).ready(function () {
  var messages = document.getElementsByClassName("message");
  
  for (var i = 0; i < messages.length; i++)
  {
      var canvasElement = document.createElement("canvas");
      canvasElement.style.width = "100%";
      canvasElement.style.maxHeight = "5px";
      canvasElement.height = 5;
      var height = canvasElement.height = 5;
      var width = canvasElement.width;
      
      var br = document.createElement("br");
      messages[i].insertBefore(br, messages[i].firstChild);
      messages[i].insertBefore(canvasElement, messages[i].firstChild);
      
      var ctx = canvasElement.getContext("2d");
      ctx.beginPath();
      ctx.moveTo(0, 2);
      ctx.lineTo(width - 1, 2);
      ctx.moveTo(width - 1, 2);
      ctx.lineTo(width - 5, 0);
      ctx.moveTo(width - 1, 2);
      ctx.lineTo(width - 5, 4);
      ctx.stroke();
  }
  
    
  $(".message").click(function (event) {
    var messageId = event.currentTarget.id;
    if (messageId == 1)
    {
      $("#really_hidden").toggle("slow");
    }
    else if (messageId == 4)
    {
      $("#really_hidden2").toggle("slow");
    }
  });
});



