document.onreadystatechange = function() {
    if (document.readyState !== "complete") {
        document.querySelector(
            "div").style.visibility = "visible";
        document.querySelector(
            ".spinner-grow").style.visibility = "visible";
    } else {
        startCount=TRUE;
        document.querySelector(
            ".spinner-grow").style.display = "none";
        document.querySelector(
            "div").style.visibility = "visible";
    }
};


        var counter = 10;
        var startCount = FALSE

        if (startCount === TRUE) {
        setInterval(function(){ 
            counter--;
            if (counter >=0){
                id = document.getElementById("count");
                id.innerHTML = counter;
            }
            if(counter ==0){
                alert("Time is up!");
            }
        
        },1000);
    }