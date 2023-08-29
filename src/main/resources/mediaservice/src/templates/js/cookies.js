const videoCookieDefault = {'type': 'video', 'playnow': 0};


function setCookieToLocalStorage(data, cookiename) {
  localStorage.setItem(cookiename, JSON.stringify(data));
}

function getCookieFromLocalStorage(cookiename) {
  return JSON.parse(localStorage.getItem(cookiename));
}

function genVideoCookie(type, playnow){
  return {'type': type, 'playnow': playnow};
}

function getOrCreateCookie(cookiename){
  try {
    return getCookieFromLocalStorage(cookiename);
  }
  catch (error){
    setCookieToLocalStorage(videoCookieDefault, cookiename);
    return getCookieFromLocalStorage(cookiename);
  }
}
