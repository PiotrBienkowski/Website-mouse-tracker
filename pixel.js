lastUpdate = parseInt(Date.now() / 1000);
lastAdd = parseInt(Date.now() / 1000);
updateFrequency = 3;
addFrequency = 0.5;

class Data {
    constructor(x, y) {
        this.x = x;
        this.y = x;
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
        console.log("-----ADDED-----");
    }
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