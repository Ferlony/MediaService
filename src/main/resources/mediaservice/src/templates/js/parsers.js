const url = window.location.href;


async function postForParser(bodyjson){
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(bodyjson)
    }).then(response => response.json())

    return JSON.stringify(response);
}


async function parserButton(parser_type){
    if (parser_type == "youtube"){
        var bodyjson = youtubeMenu();
        var responseStatus = await postForParser(bodyjson);
    }
    else if (parser_type == "songlyrics"){
        var bodyjson = songlyricsMenu();
        var responseStatus = await postForParser(bodyjson);
    }
    else if (parser_type == "EnumJs"){
        var bodyjson = enumJsMenu();
        var responseStatus = await postForParser(bodyjson);
    }
    else if (parser_type == "withHeaders"){
        var bodyjson = withHeadersMenu();
        var responseStatus = await postForParser(bodyjson);
    }
    console.log(responseStatus);
    document.getElementById("responseStatus").innerHTML = responseStatus;
}


function youtubeMenu(){
    var downloadUrl = document.getElementById("downloadUrlYoutube").value;
    var parser_type = 1;
    var action;

    if (document.getElementById("youtube1").checked){
        action = 1;
    }
    else if (document.getElementById("youtube2").checked){
        action = 2;
    }
    else if (document.getElementById("youtube3").checked){
        action = 3;            
    }
    else if (document.getElementById("youtube4").checked){
        action = 4;
    }
    return {
        'url': downloadUrl,
        'parser_type': parser_type,
        'action': action
    };
}


function songlyricsMenu(){
    var downloadUrl = document.getElementById("downloadUrlSonglyrics").value;
    var parser_type = 2;
    var action;

    if (document.getElementById("songlyrics1").checked){
        action = 1;
    }
    else if (document.getElementById("songlyrics2").checked){
        action = 2;
    }

    return {
        'url': downloadUrl,
        'parser_type': parser_type,
        'action': action
    };
}


function enumJsMenu(){
    var downloadUrl = document.getElementById("downloadUrlEnumJs").value;
    var parser_type = 3;
    var action = 0;

    return {
        'url': downloadUrl,
        'parser_type': parser_type,
        'action': action
    };
}


function withHeadersMenu(){
    var downloadUrl = document.getElementById("downloadUrlHeaders").value;
    var parser_type = 4;
    var action = 0;

    return {
        'url': downloadUrl,
        'parser_type': parser_type,
        'action': action
    };
}
