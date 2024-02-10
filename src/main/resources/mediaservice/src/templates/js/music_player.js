let playlist = []
const cookietype = "music";
console.log(playlist);

let cookie = getOrCreateCookie(cookiename, cookietype);
var audNow = cookie['playnow'] // current song

window.addEventListener("DOMContentLoaded", () => {
    // (A) PLAYER INIT

    let loopFlag = false;

    // (A2) AUDIO PLAYER & GET HTML CONTROLS
    const audio = new Audio(),
        aPlay = document.getElementById("aPlay"),
        aNow = document.getElementById("aNow"),
        aTime = document.getElementById("aTime"),
        aSeek = document.getElementById("aSeek"),
        aVolume = document.getElementById("aVolume"),
        aVolIco = document.getElementById("aVolIco"),
        aList = document.getElementById("aList"),
        aLoop = document.getElementById("aLoop");

    // (A3) BUILD PLAYLIST
    for (let i in playlist) {
        let row = document.createElement("div");
        if (i % 2 > 0) {
            row.className = "aRow";
        }
        else {
            row.className = "aRow color-mod";
        }
        row.innerHTML = String((Number(i) + 1)) + ". " + playlist[i]["name"] + "&nbsp;&nbsp;&nbsp;&nbsp;" + playlist[i]["album"];
        row.addEventListener("click", () => audPlay(i));
        playlist[i]["row"] = row;
        aList.appendChild(row);
    }

    // (B) PLAY MECHANISM
    // (B1) FLAGS
    var audStart = false, // auto start next song

        // (B2) PLAY SELECTED SONG
        audPlay = (idx, nostart) => {
            audNow = idx;
            setCookieToLocalStorage(genCookie(cookietype, audNow), cookiename);
            setCurrentTrackStatus(playlist[audNow]["name"], playlist[audNow]["album"])
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
        if (loopFlag){
            audPlay(audNow);
        }
        else {
            nextSong();
        }
    });

    // (B5) INIT SET FIRST SONG
    audPlay(cookie['playnow'], true);
    setCurrentTrackStatus(playlist[cookie['playnow']]["name"], playlist[cookie['playnow']]["album"]);


    function setCurrentTrackStatus(name, album) {
        let currentTrack = document.getElementById("currentTrack");
        let currentAlbum = document.getElementById("currentAlbum");
        currentTrack.innerHTML = name;
        currentAlbum.innerHTML = album;
    }


    // (C) PLAY/PAUSE BUTTON
    // (C1) AUTO SET PLAY/PAUSE TEXT
    audio.addEventListener("play", () => {
        // aPlayIco.innerHTML = "pause"
        let elem = document.getElementById("aPlay");
        elem.classList.add("button-pause");
        elem.classList.remove("button-play");
    }
    );

    audio.addEventListener("pause", () => {
        // aPlayIco.innerHTML = "play_arrow"
        let elem = document.getElementById("aPlay");
        elem.classList.add("button-play");
        elem.classList.remove("button-pause");
    }
    );


    // (C2) CLICK TO PLAY/PAUSE
    aPlay.addEventListener("click", () => playAudio());

    function playAudio() {
        if (audio.paused) {
            audio.play();
        }
        else {
            audio.pause();
        }
    };

    window.loopSong = function () {
        if (!loopFlag) {
            loopFlag = true;
            aLoop.classList.remove("button-loop");
            aLoop.classList.add("button-loop-dark");
        }
        else {
            loopFlag = false;
            aLoop.classList.remove("button-loop-dark");
            aLoop.classList.add("button-loop");
        }
    };

    window.nextSong = function () {
        audNow++;
        if (audNow >= playlist.length) {
            audNow = 0;
        }
        audPlay(audNow);
    };

    window.prevSong = function () {
        if (audNow == 0) {
            audNow = playlist.length - 1;
        }
        else {
            audNow--;
        }
        audPlay(audNow);
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
        if (hh > 0) { mm = mm < 10 ? "0" + mm : mm; }
        ss = ss < 10 ? "0" + ss : ss;
        return hh > 0 ? `${hh}:${mm}:${ss}` : `${mm}:${ss}`;
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
        audio.volume = audio.volume == 0 ? 1 : 0;
        aVolume.value = audio.volume;
        toggleVolumeIcon(aVolume.value);

    });

    function toggleVolumeIcon(volumeValue) {
        var elem = document.getElementById("aVolIco");
        if (volumeValue == 0) {
            elem.classList.remove("button-volume");
            elem.classList.add("button-mute");
        }
        else {
            elem.classList.remove("button-mute");
            elem.classList.add("button-volume");
        }
    }

    aVolume.addEventListener("change", () => {
        audio.volume = aVolume.value;
        toggleVolumeIcon(aVolume.value);
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
