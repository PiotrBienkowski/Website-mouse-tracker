lastUpdate = parseInt(Date.now() / 1000);
updateFrequency = 3;

document.addEventListener("mousemove", function(event) {
    console.log(`Pozycja myszki: x=${event.clientX}, y=${event.clientY}`);
    console.log(`Przesunięcie w dół: ${window.pageYOffset}`);
    console.log(document.documentElement.scrollHeight);
    console.log(document.body.scrollWidth);
});

function log(userX, userY, pageOffset) {
    
}

function checkUpdate() {
    timeNow = Date.now() / 1000;
    if (Math.abs(timeNow - lastUpdate) >= updateFrequency){
        return true;
    }
    return false;
}