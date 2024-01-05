var download_path = "downloadzip/";
var root_url = location.protocol + '//' + location.host;


async function downloadZip(path, data) {
    const response = await fetch(root_url + path + data, {
        method: 'GET'
    }).then(res => {
        const disposition = res.headers.get('Content-Disposition');
        filename = disposition.split(/;(.+)/)[1].split(/=(.+)/)[1];
        if (filename.toLowerCase().startsWith("utf-8''"))
            filename = decodeURIComponent(filename.replace("utf-8''", ''));
        else
            filename = filename.replace(/['"]/g, '');
        return res.blob();
    })
    .then(blob => {
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a); // append the element to the dom
        a.click();
        a.remove(); // afterwards, remove the element  
    });;

}


async function downloadButtonPics(data) {
    return await downloadZip("/pictures/" + download_path, data)
}


async function downloadButtonMus(data) {
    return await downloadZip("/music/" + download_path, data)
}


async function downloadButtonVid(data) {
    return await downloadZip("/videos/" + download_path, data)
}


async function downloadButtonText(data) {
    return await downloadZip("/textfiles/" + download_path, data)
}
