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


// Not in use?
function getNameFromJWT(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    } 
}

function getAllStorage() {
    var values = [];
    var keys = Object.keys(localStorage);

    for (var i = 0; i < keys.length; i++) {
        var item = {};
        item[keys[i]] = localStorage.getItem(keys[i]);
        values.push(item);
    }

    return values;
}

function updateAllStorage() {
    
}


async function syncDevices() {
    var bodyjson = {'sync_data': getAllStorage()}
    var syncData = await patchToSync(bodyjson, "/sync")
    console.log(syncData)
    document.getElementById("status").innerHTML = syncData;
}
