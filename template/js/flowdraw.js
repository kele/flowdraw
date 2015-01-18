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
        msgId--;

        var x = event.pageX;
        var y = event.pageY;

        var message = "<strong>" 
                        + messageText 
                        + "</strong><br><pre style=\"font-size: 8pt;\">" 
                        + messageContents[msgId] 
                        + "</pre>";

        var div_style = "position: absolute;";
        div_style += "top: " + y + "px;";
        div_style += "left: " + x + "px;";

        var handle = "<div class=\"handle\"></div><br>";

        var div = "<div class=\"popup\" style=\""
                    + div_style 
                    + "\"> " 
                    + handle 
                    + "<div class=\"popup_content\">" 
                    + message 
                    + "</div></div>";

        $("body").append(div);
        $("div.popup").draggable({ handle: "div.handle", stack: "div.popup"});

        $("div.handle").dblclick(function() {
            $(this).parent().remove();
        });
    });

    $("text").each(function() {
        this.style.fontSize = "9pt";
    });
}

setTimeout(main, 100);

