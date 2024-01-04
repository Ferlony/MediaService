let playlist = []
const cookietype = "music";
console.log(playlist);

window.addEventListener("DOMContentLoaded", () => {
  // (A) PLAYER INIT

  // (A2) AUDIO PLAYER & GET HTML CONTROLS
  const audio = new Audio(),
        aPlay = document.getElementById("aPlay"),
        // aPlayIco = document.getElementById("aPlayIco"),
        aNow = document.getElementById("aNow"),
        aTime = document.getElementById("aTime"),
        aSeek = document.getElementById("aSeek"),
        aVolume = document.getElementById("aVolume"),
        aVolIco = document.getElementById("aVolIco"),
        aList = document.getElementById("aList");

  // (A3) BUILD PLAYLIST
  for (let i in playlist) {
    let row = document.createElement("div");
    if (i % 2 > 0) {
      row.className = "aRow";
    }
    else {
      row.className = "aRow color-mod";
    }
    row.innerHTML = String((Number(i) + 1)) + ". " + playlist[i]["name"] + "\n" + "";
    row.addEventListener("click", () => audPlay(i));
    playlist[i]["row"] = row;
    aList.appendChild(row);
  }

  // (B) PLAY MECHANISM
  // (B1) FLAGS
  let cookie = getOrCreateCookie(cookiename, cookietype);

  var audNow = cookie['playnow'], // current song
      audStart = false, // auto start next song

  // (B2) PLAY SELECTED SONG
  audPlay = (idx, nostart) => {
    audNow = idx;
    setCookieToLocalStorage(genCookie(cookietype, audNow), cookiename);
    audStart = nostart ? false : true;
    audio.src = encodeURI(playlist[idx]["src"]);
    for (let i in playlist) {
      if (i == idx) {
         playlist[i]["row"].classList.add("now"); 
      }
      else { 
        playlist[i]["row"].classList.remove("now"); 
      }
    }
  };

  // (B3) AUTO START WHEN SUFFICIENTLY BUFFERED
  audio.addEventListener("canplay", () => { 
    if (audStart) {
      audio.play();
      audStart = false;
    }
  });

  // (B4) AUTOPLAY NEXT SONG IN THE PLAYLIST
  audio.addEventListener("ended", () => {
    audNow++;
    setCookieToLocalStorage(genCookie(cookietype, audNow), cookiename);
    if (audNow >= playlist.length) { 
      audNow = 0;
      setCookieToLocalStorage(genCookie(cookietype, audNow), cookiename);
    }
    audPlay(audNow);
  });

  // (B5) INIT SET FIRST SONG
  audPlay(cookie['playnow'], true);

  // (C) PLAY/PAUSE BUTTON
  // (C1) AUTO SET PLAY/PAUSE TEXT
  audio.addEventListener("play", () => {
      // aPlayIco.innerHTML = "pause"
      var elem = document.getElementById("aPlay");
      elem.classList.add("button-pause");
      elem.classList.remove("button-play");
    }
  );

  audio.addEventListener("pause", () => {
      // aPlayIco.innerHTML = "play_arrow"
      var elem = document.getElementById("aPlay");
      elem.classList.add("button-play");
      elem.classList.remove("button-pause");
    }
  );

  // (C2) CLICK TO PLAY/PAUSE
  aPlay.addEventListener("click", () => playAudio());

  function playAudio(){
    if (audio.paused) { 
      audio.play(); 
    }
    else { 
      audio.pause(); 
    }
  };

  // (D) TRACK PROGRESS
  // (D1) SUPPORT FUNCTION - FORMAT HH:MM:SS
  var timeString = secs => {
    // (D1-1) HOURS, MINUTES, SECONDS
    let ss = Math.floor(secs),
        hh = Math.floor(ss / 3600),
        mm = Math.floor((ss - (hh * 3600)) / 60);
    ss = ss - (hh * 3600) - (mm * 60);

    // (D1-2) RETURN FORMATTED TIME
    if (hh>0) { mm = mm<10 ? "0"+mm : mm; }
    ss = ss<10 ? "0"+ss : ss;
    return hh>0 ? `${hh}:${mm}:${ss}` : `${mm}:${ss}` ;
  };

  // (D2) INIT SET TRACK TIME
  audio.addEventListener("loadedmetadata", () => {
    aNow.innerHTML = timeString(0);
    aTime.innerHTML = timeString(audio.duration);
  });

  // (D3) UPDATE TIME ON PLAYING
  audio.addEventListener("timeupdate", () => aNow.innerHTML = timeString(audio.currentTime));

  // (E) SEEK BAR
  audio.addEventListener("loadedmetadata", () => {
    // (E1) SET SEEK BAR MAX TIME
    aSeek.max = Math.floor(audio.duration);

    // (E2) USER CHANGE SEEK BAR TIME
    var aSeeking = false; // user is now changing time
    aSeek.addEventListener("input", () => aSeeking = true); // prevents clash with (e3)
    aSeek.addEventListener("change", () => {
      audio.currentTime = aSeek.value;
      if (!audio.paused) { audio.play(); }
      aSeeking = false;
    });

    // (E3) UPDATE SEEK BAR ON PLAYING
    audio.addEventListener("timeupdate", () => {
      if (!aSeeking) { aSeek.value = Math.floor(audio.currentTime); }
    });
  });

  // (F) VOLUME
  aVolIco.addEventListener("click", () => {
    audio.volume = audio.volume==0 ? 1 : 0 ;
    aVolume.value = audio.volume;
    aVolIco.innerHTML = (aVolume.value==0 ? "volume_mute" : "volume_up");
  });
  aVolume.addEventListener("change", () => {
    audio.volume = aVolume.value;
    aVolIco.innerHTML = (aVolume.value==0 ? "volume_mute" : "volume_up");
  });

  // (G) ENABLE/DISABLE CONTROLS
  audio.addEventListener("canplay", () => {
    aPlay.disabled = false;
    aVolume.disabled = false;
    aSeek.disabled = false;
  });
  audio.addEventListener("waiting", () => {
    aPlay.disabled = true;
    aVolume.disabled = true;
    aSeek.disabled = true;
  });
});
