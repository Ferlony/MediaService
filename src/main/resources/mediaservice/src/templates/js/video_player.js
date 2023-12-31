let playlist = [];
const cookietype = "video";
console.log(playlist);



window.addEventListener("DOMContentLoaded", () => {
    // (A) PLAYER INIT

  
    // (A2) VIDEO PLAYER & GET HTML CONTROLS
    //vVid
    const video = document.getElementById("my-video"),
          vList = document.getElementById("vList");



    // (A3) BUILD PLAYLIST
    for (let i in playlist) {
      let row = document.createElement("div");
      if (i % 2 > 0){
        row.className = "vRow";
      }
      else{
        row.className = "vRow color-mod";
      }
      row.innerHTML = String((Number(i) + 1)) + ". " + playlist[i]["name"];
      row.addEventListener("click", () => vidPlay(i));
      playlist[i]["row"] = row;
      vList.appendChild(row);
    }
  
    // (B) PLAY MECHANISM
    // (B1) FLAGS

    let cookie = getOrCreateCookie(cookiename, cookietype);

    var vidNow = cookie['playnow'], // current video
        vidStart = false, // auto start next video
  
    // (B2) PLAY SELECTED VIDEO
    vidPlay = (idx, nostart) => {
      vidNow = idx;
      setCookieToLocalStorage(genCookie(cookietype, vidNow), cookiename);
      vidStart = nostart ? false : true;
      video.src = encodeURI(playlist[idx]["src"]);
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
    video.addEventListener("canplay", () => { 
      if (vidStart) {
      video.play();
      vidStart = false;
      }
    });
  
    // (B4) AUTOPLAY NEXT VIDEO IN THE PLAYLIST
    video.addEventListener("ended", () => {
      vidNow++;
      if (vidNow >= playlist.length) { 
        vidNow = 0; 
      }
      vidPlay(vidNow);
    });
  
    // (B5) INIT SET FIRST VIDEO
    vidPlay(cookie['playnow'], true);
  
    // (C2) CLICK TO PLAY/PAUSE
    video.addEventListener("click", () => playVideo());

    function playVideo(){
      if (video.paused) { 
        video.play(); 
      }
      else { 
        video.pause(); 
      }
    };


});
