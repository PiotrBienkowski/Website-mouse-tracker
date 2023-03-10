lastUpdate = parseInt(Date.now() / 1000);
lastAdd = parseInt(Date.now() / 1000);
updateFrequency = 3;
addFrequency = 0.5;
token = "97c98f9d4eb1da15ba542af8abcd12d4"
url = "http://127.0.0.1:8000/add-data"

class Data {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

var tmpData = new Array();

document.addEventListener("mousemove", function(event) {
    log(event.clientX, event.clientY, window.pageYOffset);
});

function log(userX, userY, pageYOffset) {
    xSize = document.body.scrollWidth;
    ySize = document.body.scrollHeight;

    retX = (userX / xSize) * 100;
    retY = ((userY + pageYOffset) / ySize) * 100;
    
    if (checkAdd()) {
        lastAdd = parseInt(Date.now() / 1000);
        tmpData.push(new Data(retX, retY));
    }
    addToApi();
}

function addToApi() {
    if (checkUpdate()) {
        lastUpdate = parseInt(Date.now() / 1000);
        sendToAPI();
        console.log("-----ADDED-----");
    }
}

function sendToAPI() {
    let data = {
        token: token,
        list: tmpData
    };
      
    fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
      
}

function checkAdd() {
    timeNow = Date.now() / 1000;
    if (Math.abs(timeNow - lastAdd) >= addFrequency){
        return true;
    }
    return false;
}

function checkUpdate() {
    timeNow = Date.now() / 1000;
    if (Math.abs(timeNow - lastUpdate) >= updateFrequency){
        return true;
    }
    return false;
}