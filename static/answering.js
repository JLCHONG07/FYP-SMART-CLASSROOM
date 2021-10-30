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