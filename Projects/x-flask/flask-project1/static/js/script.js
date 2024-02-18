

function httpGet(theUrl)
{
    console.log("httpGet: "+theUrl);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function main()
{
    console.log("log: main");

    button_clicker = document.getElementById("clicker");
    button_save  = document.getElementById("save");
    button_reset  = document.getElementById("reset");
    last_time   = document.getElementById("last_time");
    
    last_count_text = document.getElementById("last_count");
    user_id = document.getElementById("user_id").innerText;

    button_clicker.onclick=function(){
        last_count = parseInt(last_count_text.innerText);
        last_count_text.textContent = String(last_count+1);
    }

    button_save.onclick=function(){
        user_count = parseInt(last_count_text.innerText);
        new_time = httpGet("/save/"+user_id+"/"+user_count);
        last_time.textContent = new_time;
    }

    button_reset.onclick=function(){
        new_time = httpGet("/reset/"+user_id);
        last_count_text.textContent = 0;
        last_time.textContent = new_time;
    }
}