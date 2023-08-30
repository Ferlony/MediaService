const videoCookieDefault = {'type': 'video', 'playnow': 0};
const musicCookieDefault = {'type': 'music', 'playnow': 0};


function setCookieToLocalStorage(data, cookiename) {
  localStorage.setItem(cookiename, JSON.stringify(data));
}

function getCookieFromLocalStorage(cookiename) {
  return JSON.parse(localStorage.getItem(cookiename));
}

function genCookie(type, playnow){
  return {'type': type, 'playnow': playnow};
}

function getOrCreateCookie(cookiename){
    if (getCookieFromLocalStorage(cookiename) == null){
      setCookieToLocalStorage(videoCookieDefault, cookiename);
    }
    return getCookieFromLocalStorage(cookiename);
}
