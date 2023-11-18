function removeCookie(cookieName){
    document.cookie = cookieName + '=' + null; 
}


function logoutButton(){
    removeCookie("access_token")
    document.getElementById("status").innerHTML = "JWT removed";
}
