document.onreadystatechange = function() {
    if (document.readyState !== "complete") {
        document.querySelector(
            "div").style.visibility = "visible";
        document.querySelector(
            ".spinner-grow").style.visibility = "visible";
    } else {

        document.querySelector(
            ".spinner-grow").style.display = "none";
        document.querySelector(
            "div").style.visibility = "visible";
    }
};


var counter = 20;



setInterval(function() {
    counter--;
    if (counter >= 0) {
        id = document.getElementById("count");
        id.innerHTML = counter;
    }
    if (counter == 0) {
        alert("Time is up!");
    }

}, 1000);