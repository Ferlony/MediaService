const videoCookieDefault = {'type': 'video', 'playnow': 0, 'date': '0'};
const musicCookieDefault = {'type': 'music', 'playnow': 0, 'date': '0'};


function setCookieToLocalStorage(data, cookiename) {
  localStorage.setItem(cookiename, JSON.stringify(data));
}

function getCookieFromLocalStorage(cookiename) {
  return JSON.parse(localStorage.getItem(cookiename));
}

function genCookie(type, playnow){
  return {'type': type, 'playnow': playnow, 'date': getCurrentDate()};
}

function getOrCreateCookie(cookiename, cookietype){
    if (getCookieFromLocalStorage(cookiename) == null){
      if (cookietype == "video"){
        setCookieToLocalStorage(videoCookieDefault, cookiename);
      }
      else if (cookietype == "music"){
        setCookieToLocalStorage(musicCookieDefault, cookiename)
      }
    }
    return getCookieFromLocalStorage(cookiename);
}

function getCurrentDate() {
  let d = new Date(new Date().toLocaleString("en-US", {timeZone: "Europe/Dublin"})); // timezone: UTC-0
  var datestring =  d.getFullYear().toString() + "-" + (d.getMonth() + 1).toString() + "-" + d.getDate().toString() + " " + d.getHours().toString() + ":" + d.getMinutes().toString() + ":" + d.getSeconds().toString();
  return datestring
}
