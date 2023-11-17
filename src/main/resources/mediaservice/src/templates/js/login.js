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
    document.getElementById("responseStatus").innerHTML = status;
}

function setTokenToLocalStorage(data){
    jwt = JSON.parse(data);
    //sessionStorage.setItem("access_token", jwt["access_token"]);
    const cookieName = "access_token";
    const cookieValue = jwt["access_token"];
    const daysToExpire = new Date(2147483647 * 1000).toUTCString();

    document.cookie = cookieName + '=' + cookieValue + '; expires=' + daysToExpire;

    return "Token set";
}
