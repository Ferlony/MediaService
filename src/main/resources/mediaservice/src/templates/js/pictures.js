let picList = [];
const PIC_STEP = 30;
var pics_counter = 0


function __addNextPics() {
    var elem = document.getElementById("picblock");
    var current_pics_counter = pics_counter;
    for (pics_counter; pics_counter < (current_pics_counter + PIC_STEP); pics_counter++) {
        let name = picList[pics_counter]["name"];
        let src = picList[pics_counter]["src"];
        var html_to_insert = (' \
        <li> \
            <a href="' + src + '" target="_blank"> \
            <img class="img-fit" src="' + src + '" \
                alt="Cant load: ' + name + '" /> \
            </a> \
        </li> \
        ');
        elem.insertAdjacentHTML('beforeend', html_to_insert);
    }

}


function addNextPics() {
    if ((PIC_STEP < picList.length) && (pics_counter < picList.length) && (pics_counter < (picList.length - PIC_STEP))) {
        __addNextPics();
    }
    else {
        addAllPics();
    }
}


function addAllPics() {
    var elem = document.getElementById("picblock");
    for (pics_counter; pics_counter < picList.length; pics_counter++) {
        let name = picList[pics_counter]["name"];
        let src = picList[pics_counter]["src"];
        var html_to_insert = (' \
        <li> \
            <a href="' + src + '" target="_blank"> \
            <img class="img-fit" src="' + src + '" \
                alt="Cant load: ' + name + '" /> \
            </a> \
        </li> \
        ');
        elem.insertAdjacentHTML('beforeend', html_to_insert);
    }

}


window.addEventListener("DOMContentLoaded", () => {
    console.log(picList);
    addNextPics();

});
