function main()
{
    var diagram = Diagram.parse(document.getElementById('raw_diagram').innerText);
    diagram.drawSVG("diagram", {theme: 'simple'});

    $("tspan").click(function(event) {
        var messageText = this.firstChild.data;
        var msgId = parseInt(messageText);
        if (isNaN(msgId))
        {
            return;
        }

        var x = event.pageX;
        var y = event.pageY;

        console.log(event);
        $("div#msg_" + msgId)
            .toggle()
            .css("position", "absolute")
            .css("top", y + "px")
            .css("left", x + "px");
    });

    $("text").each(function() {
        this.style.fontSize = "9pt";
    });

    $("div.popup").draggable({ handle: "div.handle", stack: "div.popup"});

    $("div.handle").dblclick(function() {
        $(this).parent().toggle();
    });
}

setTimeout(main, 100);

