$(document).ready(function () {
  var messages = document.getElementsByClassName("message");
  
  for (var i = 0; i < messages.length; i++)
  {
      messages[i].style.color = "green";
      console.log(messages[i].offsetHeight);
      console.log(messages[i].offsetWidth);
      
      var canvasElement = document.createElement("canvas");
      var width = canvasElement.width = messages[i].clientWidth;
      var height = canvasElement.height = 5;
      
      var br = document.createElement("br");
      messages[i].insertBefore(br, messages[i].firstChild);
      messages[i].insertBefore(canvasElement, messages[i].firstChild);
      console.log(canvasElement);
      canvasElement.primary_width = width;
      
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
  
var redraw = function (messageTd)
{
  console.log(messageTd);
  var canvas = messageTd.getElementsByTagName("canvas")[0];
  console.log(canvas);
  
  var height = 5;
  var width = canvas.width = messageTd.clientWidth;
  
  
  var ctx = canvas.getContext("2d");
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
      $("#really_hidden").toggle("slow", function() { redraw(event.currentTarget); });
      
    }
    else if (messageId == 4)
    {
      $("#really_hidden2").toggle("slow", function() { redraw(event.currentTarget); });
    }
  });
  

});