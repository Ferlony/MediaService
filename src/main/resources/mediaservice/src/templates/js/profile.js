const url = window.location.href;


async function patchToSync(bodyjson, path){
    const response = await fetch(url + path, {
        method: 'PATCH',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(bodyjson)
    }).then(response => response.json());

    return JSON.stringify(response);
}


async function getData(path) {
    const response = await fetch(url + path, {
        method: 'GET'
    }).then(response => response.json());

    return JSON.stringify(response);
}


function getAllStorage() {
    var values = [];
    var keys = Object.keys(localStorage);

    for (var i = 0; i < keys.length; i++) {
        var item = {};
        item[keys[i]] = JSON.parse(localStorage.getItem(keys[i]));
        values.push(item);
    }

    return values;
}


function updateAllStorage(items) {
    for (var i = 0; i < items.length; i++) {
        key = Object.keys(items[i])[0];
        localStorage.setItem(key, JSON.stringify(items[i][key]));
    }
}


async function syncDevices() {
    var bodyjson = {'sync_data': getAllStorage()};
    var syncData =  await patchToSync(bodyjson, "/sync");
    var itemsArray = JSON.parse(syncData)["sync_data"];
    updateAllStorage(itemsArray);
    document.getElementById("statusData").innerHTML = null;
    document.getElementById("status").innerHTML = syncData;
}


async function getDataToLocal() {
    var savedData = await getData("/getdata");
    var itemsArray = JSON.parse(savedData)["sync_data"];
    updateAllStorage(itemsArray);
    document.getElementById("status").innerHTML = null;
    document.getElementById("statusData").innerHTML = savedData;
}
