var timeOut = 0;
const move = 100

var scrollFun = function(e) {
  if (e.type == "mousedown") {
    timeOut = setInterval(function() {
      if (e.target.id == "btn-scroll-up")
        window.scroll(0, window.scrollY - move);
      else window.scroll(0, window.scrollY + move);
    }, 0);
  }

  if (e.type == "mouseup") {
    clearInterval(timeOut);
  }
};

document.getElementById("btn-scroll-down").addEventListener("mousedown", scrollFun, false)
document.getElementById("btn-scroll-down").addEventListener("mouseup", scrollFun, false)

document.getElementById("btn-scroll-up").addEventListener("mousedown", scrollFun, false)
document.getElementById("btn-scroll-up").addEventListener("mouseup", scrollFun, false)
