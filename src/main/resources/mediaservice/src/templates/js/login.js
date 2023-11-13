const url = window.location.href;


async function postForUser(bodyjson){
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


async function loginButton(){
    var username = document.getElementById("login").value;
    var password = document.getElementById("password").value;

    var bodyjson = {
        "username": username,
        "password": password
    };

    var responseStatus = await postForUser(bodyjson);
    var status = setTokenToLocalStorage(responseStatus);
    //console.log(responseStatus);
    document.getElementById("responseStatus").innerHTML = status;
}

function setTokenToLocalStorage(data){
    jwt = JSON.parse(data);
    //sessionStorage.setItem("access_token", jwt["access_token"]);
    document.cookie = 'access_token=' + jwt["access_token"]; 
    return "Token set";
}
