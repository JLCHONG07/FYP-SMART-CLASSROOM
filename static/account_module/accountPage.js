//select admin or student login and change color of "Student" or "Admin words"
$(".choice").click(function(e) {
    $(".choice").removeClass("active");
    $(this).addClass("active")
})

//input container for email and password change the border color when click on it 
$(".text-container").click(function(e) {
    $(".text-container").removeClass("active-text-container");
    $(this).addClass("active-text-container")
})

//Password eye change from dot to text or text to dot when eye is open/closed
$("svg.pass-eye").click(function(e) {

    var eyeColor = $(this).find("path").attr('fill');
    // console.log(eyeColor);

    if (eyeColor == "#C4C4C4") {
        $(this).find("path").attr("fill", "#0077FF");
        var pass = $("form").find('input:password').attr("type", "text");
        // console.log(pass);

    } else {
        $(this).find("path").attr("fill", "#C4C4C4");
        $("form").find('.password-form').attr("type", "password");
    }

})

function register_done() {

    alert("Successful Register Please Login to Continue!");
    location.href = "login";
}

$(document).ready(function() {
    $("#admin-choice").click(function() {
        $("#hidField").val("admin").trigger("change");
    });

    $("#student-choice").click(function() {
        $("#hidField").val("student").trigger("change");
    });



})